from src.shared.domain.enums.state_enum import STATE
from src.shared.helpers.errors.domain_errors import EntityError

class N_Value():
    edl: float
    e_lux: float
    e_external: float
    duct: float
    a_area: float
    fd: float
    CD_VALUE: int = 3
    state: STATE

    def __init__ (self, edl: float, e_lux: float, e_external: float, duct: float, a_area: float, fd: float, CD_VALUE: int, state:STATE):
        if not N_Value.validate_edl(edl):
            raise EntityError("edl")
        self.edl = edl

        if not N_Value.validate_e_lux(e_lux):
            raise EntityError("e_lux")
        self.e_lux = e_lux

        if not N_Value.validate_e_external(e_external):
            raise EntityError("e_external")
        self.e_external = e_external

        if not N_Value.validate_duct(duct):
            raise EntityError("duct")
        self.duct = duct

        if not N_Value.validate_a(a_area):
            raise EntityError("a_area")
        self.a_area = a_area

        if not N_Value.validate_fd(fd):
            raise EntityError("fd")
        self.fd = fd

        if not N_Value.validate_CD(CD_VALUE):
            raise EntityError("CD_VALUE")
        self.CD_VALUE = CD_VALUE

        if type(state) != STATE:
            raise EntityError("state")
        self.state = state
    
    @staticmethod
    def validate_edl(edl: float) -> bool:
        if edl is None:
            return False
        elif type(edl) != float:
            return False
        return True
    
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
    def validate_duct(duct: float) -> bool:
        if duct is None:
            return False
        elif type(duct) != float:
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
    def validate_CD(CD_VALUE: int) -> bool:
        if CD_VALUE is None:
            return False
        elif type(CD_VALUE) != int:
            return False
        elif CD_VALUE != 3:
            return False
        return True