import json
import logging
from io import BytesIO
from pathlib import Path
from typing import Any, Callable, Iterable

import falcon
import numpy as np
import requests
from filelock import FileLock, Timeout


class StaticJSONResource:
    """Any JSON serializable object, representing a "static" resource (i.e. a
    resource that does not depend on request parameters).

    The object will be represented as a plain JSON string, when a GET request is
    invoked."""

    def __init__(self, obj: Any):
        """
        Parameters
        ----------
        obj : Any
            A JSON serializable object, i.e. is should be compatible with
            `json.dumps`.
        """
        self._obj = obj

    def on_get(self, _, resp: falcon.Response):
        resp.text = json.dumps(self._obj)


class FitResource:
    def __init__(
        self,
        data_getter: Callable[[], dict[str, np.ndarray]],
        model: Any,
        model_filepath: str | Path,
    ) -> None:
        self._get_fit_data = data_getter
        self._model = model
        self._model_filepath = Path(model_filepath)
        self._model_lock = FileLock(
            self._model_filepath.with_suffix(".lock"), blocking=False
        )

    def on_post(self, req: falcon.Request, resp: falcon.Response) -> None:
        logging.info("Obtaining fitting data.")
        fit_data = self._get_fit_data()
        try:
            with self._model_lock:
                logging.info("Initiating fitting.")
                self._model.fit(**fit_data)
                logging.info("Persisting fitted model.")
                self._model.save(self._model_filepath)
        except Timeout:
            error_msg = "Fitting is already in progress. Aborting current attempt."
            logging.exception(error_msg)
            raise falcon.HTTPError(
                status=falcon.HTTP_SERVICE_UNAVAILABLE,
                description=json.dumps(dict(message=error_msg)),
            )
        success_message = "Fitting has been completed successfully."
        logging.info(success_message)
        resp.text = json.dumps(dict(message=success_message))


def named_ndarrays_to_bytes(named_arrays: dict[str, np.ndarray]) -> bytes:
    """Convert named NumPy arrays to a compressed bytes sequence.

    Use this for example as payload data in a POST request.

    Parameters
    ----------
    named_arrays : dict[str, np.ndarray]
        The named NumPy arrays.

    Returns
    -------
    bytes
        A compressed bytes sequence.

    Notes
    -----
    This is the inverse to `bytes_to_named_ndarrays`.
    """
    compressed_arrays = BytesIO()
    np.savez_compressed(compressed_arrays, **named_arrays)
    return compressed_arrays.getvalue()


def bytes_to_named_ndarrays(data: bytes) -> dict[str, np.ndarray]:
    """Convert a bytes sequence of named (and compressed) NumPy arrays back to
    arrays.

    Use this for example to retrieve NumPy arrays from an HTTP response.

    Parameters
    ----------
    data : bytes
        The bytes representation of a (compressed)

    Returns
    -------
    dict[str, np.ndarray]
        The named arrays.

    Raises
    ------
    OSError
        If the input file does not exist or cannot be read.
    ValueError
        If the file contains an object array.


    Notes
    -----
    This in the inverse to `named_ndarrays_to_bytes`.
    """
    arrays = np.load(BytesIO(data))
    return {name: arrays[name] for name in arrays.files}


def get_named_arrays_or_raise(
    data_url: str,
    expected_array_labels: Iterable[str],
    params: dict[str, Any] | None = None,
    timeout: float | None = None,
) -> dict[str, np.ndarray]:
    try:
        data_resp = requests.get(url=data_url, params=params, timeout=timeout)
        if data_resp.status_code != 200:
            raise ValueError()
    except (requests.ConnectionError, ValueError):
        error_msg = "Unable to obtain data from remote location (timeout or error)."
        logging.exception(error_msg)
        raise falcon.HTTPServiceUnavailable(description=error_msg)
    arrays = parse_named_arrays_or_raise(
        data_resp.content,
        expected_array_labels=expected_array_labels,
        error_status=falcon.HTTP_INTERNAL_SERVER_ERROR,
        error_message="Array payload validation failed.",
    )
    return arrays


def parse_named_arrays_or_raise(
    payload: bytes,
    expected_array_labels: Iterable[str],
    error_status: str | int,
    error_message: str | None = None,
) -> dict[str, np.ndarray]:
    try:
        arrays = bytes_to_named_ndarrays(payload)
        if not all(
            [expected_label in arrays for expected_label in expected_array_labels]
        ):
            raise ValueError("Array payload does not contain all expected labels.")
    except (OSError, ValueError, EOFError):
        if error_message is None:
            error_message = "Array payload parsing (or validation) failed."
        logging.exception(error_message)
        raise falcon.HTTPError(status=error_status, description=error_message)
    return arrays
