from src.shared.domain.entities.edl_value import Edl_Value
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.domain.repositories.edl_value_repository_interface import IEdlValueRepository

class EdlValueRepositoryMock(IEdlValueRepository):
    def __init__(self, b_section:float=0.9, h_height:float=6.0, p_reflectance:float=0.95):
        self._mock_edl_value = Edl_Value(b_section=b_section, h_height=h_height, p_reflectance=p_reflectance)
        
    def get_edl_parameters(self) -> Edl_Value:
        return self._mock_edl_value