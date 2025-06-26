from abc import abstractmethod
from src.shared.domain.entities.n_value import N_Value

class INValueRepository():

    @abstractmethod
    def get_n_value(self) -> N_Value:
        pass