from .task_model import TaskModel
from .task import Task


class TaskList:

    def __init__(self, task_status):
        self.task_status = task_status
        task_model_list = TaskModel.objects.filter(is_finished=task_status).order_by('id')

        task_list = []

        for task_model in task_model_list:
            task = Task(
                task_model.id
                , task_model.user
                , task_model.title
                , task_model.detail
                , task_model.publish_date
                , task_model.is_finished
            )

            task_list.append(task)

        self.task_list = task_list

    def get_task_list(self):
        return self.task_list

    def delete_task(self):
        pass

    def add_task(self):
        pass

    def update_list(self):
        pass
