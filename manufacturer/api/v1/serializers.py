from rest_framework import serializers

from manufacturer.models import Manufacturer
from product.api.v1.serializers import BaseProductSerializer


class BaseManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = ('id', 'name',)


class ManufacturerSerializer(serializers.ModelSerializer):
    products = BaseProductSerializer(many=True)

    class Meta:
        model = Manufacturer
        fields = ('id', 'name', 'products',)


class CreateOrUpdateManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = ('id', 'name',)
