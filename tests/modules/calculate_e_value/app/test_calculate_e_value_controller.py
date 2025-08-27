import pytest

from src.modules.calculate_e_value.app.calculate_e_value_controller import CalculateEValueController
from src.modules.calculate_e_value.app.calculate_e_value_usecase import CalculateEValueUseCase
from src.shared.infra.repositories.e_value_repository_mock import EValueRepositoryMock
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError
from src.shared.helpers.errors.domain_errors import EntityError

class TestCalculateEValueController:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.repository = EValueRepositoryMock()
        self.usecase = CalculateEValueUseCase(self.repository)
        self.controller = CalculateEValueController(self.usecase)

    def test_calculate_e_value_controller_success(self):
        request = HttpRequest(body={
            'cd_value': 3.0,
            'n_value': 10,
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.controller(request)

        assert isinstance(response, OK)
        assert response.status_code == 200
        assert response.body == {"calculated_e_value": 413.0}

    def test_calculate_e_value_controller_missing_n_value(self):
        request = HttpRequest(body={
            'cd_value': 3.0,
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'n_value' ausente ou inválido."}

    def test_calculate_e_value_controller_missing_edl_prcnt(self):
        request = HttpRequest(body={
            'cd_value': 3.0,
            'n_value': 5,
            'b_section': 0.9,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'edl_prcnt' ausente ou inválido."}

    def test_calculate_e_value_controller_missing_b_section(self):
        request = HttpRequest(body={
            'cd_value': 3.0,
            'n_value': 5,
            'edl_prcnt': 66.0,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'b_section' ausente ou inválido."}

    def test_calculate_e_value_controller_missing_e_external(self):
        request = HttpRequest(body={
            'cd_value': 3.0,
            'n_value': 5,
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'e_external' ausente ou inválido."}

    def test_calculate_e_value_controller_missing_a_area(self):
        request = HttpRequest(body={
            'cd_value': 3.0,
            'n_value': 5,
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_external': 20000.0,
            'fd_value': 0.7
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'a_area' ausente ou inválido."}

    def test_calculate_e_value_controller_missing_fd_value(self):
        request = HttpRequest(body={
            'cd_value': 3.0,
            'n_value': 5,
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_external': 20000.0,
            'a_area': 544.0,
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'fd_value' ausente ou inválido."}

    def test_calculate_e_value_controller_invalid_n_value_type(self):
        request = HttpRequest(body={
            'cd_value': 3.0,
            'n_value': 'invalid',
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert "Erro de tipo de dados" in response.body['message']

    def test_calculate_e_value_controller_invalid_edl_prcnt_type(self):
        request = HttpRequest(body={
            'cd_value': 3.0,
            'n_value': 5,
            'edl_prcnt': 'invalid',
            'b_section': 0.9,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert "Erro de tipo de dados" in response.body['message']

    def test_calculate_e_value_controller_invalid_b_section_type(self):
        request = HttpRequest(body={
            'cd_value': 3.0,
            'n_value': 5,
            'edl_prcnt': 66.0,
            'b_section': 'invalid',
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.controller(request)
        
        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert "Erro de tipo de dados" in response.body['message']

    def test_calculate_e_value_controller_invalid_e_external_type(self):
        request = HttpRequest(body={
            'cd_value': 3.0,
            'n_value': 5,
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_external': 'invalid',
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert "Erro de tipo de dados" in response.body['message']

    def test_calculate_e_value_controller_invalid_a_area_type(self):
        request = HttpRequest(body={
            'cd_value': 3.0,
            'n_value': 5,
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_external': 20000.0,
            'a_area': 'invalid',
            'fd_value': 0.7
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert "Erro de tipo de dados" in response.body['message']

    def test_calculate_e_value_controller_invalid_fd_value_type(self):
        request = HttpRequest(body={
            'cd_value': 3.0,
            'n_value': 5,
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 'invalid'
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert "Erro de tipo de dados" in response.body['message']

    def test_calculate_e_value_controller_invalid_n_value_value(self):
        request = HttpRequest(body={
            'cd_value': 3.0,
            'n_value': -1.0,
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'n_value' deve ser um número positivo."}

    def test_calculate_e_value_controller_invalid_edl_prcnt_value(self):
        request  = HttpRequest(body={
            'cd_value': 3.0,
            'n_value': 5,
            'edl_prcnt': -1.0,
            'b_section': 0.9,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'edl_prcnt' deve ser um número positivo."}

    def test_calculate_e_value_controller_invalid_b_section_value(self):
        request = HttpRequest(body={
            'cd_value': 3.0,
            'n_value': 5,
            'edl_prcnt': 66.0,
            'b_section': -1.0,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'b_section' deve ser um número positivo."}

    def test_calculate_e_value_controller_invalid_e_external_value(self):
        request = HttpRequest(body = {
            'cd_value': 3.0,
            'n_value': 5,
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_external': -1.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'e_external' deve ser um número positivo."}

    def test_calculate_e_value_controller_invalid_a_area_value(self):
        request = HttpRequest(body={
            'cd_value': 3.0,
            'n_value': 5,
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_external': 20000.0,
            'a_area': -1.0,
            'fd_value': 0.7
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'a_area' deve ser um número positivo."}

    def test_calculate_e_value_controller_invalid_fd_value(self):
        request = HttpRequest(body={
            'cd_value': 3.0,
            'n_value': 5,
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': -1.0
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'fd_value' deve ser um número positivo."}

    def test_calculate_e_value_controller_out_of_range_n_value(self):
        request = HttpRequest(body={
            'cd_value': 3.0,
            'n_value': 1000001,
            'edl_prcnt': 101.0,
            'b_section': 10001.0,
            'e_external': 1000001.0,
            'a_area': 1000001.0,
            'fd_value': 1000001.0
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert "não deve ser maior que" in response.body['message']

    def test_calculate_e_value_controller_out_of_range_edl_prcnt(self):
        request = HttpRequest(body={
            'cd_value': 3.0,
            'n_value': 5,
            'edl_prcnt': 101.0,
            'b_section': 0.9,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert "não deve ser maior que" in response.body['message']

    def test_calculate_e_value_controller_out_of_range_b_section(self):
        request = HttpRequest(body={
            'cd_value': 3.0,
            'n_value': 5,
            'edl_prcnt': 66.0,
            'b_section': 10001.0,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert "não deve ser maior que" in response.body['message']

    def test_calculate_e_value_controller_out_of_range_e_external(self):
        request = HttpRequest(body={
            'cd_value': 3.0,
            'n_value': 5,
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_external': 1000001.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert "não deve ser maior que" in response.body['message']

    def test_calculate_e_value_controller_out_of_range_a_area(self):
        request = HttpRequest(body={
            'cd_value': 3.0,
            'n_value': 5,
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_external': 20000.0,
            'a_area': 1000001.0,
            'fd_value': 0.7
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert "não deve ser maior que" in response.body['message']

    def test_calculate_e_value_controller_out_of_range_fd_value(self):
        request = HttpRequest(body={
            'cd_value': 3.0,
            'n_value': 5,
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 1000001.0
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert "não deve ser maior que" in response.body['message']

    # Testes para campo 'cd_value'

    def test_calculate_e_value_controller_missing_cd_value(self):
        request = HttpRequest(body={
            'n_value': 5,
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert response.body == {"message": "Campo 'cd_value' ausente ou inválido."}

    def test_calculate_e_value_controller_invalid_cd_value(self):
        request = HttpRequest(body={
            'cd_value': 'invalid',
            'n_value': 5,
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert "Erro de tipo de dados" in response.body['message']

    def test_calculate_e_value_controller_out_of_range_cd_value(self):
        request = HttpRequest(body={
            'cd_value': 4.0,
            'n_value': 5,
            'edl_prcnt': 66.0,
            'b_section': 0.9,
            'e_external': 20000.0,
            'a_area': 544.0,
            'fd_value': 0.7
        })
        response = self.controller(request)

        assert isinstance(response, BadRequest)
        assert response.status_code == 400
        assert "deve estar entre 0 e 3" in response.body['message']