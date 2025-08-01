import pytest

from src.modules.calculate_n_value.app.calculate_n_value_presenter import CalculateNValuePresenter
from src.modules.calculate_n_value.app.calculate_n_value_usecase import CalculateNValueUseCase
from src.shared.infra.repositories.n_value_repository_mock import NValueRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError
from src.shared.helpers.errors.domain_errors import EntityError

class TestCalculateNValuePresenter:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.repository = NValueRepositoryMock()
        self.usecase = CalculateNValueUseCase(self.repository)
        self.presenter = CalculateNValuePresenter(self.usecase)

    def test_calculate_n_value_presenter_success(self):
        request = HttpRequest(body={
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_lux': 200,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.presenter.handle(request)

        assert isinstance(response, OK)
        assert response.status_code == 200
        assert response.body == {"calculated_n_value": 5.0}

    def test_calculate_n_value_presenter_missing_edl_prcnt(self):
        request = HttpRequest(body={
            'b_section': 0.9,
            'e_lux': 200,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.presenter.handle(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'edl_prcnt' ausente."}

    def test_calculate_n_value_presenter_missing_b_section(self):
        request = HttpRequest(body={
            'edl_prcnt': 66.0,
            'e_lux': 200,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.presenter.handle(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'b_section' ausente."}

    def test_calculate_n_value_presenter_missing_e_lux(self):
        request = HttpRequest(body={
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.presenter.handle(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'e_lux' ausente."}

    def test_calculate_n_value_presenter_missing_e_external(self):
        request = HttpRequest(body={
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_lux': 200,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.presenter.handle(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'e_external' ausente."}

    def test_calculate_n_value_presenter_missing_a_area(self):
        request = HttpRequest(body={
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_lux': 200,
            'e_external': 20000.0,
            'fd_value': 0.7
        })
        response = self.presenter.handle(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'a_area' ausente."}

    def test_calculate_n_value_presenter_missing_fd_value(self):
        request = HttpRequest(body={
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_lux': 200,
            'e_external': 20000.0,
            'a_area': 544.0
        })
        response = self.presenter.handle(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'fd_value' ausente."}

    def test_calculate_n_value_presenter_invalid_edl_prcnt_type(self):
        request = HttpRequest(body={
            'edl_prcnt': 'invalid',
            'b_section': 0.9,
            'e_lux': 200,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.presenter.handle(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert "Erro de tipo de dados" in response.body['message']

    def test_calculate_n_value_presenter_invalid_b_section_type(self):
        request = HttpRequest(body={
            'edl_prcnt': 66.0,
            'b_section': 'invalid',
            'e_lux': 200,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.presenter.handle(request)
        
        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert "Erro de tipo de dados" in response.body['message']

    def test_calculate_n_value_presenter_invalid_e_lux_type(self):
        request = HttpRequest(body={
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_lux': 'invalid',
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.presenter.handle(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert "Erro de tipo de dados" in response.body['message']

    def test_calculate_n_value_presenter_invalid_e_external_type(self):
        request = HttpRequest(body={
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_lux': 200,
            'e_external': 'invalid',
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.presenter.handle(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert "Erro de tipo de dados" in response.body['message']

    def test_calculate_n_value_presenter_invalid_a_area_type(self):
        request = HttpRequest(body={
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_lux': 200,
            'e_external': 20000.0,
            'a_area': 'invalid',
            'fd_value': 0.7
        })
        response = self.presenter.handle(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert "Erro de tipo de dados" in response.body['message']

    def test_calculate_n_value_presenter_invalid_fd_value_type(self):
        request = HttpRequest(body={
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_lux': 200,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 'invalid'
        })
        response = self.presenter.handle(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert "Erro de tipo de dados" in response.body['message']

    def test_calculate_n_value_presenter_invalid_edl_prcnt_value(self):
        request  = HttpRequest(body={
            'edl_prcnt': -1.0,
            'b_section': 0.9,
            'e_lux': 200,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.presenter.handle(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'edl_prcnt' deve ser um número positivo."}

    def test_calculate_n_value_presenter_invalid_b_section_value(self):
        request = HttpRequest(body={
            'edl_prcnt': 66.0,
            'b_section': -1.0,
            'e_lux': 200,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.presenter.handle(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'b_section' deve ser um número positivo."}

    def test_calculate_n_value_presenter_invalid_e_lux_value(self):
        request = HttpRequest(body={
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_lux': -1,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.presenter.handle(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'e_lux' deve ser um número positivo."}

    def test_calculate_n_value_presenter_invalid_e_external_value(self):
        request = HttpRequest(body = {
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_lux': 200,
            'e_external': -1.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.presenter.handle(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'e_external' deve ser um número positivo."}

    def test_calculate_n_value_presenter_invalid_a_area_value(self):
        request = HttpRequest(body={
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_lux': 200,
            'e_external': 20000.0,
            'a_area': -1.0,
            'fd_value': 0.7
        })
        response = self.presenter.handle(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'a_area' deve ser um número positivo."}

    def test_calculate_n_value_presenter_invalid_fd_value(self):
        request = HttpRequest(body={
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_lux': 200,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': -1.0
        })
        response = self.presenter.handle(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'fd_value' deve ser um número positivo."}
