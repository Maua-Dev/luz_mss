from src.modules.calculate_e_value.app.calculate_e_value_usecase import CalculateEValueUseCase
from src.modules.calculate_e_value.app.calculate_e_value_viewmodel import CalculateEValueViewModel
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError
from src.shared.helpers.errors.domain_errors import EntityError

class CalculateEValueController:
    def __init__(self, usecase: CalculateEValueUseCase):
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            body = request.data

            n_value_str = body.get("n_value")
            edl_prcnt_str = body.get("edl_prcnt")
            b_section_str = body.get("b_section")
            e_external_str = body.get("e_external")
            a_area_str = body.get("a_area")
            fd_value_str = body.get("fd_value")

            def tem_mais_de_3_casas_decimais(s_numero):
                # Verifica se há um ponto decimal na string
                if '.' in s_numero:
                    indice_ponto = s_numero.index('.')
                    parte_decimal = s_numero[indice_ponto + 1:]
                    
                    # Verifica se o comprimento da parte decimal é maior que 3
                    if len(parte_decimal) > 3:
                        return False

                # Se não houver ponto decimal ou se tiver 3 ou menos casas, retorna True
                return True

            if n_value_str is None:
                return BadRequest({"message": "Campo 'n_value' ausente ou inválido."})
            if edl_prcnt_str is None or not tem_mais_de_3_casas_decimais(str(edl_prcnt_str)):
                return BadRequest({"message": "Campo 'edl_prcnt' ausente ou inválido."})
            if b_section_str is None or not tem_mais_de_3_casas_decimais(str(b_section_str)):
                return BadRequest({"message": "Campo 'b_section' ausente ou inválido."})
            if e_external_str is None or not tem_mais_de_3_casas_decimais(str(e_external_str)):
                return BadRequest({"message": "Campo 'e_external' ausente ou inválido."})
            if a_area_str is None or not tem_mais_de_3_casas_decimais(str(a_area_str)):
                return BadRequest({"message": "Campo 'a_area' ausente ou inválido."})
            if fd_value_str is None or not tem_mais_de_3_casas_decimais(str(fd_value_str)):
                return BadRequest({"message": "Campo 'fd_value' ausente ou inválido."})

            try:
                n_value = int(n_value_str)
                edl_prcnt = float(edl_prcnt_str)
                b_section = float(b_section_str)
                e_external = float(e_external_str)
                a_area = float(a_area_str)
                fd_value = float(fd_value_str)

                if n_value < 0:
                    return BadRequest({"message": "Campo 'n_value' deve ser um número positivo."})
                if edl_prcnt < 0:
                    return BadRequest({"message": "Campo 'edl_prcnt' deve ser um número positivo."})
                if b_section < 0:
                    return BadRequest({"message": "Campo 'b_section' deve ser um número positivo."})
                if e_external < 0:
                    return BadRequest({"message": "Campo 'e_external' deve ser um número positivo."})
                if a_area < 0:
                    return BadRequest({"message": "Campo 'a_area' deve ser um número positivo."})
                if fd_value < 0:
                    return BadRequest({"message": "Campo 'fd_value' deve ser um número positivo."})

                if e_external == 0:
                    return InternalServerError({"message": f"Erro interno do servidor: {e}"})
                if fd_value == 0:
                    return InternalServerError({"message": f"Erro interno do servidor: {e}"})

                # Validate ranges
                if n_value > 1000000:
                    return BadRequest({"message": "Campo 'n_value' não deve ser maior que 1000000."})
                if edl_prcnt > 100:
                    return BadRequest({"message": "Campo 'edl_prcnt' não deve ser maior que 100%."})
                if b_section >= 10000:
                    return BadRequest({"message": "Campo 'b_section' não deve ser maior que 10000."})
                if e_external > 1000000:
                    return BadRequest({"message": "Campo 'e_external' não deve ser maior que 1000000."})
                if a_area > 1000000:
                    return BadRequest({"message": "Campo 'a_area' não deve ser maior que 1000000."})
                if fd_value > 1000000:
                    return BadRequest({"message": "Campo 'fd_value' não deve ser maior que 1000000."})

            except ValueError:
                return BadRequest(body={"message": "Erro de tipo de dados. Certifique-se de que todos os campos são valores numéricos válidos."})

            # Call the use case to calculate the E value
            calculated_e = self.usecase(
                n_value=n_value,
                edl_prcnt=edl_prcnt,
                b_section=b_section,
                e_external=e_external,
                a_area=a_area,
                fd_value=fd_value
            )

            # Create the ViewModel with the calculated value
            viewmodel = CalculateEValueViewModel(calculated_value=calculated_e)
            return OK(viewmodel.to_dict())

        except EntityError as e:
            # Handle entity validation errors
            return BadRequest({"message": f"Erro de validação da entidade: {e.message}"})

        except Exception as e:
            # Handle any other unexpected errors
            return InternalServerError({"message": f"Erro interno do servidor: {e}"})