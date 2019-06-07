from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from task_management.models.task_model import TaskModel
from task_management.models.task import Task


class IndexView(TemplateView):
    template_name = "task_management/index.html"

    def get(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)

        task_finished_list = []
        task_remain_list = []

        for task_model in TaskModel.objects.order_by('id'):
            if task_model.is_finished is True:
                task = Task(
                    task_id=task_model.id
                    , user=task_model.user
                    , title=task_model.title
                    , detail=task_model.detail
                    , publish_date=task_model.publish_date
                    , is_finished=task_model.is_finished
                )
                task_finished_list.append(task)
            else:
                task = Task(
                    task_id=task_model.id
                    , user=task_model.user
                    , title=task_model.title
                    , detail=task_model.detail
                    , publish_date=task_model.publish_date
                    , is_finished=task_model.is_finished
                )
                task_remain_list.append(task)

        context = {
            'task_list': task_finished_list,
            'task_finished_list': task_remain_list,
        }

        return HttpResponse(template.render(context, request))
