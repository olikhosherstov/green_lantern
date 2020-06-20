from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.orders.models import Order


class OrderCreateView(CreateView):
    model = Order
    fields = '__all__'
    template_name = 'orders/create_order.html'
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        form.save()
        return super(OrderCreateView, self).form_valid(form)
