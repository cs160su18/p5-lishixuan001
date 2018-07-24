from django.shortcuts import render
from django.core import serializers
from django.utils import timezone
from life.models import *

question_text = ""
question_description = ""
userList = User.objects.all()
user_self = None
if len(userList) > 0:
  user_self = userList[0]

def index(request):
    return render(request, 'life/index.html')
  
def forum(request):
  if request.method == 'POST':
    if user_self != None:
      Question.objects.create(question=question_text, description=question_description,
                              creation_date=timezone.now(), user = user_self, last_modified=timezone.now())
  else:
    pass
  return render(request, 'life/forum.html')

def forum_create(request):
    if request.method == 'POST':
        question_text = request.POST['question-text'].strip()
        question_description = request.POST['question-description'].strip()
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