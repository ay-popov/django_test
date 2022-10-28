from typing import TYPE_CHECKING
from django.contrib import admin

from .models import Employee, JobTitles

if TYPE_CHECKING:
    admin.site: admin.AdminSite


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name_plural = "Сотрудники"

    list_display = "pk", "surname", "firstname", "patronymic", "personnel_number", "email", "archived"
    list_display_links = "surname",
    ordering = "surname", "pk"


@admin.register(JobTitles)
class JobTitlesAdmin(admin.ModelAdmin):

    list_display = "pk", "name",
    list_display_links = "name",
    ordering = "name", "pk"
