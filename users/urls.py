from django.urls import path
from .views import Usersignupview

urlpatterns = [
    path("singup/", Usersignupview.as_view(), name="singup"),
]
