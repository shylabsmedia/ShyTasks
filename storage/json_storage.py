from pathlib import Path
from models.task import Task
import json

class JSONStorage:
    """Handles saving and loading tasks to and from a JSON file."""

    BASE_DIR = Path(__file__).resolve().parent.parent
    FILE_PATH = BASE_DIR / "data" / "tasks.json"

    def save_tasks(self, tasks):
        """Save tasks to a JSON file."""

        data = []

        for task in tasks:
            data.append(task.to_dict())

        with open(self.FILE_PATH, "w") as file:
            json.dump(data, file, indent=4)

    def load_tasks(self):
        """Load tasks from a JSON file."""

        if not self.FILE_PATH.exists():
            return []

        with open(self.FILE_PATH, "r") as file:
            data = json.load(file)

        tasks = []
        for task_data in data:
            task = Task.from_dict(task_data)
            tasks.append(task)

        return tasks