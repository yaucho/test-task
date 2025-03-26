from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from contract.api.v1.serializers import ContractSerializer
from contract.api.v1.services import ContractService
from contract.models import Contract


class ContractViewSet(viewsets.ModelViewSet):
    """CRUD operations for Contract"""
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    http_method_names = ('get', 'post', 'put', 'delete',)

    @action(detail=True, methods=['get'], url_path='unique-manufacturers')
    def get_unique_contract_manufacturers(self, request: Request, pk: int) -> Response:
        """
        Returns unique manufacturers ids for contract
        For now only one query executed but there is no contract existence check so
        if contract with pk does not exist - returns empty list 
        """
        unique_manufacturers_ids = ContractService.get_unique_contract_manufacturers(contract_id=pk)
        return Response({'unique_manufacturers_ids': unique_manufacturers_ids}, status=status.HTTP_200_OK)
