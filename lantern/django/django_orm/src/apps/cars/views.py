from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from apps.cars.models import Car


class CarList(ListView):
    model = Car

