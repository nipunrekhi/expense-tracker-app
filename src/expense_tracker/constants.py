from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
DATA_FILE = DATA_DIR / "expenses.json"
DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
