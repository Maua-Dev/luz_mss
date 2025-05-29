from src.shared.domain.entities.edl_value import Edl_Value
from src.shared.domain.enums.state_enum import STATE
from src.shared.helpers.errors.domain_errors import EntityError
import pytest

class Test_Edl_Value:
    def test_edl(self):
        Edl_Value(b_section=0.9, h_height=6.0, p_reflectance=0.95, state=STATE.APPROVED)

    def test_edl_b_none(self):
        with pytest.raises(EntityError):
            Edl_Value(b_section=None, h_height=6, p_reflectance=0.95, state=STATE.APPROVED)

    def test_edl_b_not_float(self):
        with pytest.raises(EntityError):
            Edl_Value(b_section="1", h_height=6, p_reflectance=0.95, state=STATE.APPROVED)

    def test_edl_h_none(self):
        with pytest.raises(EntityError):
            Edl_Value(b_section=0.9, h_height=None, p_reflectance=0.95, state=STATE.APPROVED)

    def test_edl_h_not_float(self):
        with pytest.raises(EntityError):
            Edl_Value(b_section=0.9, h_height="6", p_reflectance=0.95, state=STATE.APPROVED)

    def test_edl_p_none(self):
        with pytest.raises(EntityError):
            Edl_Value(b_section=0.9, h_height=6, p_reflectance=None, state=STATE.APPROVED)

    def test_edl_p_not_float(self):
        with pytest.raises(EntityError):
            Edl_Value(b_section=0.9, h_height=6, p_reflectance="1", state=STATE.APPROVED)

    def test_edl_state_is_not_state(self):
        with pytest.raises(EntityError):
            Edl_Value(b_section=0.9, h_height=6, p_reflectance=0.95, state="APPROVED")