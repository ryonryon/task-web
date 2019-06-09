from django.db import models

import uuid

from .user_model import UserModel


class TaskStatusModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    status = models.CharField(max_length=200, unique=True)

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.status

    class Meta:
        app_label = 'task_management'
