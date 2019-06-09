class TaskStatus:
    def __init__(self, status_id, status_name):
        self.status_id = status_id
        self.status_name = status_name
        self.tasks = []

    def set_task(self, task):
        self.tasks.append(task)
