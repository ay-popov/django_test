from django.forms import ModelForm, CharField
from django.forms.widgets import Widget
from .models import Employee


class AnimalCreateForm(ModelForm):
    class Meta:
        model = Employee
        fields = "surname", "firstname", "patronymic", "personnel_number", "email", "job"

    surname = CharField(max_length=40, label="Фамилия")
    firstname = CharField(max_length=40, label="Имя")
    patronymic = CharField(max_length=40, label="Отчество")
    personnel_number = CharField(max_length=8, label="Табельный номер")
    email = CharField(max_length=40, label="Email")
    # job = CharField(max_length=40, label="Должность")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            # print(name, field, field.widget)
            widget: Widget = field.widget
            widget.attrs["class"] = "form-control"