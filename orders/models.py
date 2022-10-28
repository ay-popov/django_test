from django.db import models


class Order(models.Model):
    name = models.CharField(max_length=64, null=False)
    worker = models.ManyToManyField("employees.employee", related_name="orders")
