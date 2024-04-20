from django.db import models


class Status(models.Model):
    status_name = models.CharField(
        verbose_name="имя статуса",
        null=False,
        max_length=64,
    )

    class Meta:
        verbose_name = "статус"
        verbose_name_plural = "статусы"

    def __str__(self):
        return f"{self.status_name}"


class Task(models.Model):
    title = models.CharField(
        verbose_name="заголовок",
        null=False,
        validators=[],
        max_length=64
    )
    text = models.TextField(
        verbose_name="описание",
        default="отсутствует",
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        verbose_name="статус",
        related_name="statuses",
        related_query_name="status",
    )
    created_at = models.DateTimeField(
        verbose_name="время",
        auto_now_add=True,
        null=True,
    )

    class Meta:
        verbose_name = "задание"
        verbose_name_plural = "задания"

    def __str__(self):
        return f"{self.title} is {self.status}"
