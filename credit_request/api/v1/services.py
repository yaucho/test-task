from rest_framework.serializers import ValidationError

from credit_request.models import CreditRequest
from product.models import Product


class CreditRequestService:

    @classmethod
    def update_credit_request(cls, credit_request: CreditRequest, data: dict) -> CreditRequest:
        """Checks that products can be attached to credit request and updates it"""
        products = data.pop('products')
        if invalid_product_ids := cls._get_invalid_products(credit_request=credit_request, products=products):
            raise ValidationError(
                detail={
                    'field': 'products', 
                    'errors': (
                        f'Product id(s)={",".join([str(product_id) for product_id in invalid_product_ids])} '
                        f'already attached to another request(s).'
                    )
                }
            )
        for key, value in data.items():
            setattr(credit_request, key, value)
        credit_request.products.set(products)
        credit_request.save()
        return credit_request

    @staticmethod
    def _get_invalid_products(credit_request: CreditRequest, products: list[Product]) -> list[int]:
        """
        Returns list of products ids that are already attached to another credit request
        """
        return [
            product.id for product in products 
            if product.credit_request is not None and product.credit_request != credit_request
        ]
