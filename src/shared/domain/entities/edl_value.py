from src.shared.domain.enums.state_enum import STATE
from src.shared.helpers.errors.domain_errors import EntityError

class Edl_Value():
    b_section: float
    h_height: float
    p_reflectance: float
    state: STATE

    def __init__ (self, b_section: float, h_height: float, p_reflectance: float, state: STATE):
        if not Edl_Value.validate_b(b_section):
            raise EntityError("b_section")
        self.b_section = b_section

        if not Edl_Value.validate_h(h_height):
            raise EntityError("h_height")
        self.h_height = h_height

        if not Edl_Value.validate_p(p_reflectance):
            raise EntityError("p_reflectance")
        self.p_reflectance = p_reflectance

        if type(state) != STATE:
            raise EntityError("state")
        self.state = state
        
    @staticmethod
    def validate_b(b_section: float) -> bool:
        if b_section is None:
            return False
        elif type(b_section) != float:
            return False
        return True

    @staticmethod
    def validate_h(h_height: float) -> bool:
        if h_height is None:
            return False
        elif type(h_height) != float:
            return False
        return True

    @staticmethod
    def validate_p(p_reflectance: float) -> bool:
        if p_reflectance is None:
            return False
        elif type(p_reflectance) != float:
            return False
        return True