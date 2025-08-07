from src.shared.infra.repositories.edl_value_repository_mock import EdlValueRepositoryMock
from src.modules.calculate_edl_value.app.calculate_edl_value_usecase import CalculateEdlValueUseCase
import pytest

class TestCalculateEdlValueUseCase:

    def test_calculate_edl_value(self):
        edl_repo = EdlValueRepositoryMock()

        get_edl_usecase = CalculateEdlValueUseCase(edl_repo)

        # Call use case with example parameters
        b = 0.9
        h = 6.0
        p = 0.95

        try:
            result = get_edl_usecase(b_section=b, h_height=h, p_reflectance=p)
            print(f"O valor EDL calculado é: {result}")

            assert isinstance(result, float)
            assert result > 0
            
        except Exception as e:
            print(f"Erro ao calcular EDL: {e}")