import json
import logging
from .constants import DATA_FILE
from .models import Expense

logger = logging.getLogger(__name__)


def save_expenses(expenses: list[Expense]) -> None:
    try:
        with open(DATA_FILE, "w") as f:
            json.dump([expense.to_dict() for expense in expenses], f, indent=4)
    except Exception as e:
        logger.error(f"Error saving expenses: {e}")
        raise e


def load_expenses() -> list[Expense]:
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            return [Expense.from_dict(item) for item in data]
    except Exception as e:
        logger.error(f"Error loading expenses: {e}")
        return []
