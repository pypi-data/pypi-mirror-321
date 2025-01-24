from collections.abc import Iterable
from os import urandom

import httpx

from .timezones import naivenow

try:
    from rest_framework.exceptions import APIException
    from rest_framework.status import HTTP_503_SERVICE_UNAVAILABLE
except ImportError:

    class APIException(Exception):
        pass

    HTTP_503_SERVICE_UNAVAILABLE = 503


def get_event_id():
    dt = naivenow()
    d = dt.date()
    t = dt.timestamp() % 86400
    return f"{d.year:2}{d.month:02}{d.day:02}:{urandom(4).hex()}:{t:08.2f}"


class TaggedError(Exception):
    def __init__(self, *details, event_id):
        super().__init__(*details)
        self.event_id = event_id

    def __str__(self):
        return f"{type(self).__name__}({', '.join(map(str, self.args))})"

    def __repr__(self):
        args = [repr(arg) for arg in self.args]
        args.append(f"event_id={self.event_id}")
        return f"{type(self).__name__}({', '.join(args)})"


class RetryableError(TaggedError):
    """
    Either the service is down or temporarily broken (eg: 404/5xx states, malformed responses etc). Retryable.
    """


class HTTPErrorMixin:
    status_code: int
    response: httpx.Response

    def __init__(self, response, *args, event_id):
        super().__init__(response, *args, event_id=event_id)
        self.status_code = response.status_code
        self.response = response


class InternalServiceError(TaggedError):
    """
    The service failed in handling (expected fields are missing, buggy code etc). Not retryable.
    """


class DecodeError(HTTPErrorMixin, InternalServiceError):
    """
    When content decoding fails.
    """

    def __init__(self, response, error, *, event_id):
        super().__init__(response, error, event_id=event_id)
        self.error = error

    def __str__(self):
        return f"DecodeError({self.response}, error={self.error!r})"


class RetryableStatusError(HTTPErrorMixin, RetryableError):
    """
    When response status is bad, but retryable.
    """

    def __init__(self, response, accept_statuses, event_id):
        super().__init__(response, accept_statuses, event_id=event_id)
        self.accept_statuses = accept_statuses

    def __str__(self):
        return f"RetryableStatusError({self.response}, accept_statuses={self.accept_statuses})"


class UnexpectedStatusError(HTTPErrorMixin, InternalServiceError):
    """
    When response status is bad.
    """

    def __init__(self, response, accept_statuses, event_id):
        super().__init__(response, accept_statuses, event_id=event_id)
        self.accept_statuses = accept_statuses

    def __str__(self):
        return f"UnexpectedStatusError({self.response}, accept_statuses={self.accept_statuses})"


class ExhaustedRetriesError(InternalServiceError):
    """
    The service reached the retry limit. Obviously not retryable.
    """


class OpenServiceError(TaggedError):
    """
    The service failed in handling in a way that should be propagated upward the public API.

    The `event_id` is a mandatory parameter to encourage adding a relevant event_id if created from within a context.
    """

    message: str = "Unknown error"
    error_code: str = "unknown"
    status_code: int = HTTP_503_SERVICE_UNAVAILABLE

    def __init__(self, message=None, *, details: Iterable = (), event_id):
        super().__init__(*details, event_id=event_id)
        self.message = str(message or self.message)

    def as_api_service_error(self):
        exc = APIServiceError(
            self.message,
            error_code=self.error_code,
            status_code=self.status_code,
            event_id=self.event_id,
            cause=self,
        )
        return exc


class APIServiceError(APIException):
    status_code = HTTP_503_SERVICE_UNAVAILABLE
    accident_id_field = "accident_id"
    message_field = "detail"
    error_code_field = "code"

    def __init__(self, message, *, error_code="unavailable", status_code=None, event_id=None, cause=None, **kwargs):
        self.message = message
        self.code = error_code
        self.detail = {
            self.accident_id_field: get_event_id() if event_id is None else event_id,
            self.message_field: message,
            self.error_code_field: error_code,
            **kwargs,
        }
        if status_code:
            self.status_code = status_code
        if cause:
            self.__cause__ = cause
