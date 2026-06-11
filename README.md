# Expense Tracker

A command-line expense tracker built in Python. Add, view, edit, and delete expenses with persistent JSON storage and structured error handling.

## Features

- **CRUD operations** — add, view, edit, and delete expenses
- **Filtering** — view by ID, category, or date (month/year)
- **Totals** — calculate total spending across all expenses
- **Persistent storage** — expenses saved to `src/expense_tracker/data/expenses.json`
- **Input validation** — retries on invalid numeric input
- **Error handling** — custom exceptions with centralized logging

## Requirements

- Python 3.12+

## Installation

```bash
git clone <repository-url>
cd expense-tracker-app

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

## Usage

Run the interactive CLI from the project root:

```bash
PYTHONPATH=src python -m expense_tracker.main
```

### Menu options

| Option | Action |
|--------|--------|
| 1 | Add expense (amount, category, description) |
| 2 | View all expenses |
| 3 | Delete expense by ID |
| 4 | Edit expense by ID |
| 5 | View expense by ID |
| 6 | View expenses by category |
| 7 | Show total expenses |
| 8 | View expenses by date (`YYYY-MM-DD`) |
| 9 | Exit |

Press `Ctrl+C` at any time to quit.

## Project structure

```
expense-tracker-app/
├── src/expense_tracker/
│   ├── main.py              # CLI entry point and menu loop
│   ├── expense_manager.py   # Business logic
│   ├── models.py            # Expense dataclass
│   ├── storage.py           # JSON load/save
│   ├── validators.py        # User input helpers
│   ├── exceptions.py        # Custom exception types
│   ├── error_handler.py     # Global error handling
│   ├── logging_config.py    # Logging setup
│   ├── constants.py         # Data file paths
│   ├── utils.py             # Formatting helpers
│   └── data/
│       └── expenses.json    # Persisted expense data
└── tests/
    └── test_expense_manager.py
```

## Data model

Each expense is stored as:

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "amount": 42.50,
  "category": "Food",
  "description": "Lunch",
  "date": "2026-06-11T10:30:00"
}
```

- `id` — auto-generated UUID
- `date` — auto-set on creation (ISO 8601)

## Error handling

The app uses a custom exception hierarchy rooted at `ExpenseTrackerError`:

| Exception | When raised |
|-----------|-------------|
| `ExpenseNotFoundError` | Delete/view/edit with an invalid ID |
| `InvalidExpenseDataError` | Invalid expense data |
| `StorageError` | File read/write failures |

Expected errors are shown in the CLI and logged. Unexpected errors are logged with a full traceback to `expense_tracker.log`.

## Testing

```bash
.venv/bin/pytest
```

Run with verbose output:

```bash
.venv/bin/pytest -v
```

## Development

Format and lint with the tools in `requirements.txt`:

```bash
.venv/bin/black src tests
.venv/bin/ruff check src tests
.venv/bin/ruff format src tests
.venv/bin/mypy src
```

## Logging

Logs are written to `expense_tracker.log` in the working directory when `logging_config` is active. Unexpected errors include stack traces via `logger.exception()`.
