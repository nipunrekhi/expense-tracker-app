from expense_tracker.expense_manager import ExpenseManager
from expense_tracker.storage import load_expenses
from expense_tracker.exceptions import ExpenseNotFoundError
import pytest


def test_add_expense():
    manager = ExpenseManager()

    manager.add_expense(amount=100, category="Food", description="Pizza")

    assert len(manager.expenses) == 1
    assert manager.expenses[0].amount == 100
    assert manager.expenses[0].category == "Food"
    assert manager.expenses[0].description == "Pizza"


def test_view_expenses():
    expenses = load_expenses()
    manager = ExpenseManager(expenses)
    manager.view_expenses()
    assert len(manager.expenses) == 1


def test_delete_expense():
    manager = ExpenseManager()

    manager.add_expense(200, "Travel", "Bus")

    expense_id = str(manager.expenses[0].id)

    manager.delete_expense(expense_id)

    assert len(manager.expenses) == 0
    assert expense_id not in [
        expense.id for expense in manager.expenses
    ], "Expense not deleted"


def test_delete_missing_expense():
    manager = ExpenseManager()
    with pytest.raises(ExpenseNotFoundError):
        manager.delete_expense("nonexistent-id")
