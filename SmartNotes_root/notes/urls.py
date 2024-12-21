from tkinter.font import names

from . import views

from django.contrib import admin
from django.urls import path


urlpatterns = [
    path("notes/", views.NotesListView.as_view(), name = "notes.list"),
    path("notes/<int:pk>", views.NotesDetailView.as_view(), name = "notes.detail"),
    path("notes/new", views.NotesCreateView.as_view(), name = "notes.new"),
    path("notes/<int:pk>/edit", views.NotesUpdateView.as_view(), name = "notes.update"),
    path("notes/<int:pk>/delete", views.NotesDeleteView.as_view(), name = "notes.delete"),
]

