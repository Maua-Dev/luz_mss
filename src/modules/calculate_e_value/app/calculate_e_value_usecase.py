import uuid
from src.shared.domain.entities.e_value import E_Value
from src.shared.domain.repositories.e_value_repository_interface import IEValueRepository

class CalculateEValueUseCase:
    def __init__(self, e_value_repo: IEValueRepository):
        self._e_value_repo = e_value_repo

    def __call__(self, n_value: int,
                edl_prcnt: float,
                b_section: float,
                e_external: float,
                a_area: float,
                fd_value: float
                 ) -> float:

        e_value_entity = E_Value(e_id=str(uuid.uuid4()), 
                                 n_value=n_value,
                                 edl_prcnt=edl_prcnt,
                                 b_section=b_section,
                                 e_external=e_external,
                                 a_area=a_area,
                                 fd_value=fd_value)

        calculated_value = self._e_value_repo.calculate_e_value(e_value_entity)
        return calculated_value