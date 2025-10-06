from django.urls import path
from . import views

urlpatterns = [
    path('', views.power_calculator, name='power_calculator'),
]
