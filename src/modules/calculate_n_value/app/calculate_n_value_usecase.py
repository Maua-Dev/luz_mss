import uuid
from src.shared.domain.entities.n_value import N_Value
from src.shared.domain.repositories.n_value_repository_interface import INValueRepository

class CalculateNValueUseCase:
    def __init__(self, n_value_repo: INValueRepository):
        self._n_value_repo = n_value_repo

    def __call__(self, edl_prcnt: float,
                 b_section: float,
                 e_lux: int,
                 e_external: float,
                 a_area: float,
                 fd_value: float
                 ) -> float:

        n_value_entity = N_Value(n_id=str(uuid.uuid4()), 
                                 edl_prcnt=edl_prcnt,
                                 b_section=b_section,
                                 e_lux=e_lux,
                                 e_external=e_external,
                                 a_area=a_area,
                                 fd_value=fd_value)

        calculated_value = self._n_value_repo.calculate_n_value(n_value_entity)
        return calculated_value