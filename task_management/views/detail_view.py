from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from ..models.question import Question


class DetailView(TemplateView):
    template_name = "task_management/detail.html"

    def get(self, request, *args, **kwargs):
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        template = loader.get_template('task_management/index.html')
        context = {
            'latest_question_list': latest_question_list,
        }
        return HttpResponse(template.render(context, request))

