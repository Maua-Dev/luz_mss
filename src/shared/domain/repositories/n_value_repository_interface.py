from abc import abstractmethod
from src.shared.domain.entities.n_value import N_Value

class INValueRepository():

    @abstractmethod
    def calculate_n_value(self, edl_prcnt: float, b_section: float, e_lux: int, e_external: float, a_area: float, fd_value: float, cd_value: float) -> int:
        pass

    @abstractmethod
    def save_n_value(self, n_value: N_Value) -> N_Value:
        pass

    @abstractmethod
    def get_n_value_by_id(self, n_id: int) -> N_Value:
        pass