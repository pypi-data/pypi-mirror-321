"""
This type stub file was generated by pyright.
"""

class StopCodemodException(Exception):
    """Raises when the codemod execution should stop early.
    This gets caught upstream and causes an early exit so that we can surface a subset of the results to the user for faster iteration.
    """
    threshold: int | None = ...
    def __init__(self, message: str | None = ..., threshold: int | None = ...) -> None:
        ...
    


class MaxTransactionsExceeded(StopCodemodException):
    """Raised when the number of transactions exceeds the max_transactions limit.
    This gets caught upstream and causes an early exit so that we can surface a subset of the results to the user for faster iteration.
    """
    ...


class MaxPreviewTimeExceeded(StopCodemodException):
    """Raised when more than the allotted time has passed for previewing transactions. Enables us to keep it at like ~5s in the frontend during debugging"""
    ...


class MaxAIRequestsError(StopCodemodException):
    """Raised when the number of AI requests exceeds the max_ai_requests limit.

    This gets caught upstream and causes an early exit so that we can surface a subset of the
    results to the user for faster iteration.
    """
    ...


