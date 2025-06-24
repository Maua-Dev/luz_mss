from src.shared.helpers.errors.domain_errors import EntityError

class N_Value():
    e_lux: float
    e_external: float
    a_area: float
    fd: float
    cd_value: float

    def __init__ (self, e_lux: float, e_external: float, a_area: float, fd: float, cd_value: float):
        if not self.validate_e_lux(e_lux):
            raise EntityError("e_lux")
        self.e_lux = e_lux

        if not self.validate_e_external(e_external):
            raise EntityError("e_external")
        self.e_external = e_external

        if not self.validate_a(a_area):
            raise EntityError("a_area")
        self.a_area = a_area

        if not self.validate_fd(fd):
            raise EntityError("fd")
        self.fd = fd

        if not self.validate_CD(cd_value):
            raise EntityError("cd_value")
        self.cd_value = cd_value
    
    @staticmethod
    def validate_e_lux(e_lux: float) -> bool:
        if e_lux is None:
            return False
        elif type(e_lux) != float:
            return False
        return True
    
    @staticmethod
    def validate_e_external(e_external: float) -> bool:
        if e_external is None:
            return False
        elif type(e_external) != float:
            return False
        return True
    
    @staticmethod
    def validate_a(a_area: float) -> bool:
        if a_area is None:
            return False
        elif type(a_area) != float:
            return False
        return True
    
    @staticmethod
    def validate_fd(fd: float) -> bool:
        if fd is None:
            return False
        elif type(fd) != float:
            return False
        return True
    
    @staticmethod
    def validate_CD(cd_value: float) -> bool:
        if cd_value is None:
            return False
        elif type(cd_value) != float:
            return False
        return True
    
    def calculate_n(self, edl_prcnt: float, b_section: float) -> int:
        # Esses valores (edl_prcnt e b_section) devem ser passados como parâmetros para o cálculo.
        
        edl_lux = (edl_prcnt * self.e_external) / 100
        duct = edl_lux * (b_section**2)

        if duct == 0 or self.cd_value == 0 or self.fd == 0:
            return 0

        n = round((self.e_lux * self.a_area) / (duct * self.CD_VALUE * self.fd))
        return n