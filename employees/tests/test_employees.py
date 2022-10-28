from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse, reverse_lazy

from employees.models import Employee


class AnimalsListTestCase(TestCase):

    fixtures = [
        "employee_jobtitles.fixture.json",
        "employee.fixture.json",
    ]

    url = reverse_lazy("employees:index")

    def test_list_employees(self):
        url = reverse("employees:index")
        response = self.client.get(url)

        employees = (
            Employee.objects
            .select_related("job")
            .filter(archived=False)
            .order_by('pk').all()
        )

        employees_in_context = response.context["employees"]

        print()
        print("Testing: compare count employees in context and in queryset...")
        self.assertEqual(len(employees), len(employees_in_context))

        print()
        print("Testing: compare data employees in context and in queryset...")
        for a1, a2 in zip(employees, employees_in_context):
            self.assertEqual(a1.pk, a2.pk)