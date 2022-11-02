from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect, JsonResponse
# Create your views here.
from .forms import QuestionForm
from .models import Question
from campaign.models import Campaign
import json
from django.views.decorators.csrf import csrf_exempt
import datetime



def show_homepage(request):
    form = QuestionForm()
    context = {
            "form":form,
            "last_question": request.session.get('last_login', 'have not submit a question yet')
        }
    return render(request,'homepage.html',context)

@login_required(login_url='/login/')
def submitquestion(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            print()
            new_question = Question(
                user = request.user,
                question=request.POST.get('question'),
            )
            new_question.save()
            response = serializers.serialize('json',[new_question])
            request.session['last_question'] = str(datetime.datetime.now())
            return JsonResponse(response, safe=False)
    return HttpResponseBadRequest


def getcampaignsum(request):
    if request.method == 'GET':
        data = str(Campaign.objects.count())
        return HttpResponse(data , content_type="text/plain")


def get_last_question(request):
    if request.method == 'GET':
        data = str(request.session.get('last_question', "haven't submit a question yet"))
        return HttpResponse(data , content_type="text/plain")

@login_required(login_url='/login/')
def show_json(request):
    data = Question.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
