from django.db import models

import uuid

from task_management.models.task_status_model import TaskStatusModel


class TaskModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    status = models.ForeignKey(TaskStatusModel, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    detail = models.CharField(max_length=800)

    publish_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'task_management'
