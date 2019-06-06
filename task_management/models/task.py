from django.db import models


class Task(models.Model):

    title = models.CharField(max_length=200)

    detail = models.CharField(max_length=800)

    publish_date = models.DateTimeField('date published')

    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        app_label = 'task_management'
