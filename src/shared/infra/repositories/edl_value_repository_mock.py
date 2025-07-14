from src.shared.domain.entities.edl_value import Edl_Value
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.domain.repositories.edl_value_repository_interface import IEdlValueRepository

class EdlValueRepositoryMock(IEdlValueRepository):
    def __init__(self, edl_value: Edl_Value = None):
        self._edl_values_db = {} # Simulates a database
        if edl_value:
            self._edl_values_db[edl_value.edl_id] = edl_value

    def save_edl_value(self, edl_value: Edl_Value) -> Edl_Value:
        if edl_value.edl_id in self._edl_values_db:
            raise ValueError("Já existe um valor EDL com este ID!")
        self._edl_values_db[edl_value.edl_id] = edl_value
        return edl_value

    def get_edl_value_by_id(self, edl_id: int) -> Edl_Value:
        if edl_id not in self._edl_values_db:
            raise NoItemsFound(f"Nenhum valor EDL encontrado com o ID {edl_id}.")
        return self._edl_values_db.get(edl_id)
