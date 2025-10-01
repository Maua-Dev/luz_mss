from abc import abstractmethod
from src.shared.domain.entities.e_value import E_Value

class IEValueRepository():

    @abstractmethod
    def calculate_e_value(self, n_value: int, edl_prcnt: float, e_external: float, a_area: float, fd_value: float) -> float:
        pass

    @abstractmethod
    def save_e_value(self, e_value: E_Value) -> E_Value:
        pass

    @abstractmethod
    def get_e_value_by_id(self, e_id: int) -> E_Value:
        pass