from django.shortcuts import render
from django.core import serializers
from django.utils import timezone
from django.http import HttpResponseRedirect
from life.models import *

# question_text = ""
# question_description = ""
# userList = User.objects.all()
# user_self = None
# if len(userList) > 0:
#     user_self = userList[0]

# Default User -> Anonymous (id=5)
currentUser = User.objects.get(id=5)

def index(request):
    return render(request, 'life/index.html')
  
def forum(request):
    question_list = Question.objects.all()
    context = {
        'question_list': question_list
    }
    return render(request, 'life/forum.html', context)

def forum_create(request):
    if request.method == 'POST':
        question_text = request.POST['question'].strip()
        question_description = request.POST['description'].strip()
        Question.objects.create(user=currentUser, question=question_text, description=question_description)
        return HttpResponseRedirect('/life/forum/')
    else:
        pass
    return render(request, 'life/forum_create.html')

def reminder(request):
	return render(request, 'life/reminder.html')

def tracker(request):
	return render(request, 'life/tracker.html')

def case(request):
	return render(request, 'life/case.html')

def case_create(request):
	return render(request, 'life/case_create.html')

def tracker(request):
	return render(request, 'life/tracker.html')






































# END