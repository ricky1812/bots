

from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('quiz/',views.quiz,name='quiz'),
    path('score/',views.score,name='quiz'),
    ]