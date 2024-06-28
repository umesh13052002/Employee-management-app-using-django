from django.urls import path
from .views import *
urlpatterns = [
    path("home/",student_home),
    path("add-emp/", add_emp),
]

