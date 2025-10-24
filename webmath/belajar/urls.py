from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('materi/', views.materi, name='materi'),
    path('eksperimen/', views.eksperimen, name='eksperimen'),
    path('quiz/', views.quiz, name='quiz'),
]
