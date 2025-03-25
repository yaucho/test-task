from rest_framework import serializers

from contract.api.v1.serializers import ContractSerializer
from credit_request.models import CreditRequest
from product.api.v1.serializers import BaseProductSerializer
from product.models import Product


class CreditRequestSerializer(serializers.ModelSerializer):
    products = BaseProductSerializer(many=True)
    contract = ContractSerializer()

    class Meta:
        model = CreditRequest
        fields = ('id', 'name', 'products', 'contract',)


class CreateOrUpdateCreditRequestSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.prefetch_related('credit_request'), many=True
    )

    class Meta:
        model = CreditRequest
        fields = ('id', 'name', 'products', 'contract',)
