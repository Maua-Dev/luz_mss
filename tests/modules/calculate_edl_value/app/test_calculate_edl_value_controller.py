from src.modules.calculate_edl_value.app.calculate_edl_value_controller import CalculateEdlValueController
from src.modules.calculate_edl_value.app.calculate_edl_value_usecase import CalculateEdlValueUseCase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.edl_value_repository_mock import EdlValueRepositoryMock

class TestCalculateEdlValueController:

    def test_calculate_edl_value_success(self):
        edl_repo = EdlValueRepositoryMock()
        usecase = CalculateEdlValueUseCase(edl_repo)
        controller = CalculateEdlValueController(usecase)

        request = HttpRequest(body={
            'b_section': 0.9,
            'h_height': 6.0,
            'p_reflectance': 0.95
        })
        response = controller(request)
        assert response.status_code == 200
        assert 'calculated_edl_value' in response.data

    def test_calculate_edl_value_missing_fields(self):
        edl_repo = EdlValueRepositoryMock()
        usecase = CalculateEdlValueUseCase(edl_repo)
        controller = CalculateEdlValueController(usecase)

        request = HttpRequest(body={
            'h_height': 2.0,
            'p_reflectance': 0.5
        })
        response = controller(request)
        assert response.status_code == 400
        assert "Campo 'b_section' ausente." in response.data['message']

    def test_calculate_edl_value_invalid_type(self):
        edl_repo = EdlValueRepositoryMock()
        usecase = CalculateEdlValueUseCase(edl_repo)
        controller = CalculateEdlValueController(usecase)

        request = HttpRequest(body={
            'b_section': 'invalid',
            'h_height': 2.0,
            'p_reflectance': 0.5
        })
        response = controller(request)
        assert response.status_code == 400
        assert "Erro de tipo de dados" in response.data['message']