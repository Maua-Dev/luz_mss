from abc import abstractmethod
from src.shared.domain.entities.edl_value import Edl_Value

class IEdlValueRepository():

    @abstractmethod
    def calculate_edl_value(self, b_section: float, h_height: float, p_reflectance: float) -> float:
        pass

    @abstractmethod
    def save_edl_value(self, edl_value: Edl_Value) -> Edl_Value:
        pass

    @abstractmethod
    def get_edl_value_by_id(self, edl_id: int) -> Edl_Value:
        pass