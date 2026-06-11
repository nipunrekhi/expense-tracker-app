from dataclasses import dataclass, field
from datetime import datetime
import uuid


@dataclass
class Expense:
    amount: float
    category: str
    description: str

    id: uuid.UUID = field(default_factory=uuid.uuid4)
    date: datetime = field(default_factory=datetime.now)

    def to_dict(self) -> dict:
        return {
            "id": str(self.id),
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date.isoformat(),
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Expense":
        return cls(
            amount=data["amount"],
            category=data["category"],
            description=data["description"],
            id=uuid.UUID(data["id"]),
            date=datetime.fromisoformat(data["date"]),
        )
