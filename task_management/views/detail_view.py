from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView


class DetailView(TemplateView):
    template_name = "task_management/detail.html"

    def get(self, request, *args, **kwargs):

        question = kwargs['question_id']

        template = loader.get_template(self.template_name)
        context = {
            'question_id': question,
        }
        return HttpResponse(template.render(context, request))

