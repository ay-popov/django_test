from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, HttpResponse, get_object_or_404
from django.urls import reverse_lazy, reverse

from .models import Employee, JobTitles
from .forms import AnimalCreateForm
from django.views.generic import ListView, DetailView, DeleteView, CreateView


class EmployeesListView(ListView):

    template_name = "employees/index.html"
    context_object_name = "employees"

    queryset = (
        Employee.objects
        .select_related("job")
        .filter(archived=False)
        .order_by('pk').all()
        )


class EmployeeDetailView(DetailView):
    template_name = "employees/details.html"
    context_object_name = "employee"
    queryset = (Employee.objects.select_related("job"))


class EmployeeDeleteView(DeleteView):
    model = Employee
    success_url = reverse_lazy("employees:index")
    context_object_name = "employee"

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class EmployeeCreateView(CreateView):
    # model = Employee
    # fields = ["surname", "firstname", "patronymic", "personnel_number", "email", "job"]
    # success_url = reverse_lazy("employees:index")

    model = Employee
    form_class = AnimalCreateForm

    def get_success_url(self):
        return reverse("employees:details", kwargs={"pk": self.object.pk})