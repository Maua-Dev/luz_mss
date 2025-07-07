from src.shared.helpers.errors.domain_errors import EntityError

class N_Value():
    edl_prcnt: float
    b_section: float
    e_lux: float
    e_external: float
    a_area: float
    fd: float
    cd_value: float
    n_id: int

    def __init__ (self, edl_prcnt: float, b_section: float, e_lux: float, e_external: float, a_area: float, fd: float, cd_value: float, n_id: int = None):
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

        if not self.validate_a(a_area):
            raise EntityError("a_area")
        self.a_area = a_area

        if not self.validate_fd(fd):
            raise EntityError("fd")
        self.fd = fd

        if not self.validate_CD(cd_value):
            raise EntityError("cd_value")
        self.cd_value = cd_value

        if type(n_id) == int:
            if n_id < 0:
                raise EntityError("n_id")

        if type(n_id) != int:
            raise EntityError("n_id")

        self.n_id = n_id
    
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
    
    def calculate_n(self) -> int:        
        edl_lux = (self.edl_prcnt * self.e_external) / 100
        duct = edl_lux * (self.b_section**2)

        if duct == 0 or self.cd_value == 0 or self.fd == 0:
            return 0

        n = round((self.e_lux * self.a_area) / (duct * self.cd_value * self.fd))
        return n