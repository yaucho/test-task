from credit_request.models import CreditRequest


class ContractService:

    @classmethod
    def get_unique_contract_manufacturers(cls, contract_id: int) ->list[int]:
        """Returns all unique manufacturers ids for contract"""
        return (
            CreditRequest.objects
            .filter(contract_id=contract_id)
            .values_list('products__manufacturer', flat=True)
            .distinct()
        )
