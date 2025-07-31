from src.modules.calculate_edl_value.app.calculate_edl_value_usecase import CalculateEdlValueUseCase
from src.modules.calculate_edl_value.app.calculate_edl_value_presenter import CalculateEdlValuePresenter
from src.modules.calculate_edl_value.app.calculate_edl_value_controller import CalculateEdlValueController
from src.shared.infra.repositories.edl_value_repository_mock import EdlValueRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError
import pytest

class TestCalculateEdlValuePresenter:

    def setup(self):
        self.repo = EdlValueRepositoryMock()
        self.usecase = CalculateEdlValueUseCase(self.repo)
        self.presenter = CalculateEdlValuePresenter(self.usecase)
        self.controller = CalculateEdlValueController(self.presenter)

    def test_calculate_edl_value_controller_success(self):
            request = HttpRequest(body={
                'b_section': 0.9,
                'h_height': 6.0,
                'p_reflectance': 0.95
            })
            response = self.controller(request)

            assert isinstance(response, OK)
            assert response.status_code == 200
            assert response.body == {"calculated_edl_value": 66.0}

    def test_calculate_edl_value_controller_missing_fields_delegation(self):
        request = HttpRequest(body={
            'h_height': 2.0,
            'p_reflectance': 0.5
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'b_section' ausente."}

    def test_calculate_edl_value_controller_invalid_type_delegation(self):
        request = HttpRequest(body={
            'b_section': 'invalid',
            'h_height': 2.0,
            'p_reflectance': 0.5
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert "Erro de tipo de dados" in response.body['message']

    def test_calculate_edl_value_controller_invalid_value_delegation(self):
        request = HttpRequest(body={
            'b_section': -1.0,
            'h_height': 2.0,
            'p_reflectance': 0.5
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'b_section' deve ser um número positivo."}