from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy



# Create your views here.


class Usersignupview(CreateView):
    template_name = "users/singup.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("starting-page")