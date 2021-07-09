from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


month_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day",
    "march": "Walk for at least 20 minutes every day",
    "april": "Walk for at least 30 minutes every day",
    "may": "Walk for at least 40 minutes every day",
    "june": "Walk for at least 50 minutes every day",
    "july": "Walk for at least 60 minutes every day",
    "august": "Walk for at least 70 minutes every day",
    "september": "Walk for at least 80 minutes every day",
    "october": "Walk for at least 90 minutes every day",
    "november": "Walk for at least 100 minutes every day",
    "december": None
}


def index(request):
    months = list(month_challenges.keys())
    return render(request, "challenges/index.html", {'months': months})


def monthly_challenge(request, month):
    try:
        challenge_text = month_challenges[month]
        return render(request, "challenges/challenge.html", {'data': challenge_text, 'title': month})
    except:
        return HttpResponseNotFound("This month is not supported")


def monthly_challenge_by_number(request, month):
    months = list(month_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound('This month is not supported')
    else:
        forward_month = months[month-1]
        redirect_path = reverse("month-challenge", args=[forward_month])
        return HttpResponseRedirect(redirect_path)
