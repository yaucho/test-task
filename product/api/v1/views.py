from rest_framework import viewsets

from product.api.v1.serializers import ProductSerializer
from product.models import Product


class ProductViewSet(viewsets.ModelViewSet):
    """CRUD operations for Product"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ('get', 'post', 'put', 'delete',)
