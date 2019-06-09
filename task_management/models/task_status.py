class TaskStatus:
    def __init__(self, status_id, status_name, tasks):
        self.status_id = status_id
        self.status_name = status_name
        self.tasks = []

    def set_tasks(self, task):
        self.tasks.append(task)
