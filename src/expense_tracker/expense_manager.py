from numbers import Number

from .exceptions import ExpenseNotFoundError
from .utils import json_to_dict
from .models import Expense
from .storage import save_expenses
from datetime import datetime


class ExpenseManager:
    def __init__(self, expenses: list[Expense] or None = None) -> None:
        self.expenses: list[Expense] = expenses if expenses else []

    def add_expense(self, amount: float, category: str, description: str) -> None:
        self.expenses.append(
            Expense(amount=amount, category=category, description=description)
        )
        print(f"Expense added successfully: {self.expenses[-1].to_dict()}")
        save_expenses(self.expenses)

    def view_expenses(self) -> None:
        print(json_to_dict([expense.to_dict() for expense in self.expenses]))

    def delete_expense(self, expense_id: str) -> None:
        expense_to_delete = next(
            (expense for expense in self.expenses if str(expense.id) == expense_id),
            None,
        )
        if expense_to_delete is None:
            raise ExpenseNotFoundError(expense_id)

        self.expenses.remove(expense_to_delete)
        save_expenses(self.expenses)
        print(f"Expense deleted successfully: {expense_id}")

    def edit_expense(
        self, expense_id: str, amount: float, category: str, description: str
    ) -> None:
        expense_to_edit = next(
            (expense for expense in self.expenses if str(expense.id) == expense_id),
            None,
        )
        if expense_to_edit is None:
            print(f"Expense with ID {expense_id} not found")
            return
        expense_to_edit.amount = amount
        expense_to_edit.category = category
        expense_to_edit.description = description
        save_expenses(self.expenses)
        print(f"Expense edited successfully: {expense_id}")

    def view_expense_by_id(self, expense_id: str) -> None:
        expense_to_view = next(
            (expense for expense in self.expenses if str(expense.id) == expense_id),
            None,
        )
        if expense_to_view is None:
            print(f"Expense with ID {expense_id} not found")
            return
        print(
            f"Expense with ID {expense_id}: {json_to_dict([expense_to_view.to_dict()])}"
        )

    def view_expenses_by_category(self, category: str) -> None:
        expenses = [
            expense
            for expense in self.expenses
            if expense.category.lower() == category.lower()
        ]

        if not expenses:
            print(f"No expenses found for category: {category}")
            return

        print(json_to_dict([expense.to_dict() for expense in expenses]))

    def total_expenses(self) -> Number:
        total = sum([expense.amount for expense in self.expenses])
        print(f"Total expenses: {total}")
        return total

    def view_expenses_by_date(self, date: str) -> None:
        date = datetime.fromisoformat(date)
        expenses = [
            expense
            for expense in self.expenses
            if expense.date.month == date.month and expense.date.year == date.year
        ]
        if not expenses:
            print(f"No expenses found for date: {date}")
            return
        print(json_to_dict([expense.to_dict() for expense in expenses]))
