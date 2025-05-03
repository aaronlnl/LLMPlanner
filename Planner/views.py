from django.http import HttpResponse
from django.shortcuts import render

import calendar
import datetime

from . import utilities


# Create your views here.
def index(request):
    return render(request, "planner/index.html")

def cal(request):
    today = datetime.date.today()
    dates = [ (today + datetime.timedelta(i)) for i in range(-1 - today.weekday(), 6 - today.weekday())]    
    schedule = [
        utilities.ScheduleEvent("abc", 1, datetime.datetime(2025, 5, 3, 12, 00), datetime.datetime(2025, 5, 3, 13, 00), "HKUST", "Test event 1"),
        utilities.ScheduleEvent("abc", 1, datetime.datetime(2025, 5, 3, 13, 00), datetime.datetime(2025, 5, 3, 14, 00), "HKUST", "Test event 2"),
        utilities.ScheduleEvent("abc", 1, datetime.datetime(2025, 5, 3, 18, 00), datetime.datetime(2025, 5, 3, 20, 00), "HKUST", "Test event 3"),
    ]

    schedule_response = [[] for i in range(7)]

    for event in schedule:
        if event.get_start_time().date() in dates:
            schedule_response[(event.get_start_time().weekday() + 1) % 7].append(event)

    return render(request, "planner/calendar.html", {
        "dates": dates,
        "schedule": schedule_response
    })

def chat(request):
    return render(request, "planner/chat.html")