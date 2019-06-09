from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from task_management.models.task_model import TaskModel
from task_management.models.task_status import TaskStatus
from task_management.models.task import Task


class IndexView(TemplateView):
    template_name = "task_management/index.html"

    def get(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)

        context = self.get_status_lists(TaskModel.objects.order_by('id'))

        return HttpResponse(template.render(context, request))

    def get_status_lists(self, task_list):

        task_state = TaskStatus.objects.all()

        task_dict = {'task_status_list': task_state}

        for task_status in TaskStatus.objects.order_by('id'):

            task_status_list = []

            for task_model in task_list:

                if task_status.status == task_model.status:

                    task_status_list.append(Task(
                        task_id=task_model.id
                        , user=task_model.user
                        , title=task_model.title
                        , detail=task_model.detail
                        , publish_date=task_model.publish_date
                        , status=task_model.status
                    ))
            task_dict[task_status] = task_status_list

        return task_dict

