import uuid
from django.db import models

from task_manager.constants import COMPLETED, CREATED, IN_WORK


STATUSES = (
    (CREATED, 'Создано'),
    (IN_WORK, 'В работе'),
    (COMPLETED, 'Завершено')
)


class Task(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(verbose_name='Название', max_length=120)
    description = models.TextField()
    status = models.CharField(
        'Статус',
        # max_length=ROLE_MAX_LENGTH,
        choices=STATUSES,
        default=CREATED
    )

    def _str_(self):
        return self.title
