from django.shortcuts import render,redirect
from  django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import Question,Choice
def index(request):
	return render(request,'quiz/login.html')

def register(request):
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/register')
	else:
		form=UserCreationForm()

		args={'form': form}

		return render(request,'quiz/reg_form.html',args)

def quiz(request):
	question_all=Question.objects.all()

	context={'question_all':question_all}

	return render(request,'quiz/quiz.html',context)

