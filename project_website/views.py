from django.shortcuts import render, redirect
from . import brainrot

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

def loading(request):
    return render(request, "loading.html")

def audio_lesson(request):
    
    if request.method == "POST":
        textInput = dict(request.POST)
        
        print("Just sent POST request")
        
        brainrot.create_video(textInput["inputText"][0], "/Users/daniel/Documents/coding_stuff/novaSpy/project_website/static/subway.mp4", "/Users/daniel/Documents/coding_stuff/novaSpy/project_website/static/output.mp4")
        
        return redirect("/static/output.mp4")
    
    return render(request, "audioLesson.html")