from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from contract.api.v1.serializers import ContractSerializer
from contract.api.v1.services import ContractService
from contract.models import Contract
from manufacturer.api.v1.serializers import BaseManufacturerSerializer


class ContractViewSet(viewsets.ModelViewSet):
    """CRUD operations for Contract"""
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    http_method_names = ('get', 'post', 'put', 'delete',)

    @action(detail=True, methods=['get'], url_path='unique-manufacturers')
    def get_unique_contract_manufacturers(self, request: Request, pk: int) -> Response:
        """Returns unique manufacturers for contract"""
        contract = self.get_object()
        unique_manufacturers = ContractService.get_unique_contract_manufacturers(contract=contract)
        response_data = BaseManufacturerSerializer(unique_manufacturers, many=True).data
        return Response({'unique_manufacturers': response_data}, status=status.HTTP_200_OK)
