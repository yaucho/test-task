from contract.models import Contract
from manufacturer.models import Manufacturer


class ContractService:

    @classmethod
    def get_unique_contract_manufacturers(cls, contract: Contract) ->list[Manufacturer]:
        """Returns all unique manufacturers for contract"""
        return (
            Manufacturer.objects
            .filter(products__credit_request__contract=contract)
            .distinct()
        )
