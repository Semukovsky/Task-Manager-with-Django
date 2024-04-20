import django.forms

from .models import Task

__all__ = []


class TaskForm(django.forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs["class"] = "form-control"

    class Meta:
        model = Task
        verbose_name = "Задача"

        fields = (Task.title.field.name, Task.text.field.name, Task.status.field.name)

        labels = {
            Task.title.field.name: "Заголовок задачи",
            Task.text.field.name: "Описание задачи",
            Task.status.field.name: "Статус задачи",
        }

        exclude = ("created_at",)
