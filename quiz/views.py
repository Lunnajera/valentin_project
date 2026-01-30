from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import QuizForm


def quiz_view(request):
    if request.method == "POST":
        form = QuizForm(request.POST)
        if form.is_valid():
            score = 0

            correct_answers = {
                "q1": "3",
                "q2": "2",
                "q3": "2",
                "q4": "1",
                "q5": "1",
                "q6": "3",
                "q7": "1",
                "q8": "3",
                "q9": "2",
                "q10": "3",               
            }

            for question, correct in correct_answers.items():
                if form.cleaned_data[question] == correct:
                    score += 1

            if score >= 7:
                return render(request, "quiz/valentine.html", {"score": score})
            

            return render(request, "quiz/fail.html", {"score": score})

    else:
        form = QuizForm()

    return render(request, "quiz/quiz.html", {"form": form})


def valentine_view(request):
    return render(request, "quiz/valentine.html")


def accept_view(request):
    return render(request, "quiz/accepted.html")
