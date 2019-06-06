from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from task_management.models.task_list import TaskList


class IndexView(TemplateView):
    template_name = "task_management/index.html"

    def get(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)

        task_finished_list = TaskList(True)
        task_remain_list = TaskList(False)

        context = {
            'task_list': task_finished_list.get_task_list,
            'task_finished_list': task_remain_list.get_task_list,
        }
        return HttpResponse(template.render(context, request))

