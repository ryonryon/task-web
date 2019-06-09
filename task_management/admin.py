from django.contrib import admin

from .models import TaskModel
from .models import TaskStatusModel
from .models import UserModel

admin.site.register(TaskModel)
admin.site.register(TaskStatusModel)
admin.site.register(UserModel)
