from django.db import models

from test_task.models import BaseModel


class CreditRequest(BaseModel):
    name = models.CharField(max_length=255)

    contract = models.ForeignKey(
        'contract.Contract',
        on_delete=models.SET_NULL,
        related_name='credit_requests',
        null=True,
    )

    def __str__(self) -> str:
        return f'Credit Request {self.name}'
