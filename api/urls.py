from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('answers/', views.getQuestionAnswer, name="answers"),
    path('allquestion/', views.getAllQuestion, name="allQuestion"), 
    path('question/<int:pk>/', views.getQuestion, name="question"),  
]
