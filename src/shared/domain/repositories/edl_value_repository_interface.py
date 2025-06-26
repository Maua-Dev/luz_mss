from abc import abstractmethod
from src.shared.domain.entities.edl_value import Edl_Value

class IEdlValueRepository():

    @abstractmethod
    def get_edl_value(self) -> Edl_Value:
        pass