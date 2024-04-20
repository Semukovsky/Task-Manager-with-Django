from django.urls import path
from .views import tasks, detail, new_task, change_status

app_name = "tasks"

urlpatterns = [
    path("", tasks, name="tasks"),
    path("details/<int:id>/", detail, name="detail"),
    path("new_task/", new_task, name="new_task"),
    path("change_status/<int:id_task>/<int:id_status>/", change_status, name="change_status")
]

