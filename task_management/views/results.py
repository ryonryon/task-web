from django.http import HttpResponse

def results(request, question_id):
    return HttpResponse("You're looking at the reslut of the question %s" % question_id)