from src.shared.domain.entities.e_value import E_Value
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.domain.repositories.e_value_repository_interface import IEValueRepository

class EValueRepositoryMock(IEValueRepository):
    
    def __init__(self, e_value: E_Value = None):
        self._e_values_db = {}
        if e_value:
            self._e_values_db[e_value.e_id] = e_value

    def save_e_value(self, e_value: E_Value) -> E_Value:
        if e_value.e_id in self._e_values_db:
            raise ValueError("Já existe um valor de iluminância média com este ID!")
        self._e_values_db[e_value.e_id] = e_value
        return e_value

    def get_e_value_by_id(self, e_id: int) -> E_Value:
        if e_id not in self._e_values_db:
            raise NoItemsFound(f"Nenhum valor de iluminância média encontrado com o ID {e_id}.")
        return self._e_values_db.get(e_id, None)

    def calculate_e_value(self, temp_e_entity: E_Value) -> float:
        if temp_e_entity is None:
            raise ValueError("O objeto E_Value não pode ser None.")
        return temp_e_entity.calculate_e(temp_e_entity.edl_prcnt, temp_e_entity.e_external, temp_e_entity.b_section, temp_e_entity.fd_value, temp_e_entity.a_area, temp_e_entity.n_value, temp_e_entity.cd_value)