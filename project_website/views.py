from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "index.html")

def query(request):
    return render(request, "query.html")

def interactive(request):
    return render(request, "interactiveQuiz.html")

def flashcards(request):
    return render(request, "flashcards.html")

def review_exam(request):
    return render(request, "reviewExam.html")

def audio_lesson(request):
    return render(request, "audioLesson.html")