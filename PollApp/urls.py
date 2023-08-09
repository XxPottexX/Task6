from django.urls import path, include
from django.contrib import admin
from . import views
# add views to urls, so they can map to some path 

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("poll/<int:poll_id>/", views.PollView.as_view(), name="poll"),
]