import uuid
from src.shared.helpers.errors.domain_errors import EntityError

class E_Value():
    n_value: int
    edl_prcnt: float
    b_section: float
    e_external: float
    a_area: float
    fd_value: float
    CD_VALUE: int = 3
    e_id: str

    def __init__(self, n_value: int, edl_prcnt: float, b_section: float, e_external: float, a_area: float, fd_value: float, e_id: str = None):
        if not self.validate_n_value(n_value):
            raise EntityError("n_value")
        self.n_value = n_value

        if not self.validate_edl_prcnt(edl_prcnt):
            raise EntityError("edl_prcnt")
        self.edl_prcnt = edl_prcnt

        if not self.validate_b_section(b_section):
            raise EntityError("b_section")
        self.b_section = b_section

        if not self.validate_e_external(e_external):
            raise EntityError("e_external")
        self.e_external = e_external

        if not self.validate_a_area(a_area):
            raise EntityError("a_area")
        self.a_area = a_area

        if not self.validate_fd_value(fd_value):
            raise EntityError("fd_value")
        self.fd_value = fd_value

        if not self.validate_e_id(e_id):
            raise EntityError("e_id")
        self.e_id = e_id

    @staticmethod
    def validate_n_value(n_value: int) -> bool:
        if n_value is None:
            return False
        elif type(n_value) != int:
            return False
        return True

    @staticmethod
    def validate_edl_prcnt(edl_prcnt: float) -> bool:
        if edl_prcnt is None:
            return False
        elif type(edl_prcnt) != float:
            return False
        elif edl_prcnt < 0 or edl_prcnt > 100:
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
        elif fd_value == 0:
            return False
        return True

    @staticmethod
    def validate_e_id(e_id: str) -> bool:
        if not isinstance(e_id, str):
            return False
        try:
            val = uuid.UUID(e_id, version=4)
        except ValueError:
            return False
        return True

    def calculate_e(self, edl_prcnt: float, e_external: float, b_section: float, fd_value: float, a_area: float, n_value: int) -> float:
        edl_lux = (edl_prcnt * e_external) / 100
        duct = edl_lux * (b_section**2)

        if duct == 0 or fd_value == 0:
            return 0

        e = (n_value * duct * self.CD_VALUE * fd_value) / a_area
        return e