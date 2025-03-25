from rest_framework import viewsets

from manufacturer.api.v1.serializers import (
    CreateOrUpdateManufacturerSerializer, 
    ManufacturerSerializer,
)
from manufacturer.models import Manufacturer


class ManufacturerViewSet(viewsets.ModelViewSet):
    """CRUD operations for Manufacturer"""
    queryset = Manufacturer.objects.prefetch_related('products')
    serializer_class = ManufacturerSerializer
    http_method_names = ('get', 'post', 'put', 'delete',)

    def get_serializer_class(self, *args, **kwargs):
        match self.action:
            case 'create' | 'update':
                return CreateOrUpdateManufacturerSerializer
            case _:
                return self.serializer_class
