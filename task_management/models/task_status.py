from django.db import models

import uuid


class TaskStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    status = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.status

    class Meta:
        app_label = 'task_management'
