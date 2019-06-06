from django.db import models


class User(models.Model):

    user_name = models.CharField(max_length=200)

    email = models.EmailField()

    def __str__(self):
        return self.user_name

    class Meta:
        app_label = 'task_management'
