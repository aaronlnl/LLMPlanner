from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("calendar", views.cal, name = "calendar"),
    path("chat", views.chat, name = "chat"),
]