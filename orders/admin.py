from typing import TYPE_CHECKING
from django.contrib import admin

from .models import Order

if TYPE_CHECKING:
    admin.site: admin.AdminSite


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name_plural = "Сотрудники"

    list_display = "pk", "name",
    list_display_links = "name",
    ordering = "name", "pk"
