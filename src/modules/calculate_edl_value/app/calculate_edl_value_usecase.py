import uuid
from src.shared.domain.entities.edl_value import Edl_Value
from src.shared.domain.repositories.edl_value_repository_interface import IEdlValueRepository

class CalculateEdlValueUseCase:
    def __init__(self, edl_repo: IEdlValueRepository):
        self._edl_repo = edl_repo

    def __call__(self,
                 b_section: float, 
                 h_height: float, 
                 p_reflectance: float) -> float:

        edl_entity = Edl_Value(edl_id=str(uuid.uuid4()), b_section=b_section, h_height=h_height, p_reflectance=p_reflectance)

        calculated_value = self._edl_repo.calculate_edl_value(edl_entity)
        return calculated_value