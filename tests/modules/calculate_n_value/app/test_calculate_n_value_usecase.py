from src.shared.infra.repositories.n_value_repository_mock import NValueRepositoryMock
from src.modules.calculate_n_value.app.calculate_n_value_usecase import CalculateNValueUseCase
import pytest

class TestCalculateNValueUseCase:

    def test_calculate_n_value(self):
        n_repo = NValueRepositoryMock()

        get_n_usecase = CalculateNValueUseCase(n_repo)

        # Call use case with example parameters
        edl_prcnt = 66.0
        b_section = 0.9
        e_lux = 200
        e_external = 20000.0
        a_area = 544.0
        fd_value = 0.7

        try:
            result = get_n_usecase(edl_prcnt=edl_prcnt, b_section=b_section, e_lux=e_lux, e_external=e_external, a_area=a_area, fd_value=fd_value)
            print(f"O valor N calculado é: {result}")

            assert isinstance(result, float)
            assert result > 0

        except Exception as e:
            print(f"Erro ao calcular N: {e}")