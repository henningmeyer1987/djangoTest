from django.http import HttpResponse
from polls.models import Question


def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	output = ','.join([p.question_text for p in latest_question_list])
	return HttpResponse(output)


def detail(request, question_id):
	return HttpResponse("Youre looking at question %s." % question_id)


def results(request, question_id):
	response = "Youre looking at the results of Question %s."
	return HttpResponse(response % question_id)


def vote(request, question_id):
	return HttpResponse("Youre voting on question %s." % question_id)
