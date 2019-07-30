from django.shortcuts import render,redirect
from  django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Question,Choice
from django.contrib.auth.models import User

def index(request):
	users=User.objects.all()
	return render(request,'quiz/login.html',{'users':users})

def register(request):
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form=UserCreationForm()

		args={'form': form}

		return render(request,'quiz/reg_form.html',args)

def quiz(request):
	question_all=Question.objects.all()

	context={'question_all':question_all}

	return render(request,'quiz/quiz.html',context)
def score(request):
	users=User.objects.all()
	return render(request,'quiz/index2.html',{'users':users})


