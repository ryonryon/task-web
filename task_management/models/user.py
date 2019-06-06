from django.db import models

import uuid


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user_name = models.CharField(max_length=200)

    email = models.EmailField()

    def __str__(self):
        return self.user_name

    class Meta:
        app_label = 'task_management'
