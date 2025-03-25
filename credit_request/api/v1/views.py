from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.request import Request

from credit_request.api.v1.serializers import (
    CreateOrUpdateCreditRequestSerializer, 
    CreditRequestSerializer,
)
from credit_request.api.v1.services import CreditRequestService
from credit_request.models import CreditRequest


class CreditRequestViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for Credit Request.
    When create allow to add products that are not in any contract.
    When update allow to add products that are not in any contract or already in current contract.
    """
    queryset = (
        CreditRequest.objects
        .select_related('contract')
        .prefetch_related('products')
    )
    serializer_class = CreditRequestSerializer
    http_method_names = ('get', 'post', 'put', 'delete',)

    def get_serializer_class(self):
        match self.action:
            case 'create' | 'update':
                return CreateOrUpdateCreditRequestSerializer
            case _:
                return self.serializer_class
    
    def update(self, request: Request, *args, **kwargs):
        credit_request = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        updated_credit_request = CreditRequestService.update_credit_request(
            credit_request=credit_request, data=serializer.validated_data
        )
        response_data = self.serializer_class(updated_credit_request).data
        return Response(data=response_data, status=status.HTTP_200_OK)
