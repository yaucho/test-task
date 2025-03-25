from django.db import models

from test_task.models import BaseModel


class Product(BaseModel):
    name = models.CharField(max_length=255)

    manufacturer = models.ForeignKey(
        'manufacturer.Manufacturer', 
        on_delete=models.CASCADE,
        related_name='products',
    )
    credit_request = models.ForeignKey(
        'credit_request.CreditRequest',
        on_delete=models.SET_NULL,
        related_name='products',
        null=True,
    )

    def __str__(self) -> str:
        return f'Product {self.name}'
