import uuid
from src.shared.helpers.errors.domain_errors import EntityError

class N_Value():
    edl_prcnt: float
    b_section: float
    e_lux: int
    e_external: float
    a_area: float
    fd_value: float
    cd_value: float
    n_id: str

    def __init__ (self, edl_prcnt: float, b_section: float, e_lux: int, e_external: float, a_area: float, fd_value: float, cd_value: float, n_id: str = None):
        if not self.validate_edl_prcnt(edl_prcnt):
            raise EntityError("edl_prcnt")
        self.edl_prcnt = edl_prcnt

        if not self.validate_b_section(b_section):
            raise EntityError("b_section")
        self.b_section = b_section

        if not self.validate_e_lux(e_lux):
            raise EntityError("e_lux")
        self.e_lux = e_lux

        if not self.validate_e_external(e_external):
            raise EntityError("e_external")
        self.e_external = e_external

        if not self.validate_a_area(a_area):
            raise EntityError("a_area")
        self.a_area = a_area

        if not self.validate_fd_value(fd_value):
            raise EntityError("fd_value")
        self.fd_value = fd_value

        if not self.validate_cd_value(cd_value):
            raise EntityError("cd_value")
        self.cd_value = cd_value

        if not self.validate_n_id(n_id):
            raise EntityError("n_id")
        self.n_id = n_id
    
    @staticmethod
    def validate_edl_prcnt(edl_prcnt: float) -> bool:
        if edl_prcnt is None:
            return False
        elif type(edl_prcnt) != float:
            return False
        return True
    
    @staticmethod
    def validate_b_section(b_section: float) -> bool:
        if b_section is None:
            return False
        elif type(b_section) != float:
            return False
        return True

    @staticmethod
    def validate_e_lux(e_lux: int) -> bool:
        if e_lux is None:
            return False
        elif type(e_lux) != int:
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
    def validate_a_area(a_area: float) -> bool:
        if a_area is None:
            return False
        elif type(a_area) != float:
            return False
        return True
    
    @staticmethod
    def validate_fd_value(fd_value: float) -> bool:
        if fd_value is None:
            return False
        elif type(fd_value) != float:
            return False
        return True

    @staticmethod
    def validate_cd_value(cd_value: float) -> bool:
        if cd_value is None:
            return False
        elif type(cd_value) != float:
            return False
        return True

    @staticmethod
    def validate_n_id(n_id: str) -> bool:
        if not isinstance(n_id, str):
            return False
        try:
            val = uuid.UUID(n_id, version=4)
        except ValueError:
            return False
        return True

    def calculate_n(self, edl_prcnt: float, b_section: float, e_lux: int, e_external: float, a_area: float, fd_value: float, cd_value: float) -> int:
        edl_lux = (edl_prcnt * e_external) / 100
        duct = edl_lux * (b_section**2)

        if duct == 0 or fd_value == 0:
            return 0

        n = round((e_lux * a_area) / (duct * cd_value * fd_value))
        return n