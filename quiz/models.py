from django.db import models

# Create your models here.

class Question(models.Model):
	question_text=models.CharField(max_length=500)

	def __str__(self):
		return self.question_text
class Choice(models.Model):
	question=models.ForeignKey(Question, on_delete=models.CASCADE)
	choice1=models.CharField(max_length=200)
	choice2=models.CharField(max_length=200)
	choice3=models.CharField(max_length=200)
	choice4=models.CharField(max_length=200)
	correct_ans=models.CharField(max_length=200)
	user_ans=models.CharField(max_length=200)

	def __str__(self):
		return self.correct_ans


