from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.views.generic  import TemplateView
from django.shortcuts import redirect
from django.contrib.auth import logout

# Create your views here.
class HomeView(TemplateView):
    template_name = "home/homepage.html"
    extra_context = {"today":datetime.today()}


class LoginInterfaceView(LoginView):
    template_name = "home/login.html"
    success_url = 'smart/notes'


class LogoutInterfaceView(LogoutView):
    template_name = "home/logout.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        logout(request)  # Убедитесь, что это выполняется
        return self.render_to_response(self.get_context_data())

class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = "/login"
    template_name = "home/registr.html"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("notes.list")
        return super().get(request, *args, **kwargs)