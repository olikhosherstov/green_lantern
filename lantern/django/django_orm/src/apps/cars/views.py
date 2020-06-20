from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from apps.cars.models import Car


class CarListView(ListView):
    model = Car
    queryset = Car.objects.all().order_by('-dealer')
    template_name = 'cars/cars_list.html'

    def get_queryset(self):
        if self.kwargs.get('pk'):
            return super().get_queryset().filter(dealer__id=self.kwargs.get('pk'))
        else:
            return super().get_queryset().all()
