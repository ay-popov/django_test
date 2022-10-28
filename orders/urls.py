from django.contrib import admin
from django.urls import path
from .views import OrdersListView

app_name = "orders"

urlpatterns = [
    path("", OrdersListView.as_view(), name="index"),
]