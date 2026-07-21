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