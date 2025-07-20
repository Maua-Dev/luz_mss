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

    def calculate_e_value(self, b_section: float, h_height: float, p_reflectance: float) -> float:
        '''
        This method simulates the calculation of an E value based on the E_Value instance created below.
        '''
        temp_e_entity = E_Value(b_section=b_section, h_height=h_height, p_reflectance=p_reflectance, e_id="00000000-0000-0000-0000-000000000000")
        return temp_e_entity.calculate_e()