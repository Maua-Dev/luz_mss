from src.modules.calculate_n_value.app.calculate_n_value_usecase import CalculateNValueUseCase
from src.modules.calculate_n_value.app.calculate_n_value_viewmodel import CalculateNValueViewModel
from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError
from src.shared.helpers.errors.domain_errors import EntityError

class CalculateNValuePresenter:
    def __init__(self, usecase: CalculateNValueUseCase):
        self.usecase = usecase

    def handle(self, request: HttpRequest) -> HttpResponse:
        try:
            body = request.data

            edl_prcnt_str = body.get('edl_prcnt')
            b_section_str = body.get('b_section')
            e_lux_str = body.get('e_lux')
            e_external_str = body.get('e_external')
            a_area_str = body.get('a_area')
            fd_value_str = body.get('fd_value')

            if edl_prcnt_str is None:
                return BadRequest({"message": "Campo 'edl_prcnt' ausente."})
            if b_section_str is None:
                return BadRequest({"message": "Campo 'b_section' ausente."})
            if e_lux_str is None:
                return BadRequest({"message": "Campo 'e_lux' ausente."})
            if e_external_str is None:
                return BadRequest({"message": "Campo 'e_external' ausente."})
            if a_area_str is None:
                return BadRequest({"message": "Campo 'a_area' ausente."})
            if fd_value_str is None:
                return BadRequest({"message": "Campo 'fd_value' ausente."})

            try:
                edl_prcnt = float(edl_prcnt_str)
                b_section = float(b_section_str)
                e_lux = int(e_lux_str)
                e_external = float(e_external_str)
                a_area = float(a_area_str)
                fd_value = float(fd_value_str)

                if edl_prcnt < 0:
                    return BadRequest({"message": "Campo 'edl_prcnt' deve ser um número positivo."})
                if b_section < 0:
                    return BadRequest({"message": "Campo 'b_section' deve ser um número positivo."})
                if e_lux < 0:
                    return BadRequest({"message": "Campo 'e_lux' deve ser um número positivo."})
                if e_external < 0:
                    return BadRequest({"message": "Campo 'e_external' deve ser um número positivo."})
                if a_area < 0:
                    return BadRequest({"message": "Campo 'a_area' deve ser um número positivo."})
                if fd_value < 0:
                    return BadRequest({"message": "Campo 'fd_value' deve ser um número positivo."})
                
            except ValueError:
                return BadRequest(body={"message": "Erro de tipo de dados. Certifique-se de que todos os campos são valores numéricos válidos."})

            # Call the use case to calculate the N value
            calculated_n = self.usecase(
                edl_prcnt=edl_prcnt,
                b_section=b_section,
                e_lux=e_lux,
                e_external=e_external,
                a_area=a_area,
                fd_value=fd_value
            )

            # Create the ViewModel with the calculated value
            viewmodel = CalculateNValueViewModel(calculated_value=calculated_n)
            return OK(viewmodel.to_dict())

        except EntityError as e:
            # Handle entity validation errors
            return BadRequest({"message": f"Erro de validação da entidade: {e.message}"})

        except Exception as e:
            # Handle any other unexpected errors
            return InternalServerError({"message": f"Erro interno do servidor: {e}"})