# Generated by Django 4.1.2 on 2022-10-24 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_employee_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]