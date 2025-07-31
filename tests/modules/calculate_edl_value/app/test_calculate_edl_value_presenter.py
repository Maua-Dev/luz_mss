import pytest

from src.modules.calculate_edl_value.app.calculate_edl_value_presenter import CalculateEdlValuePresenter
from src.modules.calculate_edl_value.app.calculate_edl_value_usecase import CalculateEdlValueUseCase
from src.shared.infra.repositories.edl_value_repository_mock import EdlValueRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError
from src.shared.helpers.errors.domain_errors import EntityError

class TestCalculateEdlValuePresenter:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.repository = EdlValueRepositoryMock()
        self.usecase = CalculateEdlValueUseCase(self.repository)
        self.presenter = CalculateEdlValuePresenter(self.usecase)

    def test_calculate_edl_value_presenter_success(self):
        request = HttpRequest(body={
            'b_section': 0.9,
            'h_height': 6.0,
            'p_reflectance': 0.95
        })
        response = self.presenter.handle(request)

        assert isinstance(response, OK)
        assert response.status_code == 200
        assert response.body == {"calculated_edl_value": 66.0}

    def test_calculate_edl_value_presenter_missing_b_section(self):
        request = HttpRequest(body={
            'h_height': 2.0,
            'p_reflectance': 0.5
        })
        response = self.presenter.handle(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'b_section' ausente."}

    def test_calculate_edl_value_presenter_missing_h_height(self):
        request = HttpRequest(body={
            'b_section': 1.0,
            'p_reflectance': 0.5
        })
        response = self.presenter.handle(request)
        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'h_height' ausente."}

    def test_calculate_edl_value_presenter_missing_p_reflectance(self):
        request = HttpRequest(body={
            'b_section': 1.0,
            'h_height': 2.0
        })
        response = self.presenter.handle(request)
        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'p_reflectance' ausente."}

    def test_calculate_edl_value_presenter_invalid_b_section_type(self):
        request = HttpRequest(body={
            'b_section': 'abc', 
            'h_height': 2.0,
            'p_reflectance': 0.5
        })
        response = self.presenter.handle(request)
        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert "Erro de tipo de dados" in response.body['message']

    def test_calculate_edl_value_presenter_invalid_h_height_type(self):
        request = HttpRequest(body={
            'b_section': 1.0,
            'h_height': 'xyz', 
            'p_reflectance': 0.5
        })
        response = self.presenter.handle(request)
        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert "Erro de tipo de dados" in response.body['message']
        
    def test_calculate_edl_value_presenter_invalid_p_reflectance_type(self):
        request = HttpRequest(body={
            'b_section': 1.0,
            'h_height': 2.0,
            'p_reflectance': 'qwe' 
        })
        response = self.presenter.handle(request)
        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert "Erro de tipo de dados" in response.body['message']

    def test_calculate_edl_value_presenter_invalid_b_section_value(self):
        request = HttpRequest(body={
            'b_section': -1.0,
            'h_height': 2.0,
            'p_reflectance': 0.5
        })
        response = self.presenter.handle(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'b_section' deve ser um número positivo."}

    def test_calculate_edl_value_presenter_invalid_h_height_value(self):
        request = HttpRequest(body={
            'b_section': 1.0,
            'h_height': -2.0,
            'p_reflectance': 0.5
        })
        response = self.presenter.handle(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'h_height' deve ser um número positivo."}

    def test_calculate_edl_value_presenter_invalid_p_reflectance_value(self):
        request = HttpRequest(body={
            'b_section': 1.0,
            'h_height': 2.0,
            'p_reflectance': -0.5
        })
        response = self.presenter.handle(request)
        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'p_reflectance' deve ser um número positivo."}