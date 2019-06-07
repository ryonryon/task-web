from django.contrib import admin

from .models import TaskModel
from .models import TaskStatus
from .models import UserModel

admin.site.register(TaskModel)
admin.site.register(TaskStatus)
admin.site.register(UserModel)
