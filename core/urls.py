from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('sign-up/', UserCreate.as_view()),
    path('login/', Login.as_view()),
]
