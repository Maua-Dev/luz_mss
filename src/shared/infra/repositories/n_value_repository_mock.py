from src.shared.domain.entities.n_value import N_Value
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.domain.repositories.n_value_repository_interface import INValueRepository

class NValueRepositoryMock(INValueRepository):
    def __init__(self, n_value: N_Value = None):
        self._n_values_db = {} # Simulates a database
        if n_value:
            self._n_values_db[n_value.n_id] = n_value

    def save_edl_value(self, n_value: N_Value) -> N_Value:
        if n_value.n_id in self._n_values_db:
            raise ValueError("Já existe um valor N com este ID!")
        self._n_values_db[n_value.n_id] = n_value
        return n_value

    def get_n_value_by_id(self, n_id: int) -> N_Value:
        if n_id not in self._n_values_db:
            raise NoItemsFound(f"Nenhum valor N encontrado com o ID {n_id}.")
        return self._n_values_db.get(n_id)