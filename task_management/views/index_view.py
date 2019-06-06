from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from ..models.task import Task


class IndexView(TemplateView):
    template_name = "task_management/index.html"

    def get(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)
        context = {
            'task_list': Task.objects.order_by('id'),
        }
        return HttpResponse(template.render(context, request))


