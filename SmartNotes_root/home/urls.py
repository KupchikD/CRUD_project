from tkinter.font import names

from . import views

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path("", views.HomeView.as_view(), name = "homepage"),
    path("login", views.LoginInterfaceView.as_view(), name = "login"),
    path("logout", views.LogoutInterfaceView.as_view(), name = "logout"),
    path("signup", views.SignupView.as_view(), name = "signup"),
]
