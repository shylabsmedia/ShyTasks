from datetime import datetime

class Task:
    """Represents something the user wants to accomplish."""

    def __init__(
        self,
        task_id: int,
        title: str,
        description: str,
        priority: str,
        category: str,
        due_date: str,
    ):
        self.id = task_id
        self.title = title
        self.description = description
        self.priority = priority
        self.category = category
        self.status = "To Do"

        self.due_date = due_date

        self.created_at = datetime.now()
        self.started_at = None
        self.completed_at = None

    def to_dict(self):
        """Convert the task to a dictionary for JSON serialization."""

        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "category": self.category,
            "status": self.status,
            "due_date": self.due_date,
            "created_at": self.created_at.isoformat(),
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Task object from a dictionary."""

        task = cls(
            task_id=data["id"],
            title=data["title"],
            description=data["description"],
            priority=data["priority"],
            category=data["category"],
            due_date=data["due_date"],
        )

        task.status = data["status"]
        task.created_at = datetime.fromisoformat(data["created_at"])
        task.started_at = datetime.fromisoformat(data["started_at"]) if data["started_at"] else None
        task.completed_at = datetime.fromisoformat(data["completed_at"]) if data["completed_at"] else None

        return task