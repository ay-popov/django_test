from django.http import HttpRequest
from django.shortcuts import render
from .models import Order
from django.views.generic import ListView, DetailView


class OrdersListView(ListView):

    template_name = "orders/index.html"
    context_object_name = "orders"

    queryset = (
        Order.objects
            #.select_related("job")
            .prefetch_related("worker")
            .order_by('pk').all()
        )