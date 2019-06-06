from django.contrib import admin

from .models import TaskModel
from .models import UserModel

admin.site.register(TaskModel)
admin.site.register(UserModel)
