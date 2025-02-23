
from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home),
    path("query/", views.query),
    path("interactive/", views.interactive),
    path("flashcards/", views.flashcards),
    path("review-exam/", views.review_exam),
    path("audioLesson/", views.audio_lesson),
    path("loading/", views.loading),
]