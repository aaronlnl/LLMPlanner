from django.http import HttpResponse
from django.shortcuts import render
from .models import User, CalendarEvent

import calendar
import datetime


# Create your views here.
def index(request):
    return render(request, "planner/index.html")

def cal(request):
    today = datetime.date.today()
    dates = [ (today + datetime.timedelta(i)) for i in range(-1 - today.weekday(), 6 - today.weekday())]

    schedule = [CalendarEvent.objects.filter(start_date=date).order_by('start_time') for date in dates]

    return render(request, "planner/calendar.html", {
        "dates": dates,
        "schedule": schedule
    })

def chat(request):
    return render(request, "planner/chat.html")