from expense_tracker.error_handler import run_and_handle_error
from expense_tracker.exceptions import ExpenseTrackerError
from expense_tracker.expense_manager import ExpenseManager
from expense_tracker.storage import load_expenses
from expense_tracker.validators import get_float_input, get_string_input

manager = ExpenseManager(load_expenses())


def print_menu() -> None:
    print("Welcome to the expense tracker")
    print("1. Add expense")
    print("2. View expenses")
    print("3. Delete expense")
    print("4. Edit expense")
    print("5. View expenses by ID")
    print("6. View expenses by category")
    print("7. Total expenses")
    print("8. View expenses by date")
    print("9. Exit")


def main() -> None:
    while True:
        try:
            print_menu()
            choice = get_string_input("Enter your choice: ")
            if choice == "1":
                amount = get_float_input("Enter the amount: ", 0)
                category = get_string_input("Enter the category: ")
                description = get_string_input("Enter the description: ")
                manager.add_expense(amount, category, description)
            elif choice == "2":
                manager.view_expenses()
            elif choice == "3":
                expense_id = get_string_input("Enter the expense ID to delete: ")
                confirm = get_string_input(
                    f"Are you sure you want to delete this expense? (y/n): "
                )
                if confirm.lower() != "y":
                    print("Deletion cancelled")
                    continue
                else:
                    manager.delete_expense(expense_id)
                    print("Expense deleted successfully")
            elif choice == "4":
                expense_id = get_string_input("Enter the expense ID to edit: ")
                amount = get_float_input("Enter the new amount: ", 0)
                category = get_string_input("Enter the new category: ")
                description = get_string_input("Enter the new description: ")
                manager.edit_expense(expense_id, amount, category, description)
            elif choice == "5":
                expense_id = get_string_input("Enter the expense ID to view: ")
                manager.view_expense_by_id(expense_id)
            elif choice == "6":
                category = get_string_input("Enter the category to view: ")
                manager.view_expenses_by_category(category)
            elif choice == "7":
                manager.total_expenses()
            elif choice == "8":
                date = get_string_input("Enter the date to view (YYYY-MM-DD): ")
                manager.view_expenses_by_date(date)
            elif choice == "9":
                break
            else:
                print("Invalid choice")

        except ExpenseTrackerError as e:
            print(f"Error: {e}")
            continue


if __name__ == "__main__":
    run_and_handle_error(main)
