from django.urls import path
from . import views

urlpatterns = [
    path('login/' , views.vista_login),
]
