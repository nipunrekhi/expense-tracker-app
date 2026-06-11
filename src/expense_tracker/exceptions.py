class ExpenseTrackerError(Exception):
    """Base exception for the expense tracker"""


class ExpenseNotFoundError(ExpenseTrackerError):
    """Exception raised when an expense is not found"""

    def __init__(self, expense_id: str) -> None:
        self.expense_id = expense_id
        super().__init__(f"Expense with ID {expense_id} not found")


class InvalidExpenseDataError(ExpenseTrackerError):
    """Exception raised when invalid expense data is provided"""

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


class StorageError(ExpenseTrackerError):
    """Exception raised when there is an error with the storage"""

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)
