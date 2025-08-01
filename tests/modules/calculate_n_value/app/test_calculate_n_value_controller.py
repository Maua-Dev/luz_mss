from src.modules.calculate_n_value.app.calculate_n_value_usecase import CalculateNValueUseCase
from src.modules.calculate_n_value.app.calculate_n_value_presenter import CalculateNValuePresenter
from src.modules.calculate_n_value.app.calculate_n_value_controller import CalculateNValueController
from src.shared.infra.repositories.n_value_repository_mock import NValueRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError
import pytest

class TestCalculateNValuePresenter:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.repo = NValueRepositoryMock()
        self.usecase = CalculateNValueUseCase(self.repo)
        self.presenter = CalculateNValuePresenter(self.usecase)
        self.controller = CalculateNValueController(self.presenter)

    def test_calculate_n_value_controller_success(self):
            request = HttpRequest(body={
                'edl_prcnt': 66.0,
                'b_section': 0.9,
                'e_lux': 200,
                'e_external': 20000.0,
                'a_area': 544.0,
                'fd_value': 0.7
            })
            response = self.controller(request)

            assert isinstance(response, OK)
            assert response.status_code == 200
            assert response.body == {"calculated_n_value": 5.0}

    def test_calculate_n_value_controller_missing_fields_delegation(self):
        request = HttpRequest(body={
            'edl_prcnt': 66.0,
            'e_lux': 200,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'b_section' ausente."}

    def test_calculate_n_value_controller_invalid_type_delegation(self):
        request = HttpRequest(body={
            'edl_prcnt': 66.0,
            'b_section': 'invalid',
            'e_lux': 200,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert "Erro de tipo de dados" in response.body['message']

    def test_calculate_n_value_controller_invalid_value_delegation(self):
        request = HttpRequest(body={
            'edl_prcnt': 66.0,
            'b_section': -1.0,
            'e_lux': 200,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'b_section' deve ser um número positivo."}