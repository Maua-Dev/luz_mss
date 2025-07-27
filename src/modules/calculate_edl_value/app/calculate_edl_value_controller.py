from .calculate_edl_value_usecase import CalculateEdlValueUseCase
from .calculate_edl_value_viewmodel import CalculateEdlValueViewModel
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError


class CalculateEdlValueController:
    def __init__(self, calculate_edl_value_usecase: CalculateEdlValueUseCase):
        self.calculate_edl_value_usecase = calculate_edl_value_usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            body = request.data
            if 'b_section' not in body:
                return BadRequest({"message": "Campo 'b_section' ausente."})
            if 'h_height' not in body:
                return BadRequest({"message": "Campo 'h_height' ausente."})
            if 'p_reflectance' not in body:
                return BadRequest({"message": "Campo 'p_reflectance' ausente."})

            b_section = float(body['b_section'])
            h_height = float(body['h_height'])
            p_reflectance = float(body['p_reflectance'])

            # Calls use case to calculate the EDL value
            calculated_edl = self.calculate_edl_value_usecase(
                b_section=b_section,
                h_height=h_height,
                p_reflectance=p_reflectance
            )

            # Success response
            viewmodel = CalculateEdlValueViewModel(calculated_value=calculated_edl)
            return OK(viewmodel.to_dict())

        except ValueError as e:
            # Type error in the request body
            return BadRequest({"message": f"Erro de tipo de dados: {e}. Certifique-se de que os valores numéricos são válidos."})
        
        except EntityError as e:
            # Entity validation error 
            return BadRequest({"message": f"Erro de validação da entidade: {e.message}"})

        except Exception as e:
            # Catch any other unexpected errors
            return InternalServerError({"message": f"Erro interno do servidor: {e}"})