import math
from src.shared.helpers.errors.domain_errors import EntityError

class Edl_Value():
    b_section: float
    h_height: float
    p_reflectance: float

    def __init__ (self, b_section: float, h_height: float, p_reflectance: float):
        if not self.validate_b(b_section):
            raise EntityError("b_section")
        self.b_section = b_section

        if not self.validate_h(h_height):
            raise EntityError("h_height")
        self.h_height = h_height

        if not self.validate_p(p_reflectance):
            raise EntityError("p_reflectance")
        self.p_reflectance = p_reflectance
        
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
    
    def calculate_edl(self, b_section: float, h_height: float, p_reflectance: float) -> float:
        cfi = []

        for i in range(31):
            if i == 0:
                cfi_value = (math.sin(math.atan(b_section/h_height/2)))**2
                cfi.append(cfi_value)
            else:
                cfi_value = ((math.sin(math.atan((i+0.5)*b_section/h_height)))**2 -(math.sin(math.atan((i-0.5)*b_section/h_height)))**2)*p_reflectance**i
                cfi.append(cfi_value)

        edl_prcnt = round(sum(cfi)*100)
        return edl_prcnt