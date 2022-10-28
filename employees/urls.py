from django.contrib import admin
from django.urls import path
from .views import EmployeesListView, EmployeeDetailView, EmployeeDeleteView, EmployeeCreateView


app_name = "employees"

urlpatterns = [

    path("", EmployeesListView.as_view(), name="index"),

    path("<int:pk>", EmployeeDetailView.as_view(), name="details"),

    path("<int:pk>/confirm-delete", EmployeeDeleteView.as_view(), name="delete-employee"),

    path("create/", EmployeeCreateView.as_view(), name="create-employee"),
]