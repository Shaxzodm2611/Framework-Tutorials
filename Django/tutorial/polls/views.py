from django.shortcuts import render
from django.http import HttpResponse, request


from .models import Question
def index(request):
    latest_q_list = Question.objects.order_by("-pub_date")[:5]
    context = {
        "latest_question_list": latest_q_list
    }
    return render(request, "polls/index.html", context)

def details(request, question_id):
    return HttpResponse("You're looking at question: %s." % question_id)
# Create your views here.

def results(request, question_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
