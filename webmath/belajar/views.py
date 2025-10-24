from django.shortcuts import render

def index(request):
    return render(request, 'belajar/index.html')

def materi(request):
    return render(request, 'belajar/materi.html')

def eksperimen(request):
    return render(request, 'belajar/desmos.html')

def quiz(request):
    return render(request, 'belajar/quiz.html')
