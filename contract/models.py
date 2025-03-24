from django.db import models

from test_task.models import BaseModel


class Contract(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f'Contract {self.name}'
