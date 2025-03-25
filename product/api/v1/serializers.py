from rest_framework import serializers

from product.models import Product


class BaseProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name',)


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'manufacturer', 'credit_request',)
