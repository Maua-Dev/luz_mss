from src.shared.domain.entities.n_value import N_Value
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.domain.repositories.n_value_repository_interface import INValueRepository
from src.shared.infra.repositories.edl_value_repository_mock import EdlValueRepositoryMock

class NValueRepositoryMock(INValueRepository):
    b_section = EdlValueRepositoryMock.calculate_edl.b_section
    edl_prcnt = EdlValueRepositoryMock.get_edl_value()
    calculate_n: float

    def __init__(self):
        self._mock_n_value = N_Value(e_lux=200.0, e_external=20000.0, a_area=544.0, fd=0.7)

    def get_n_parameters(self) -> N_Value:
        return self._mock_n_value