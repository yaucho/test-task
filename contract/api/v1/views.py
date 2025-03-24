from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from contract.api.v1.serializers import ContractSerializer
from contract.models import Contract


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

    @action(detail=True, methods=['get'], url_path='unique-manufacturers')
    def get_unique_contract_manufacturers(self, request: Request, pk: int) -> Response:
        """"""
        return Response({'response': 'ok'}, status=status.HTTP_200_OK)
