from models.task import Task
from storage.json_storage import JSONStorage

class TaskManager:
    """Manages all tasks."""

    def __init__(self):
        self.storage = JSONStorage()
        self.tasks = self.storage.load_tasks()

        self.next_id = max(
            (task.id for task in self.tasks), 
            default=0
        ) + 1

    def add_task(
            self, 
            title: str, 
            description: str, 
            priority: str, 
            category: str, 
            due_date: str):
        """Creates a Task object and adds it to the manager."""

        task = Task(
            self.next_id, 
            title, 
            description, 
            priority, 
            category, 
            due_date
        )
        
        self.tasks.append(task)
        self.next_id += 1

        self.storage.save_tasks(self.tasks)

        return task
    
    def view_tasks(self):
        """Returns a list of all tasks."""

        return self.tasks
    
    def delete_task(self, task_id: int):
        """Deletes a task by its ID."""

        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)

                self.storage.save_tasks(self.tasks)

                return task
        
        return None