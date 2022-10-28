from django.db import models


class JobTitles(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Employee(models.Model):
    surname = models.CharField(max_length=64, null=False)
    firstname = models.CharField(max_length=64, null=False)
    patronymic = models.CharField(max_length=64, null=False)
    personnel_number = models.CharField(max_length=64, unique=True, null=False)
    email = models.CharField(max_length=64, null=False)
    job = models.ForeignKey(JobTitles, on_delete=models.PROTECT, related_name="employee")
    archived = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.surname} {self.firstname} ({self.job})"



