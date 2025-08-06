from src.modules.calculate_edl_value.app.calculate_edl_value_usecase import CalculateEdlValueUseCase
from src.modules.calculate_edl_value.app.calculate_edl_value_viewmodel import CalculateEdlValueViewModel
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError
from src.shared.helpers.errors.domain_errors import EntityError

class CalculateEdlValueController:
    def __init__(self, usecase: CalculateEdlValueUseCase):
        self.usecase = usecase

    def __call__(self, request: HttpRequest) -> HttpResponse:
        try:
            body = request.data

            # Secure access with get method to avoid KeyError
            b_section_str = body.get('b_section')
            h_height_str = body.get('h_height')
            p_reflectance_str = body.get('p_reflectance')

            if b_section_str is None:
                return BadRequest({"message": "Campo 'b_section' ausente."})
            if h_height_str is None:
                return BadRequest({"message": "Campo 'h_height' ausente."})
            if p_reflectance_str is None:
                return BadRequest({"message": "Campo 'p_reflectance' ausente."})
            
            # Convert string inputs to float
            try:
                b_section = float(b_section_str)
                h_height = float(h_height_str)
                p_reflectance = float(p_reflectance_str)

                if b_section < 0:
                    return BadRequest({"message": "Campo 'b_section' deve ser um número positivo."})
                if h_height < 0:
                    return BadRequest({"message": "Campo 'h_height' deve ser um número positivo."})
                if p_reflectance < 0:
                    return BadRequest({"message": "Campo 'p_reflectance' deve ser um número positivo."})
                    
            except ValueError:
                return BadRequest(body={"message": "Erro de tipo de dados. Certifique-se de que 'b_section', 'h_height' e 'p_reflectance' são valores numéricos válidos."})

            # Call the use case to calculate the EDL value
            calculated_edl = self.usecase(
                b_section=b_section,
                h_height=h_height,
                p_reflectance=p_reflectance
            )

            # Create the ViewModel with the calculated value
            viewmodel = CalculateEdlValueViewModel(calculated_value=calculated_edl)
            return OK(viewmodel.to_dict())

        except EntityError as e:
            # Handle entity validation errors
            return BadRequest({"message": f"Erro de validação da entidade: {e.message}"})

        except Exception as e:
            # Handle any other unexpected errors
            return InternalServerError({"message": f"Erro interno do servidor: {e}"})