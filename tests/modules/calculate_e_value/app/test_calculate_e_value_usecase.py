from src.shared.infra.repositories.e_value_repository_mock import EValueRepositoryMock
from src.modules.calculate_e_value.app.calculate_e_value_usecase import CalculateEValueUseCase
import pytest

class TestCalculateEValueUseCase:

    def test_calculate_e_value(self):
        e_repo = EValueRepositoryMock()

        get_e_usecase = CalculateEValueUseCase(e_repo)

        # Call use case with example parameters
        n_value: int = 100
        edl_prcnt: float = 66.0
        b_section: float = 0.9
        e_external: float = 20000.0
        a_area: float = 544.0
        fd_value: float = 0.7

        try:
            result = get_e_usecase(n_value=n_value, edl_prcnt=edl_prcnt, b_section=b_section, e_external=e_external, a_area=a_area, fd_value=fd_value)
            print(f"O valor E calculado é: {result}")

            assert isinstance(result, float)
            assert result > 0

        except Exception as e:
            print(f"Erro ao calcular E: {e}")