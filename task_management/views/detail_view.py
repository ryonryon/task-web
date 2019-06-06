from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView


class DetailView(TemplateView):
    template_name = "task_management/detail.html"

    def get(self, request, *args, **kwargs):

        task_title = kwargs['title']

        template = loader.get_template(self.template_name)
        context = {
            'task_title': task_title,
        }
        return HttpResponse(template.render(context, request))

