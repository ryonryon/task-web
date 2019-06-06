from .task_model import TaskModel
from .task import Task


class TaskList:

    def __init__(self, task_status):
        self.task_status = task_status
        task_model_list = TaskModel.objects.filter(is_finished=task_status).order_by('id')

        task_list = []

        for task_model in task_model_list:
            task = Task(
                task_id=task_model.id
                , user=task_model.user
                , title=task_model.title
                , detail=task_model.detail
                , publish_date=task_model.publish_date
                , is_finished=task_model.is_finished
            )

            task_list.append(task)

        self.task_list = task_list

    def get_task_list(self):
        return self.task_list

    def delete_task(self, task_id):
        task = self.get_task(task_id=task_id)

        if task in self.task_list:
            self.task_list.remove(task)

    def add_task(self):
        pass

    def update_list(self):
        pass

    def get_task(self, task_id):
        for task in self.task_list:
            if task.task_id == task_id:
                return task
