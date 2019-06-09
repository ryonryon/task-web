from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from task_management.models.task_model import TaskModel
from task_management.models.task_status import TaskStatus
from task_management.models.task_status_model import TaskStatusModel
from task_management.models.task import Task


class IndexView(TemplateView):
    template_name = "task_management/index.html"

    def get(self, request, *args, **kwargs):

        template = loader.get_template(self.template_name)

        context = self.get_status_lists()

        return HttpResponse(template.render(context, request))

    def get_status_lists(self):

        task_status_list = []

        task_dict = {'task_status_list': task_status_list}

        for task_status_model in TaskStatusModel.objects.order_by('id'):

            task_status = TaskStatus(task_status_model.id, task_status_model.status)

            task_status_list.append(task_status)

        for task_model in TaskModel.objects.order_by('id'):

            task = Task(
                task_id=task_model.id
                , status=task_model.status
                , title=task_model.title
                , detail=task_model.detail
                , publish_date=task_model.publish_date
            )

            for status in task_status_list:
                if task.status.id == status.status_id:
                    status.set_task(task)

        return task_dict

