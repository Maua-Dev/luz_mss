from src.shared.domain.entities.n_value import N_Value
from src.shared.domain.enums.state_enum import STATE
from src.shared.helpers.errors.domain_errors import EntityError
import pytest

class Test_N_Value:
    def test_n(self):
        N_Value(edl=0.66, e_lux=200.0, e_external=20000.0, duct=10692.0, a_area=544.0, fd=0.7, CD_VALUE=3, state=STATE.APPROVED)

    def test_n_edl_none(self):
        with pytest.raises(EntityError):
            N_Value(edl=None, e_lux=200.0, e_external=20000.0, duct=10692.0, a_area=544.0, fd=0.7, CD_VALUE=3, state=STATE.APPROVED)

    def test_n_edl_not_float(self):
        with pytest.raises(EntityError):
            N_Value(edl=1, e_lux=200.0, e_external=20000.0, duct=10692.0, a_area=544.0, fd=0.7, CD_VALUE=3, state=STATE.APPROVED)

    def test_n_elux_none(self):
        with pytest.raises(EntityError):
            N_Value(edl=0.66, e_lux=None, e_external=20000.0, duct=10692.0, a_area=544.0, fd=0.7, CD_VALUE=3, state=STATE.APPROVED)

    def test_n_elux_not_float(self):
        with pytest.raises(EntityError):
            N_Value(edl=0.66, e_lux=1, e_external=20000.0, duct=10692.0, a_area=544.0, fd=0.7, CD_VALUE=3, state=STATE.APPROVED)

    def test_n_eexternal_none(self):
        with pytest.raises(EntityError):
            N_Value(edl=0.66, e_lux=200.0, e_external=None, duct=10692.0, a_area=544.0, fd=0.7, CD_VALUE=3, state=STATE.APPROVED)

    def test_n_eexternal_not_float(self):
        with pytest.raises(EntityError):
            N_Value(edl=0.66, e_lux=200.0, e_external=1, duct=10692.0, a_area=544.0, fd=0.7, CD_VALUE=3, state=STATE.APPROVED)

    def test_n_duct_none(self):
        with pytest.raises(EntityError):
            N_Value(edl=0.66, e_lux=200.0, e_external=20000.0, duct=None, a_area=544.0, fd=0.7, CD_VALUE=3, state=STATE.APPROVED)

    def test_n_duct_not_float(self):
        with pytest.raises(EntityError):
            N_Value(edl=0.66, e_lux=200.0, e_external=20000.0, duct=1, a_area=544.0, fd=0.7, CD_VALUE=3, state=STATE.APPROVED)

    def test_n_aarea_none(self):
        with pytest.raises(EntityError):
            N_Value(edl=0.66, e_lux=200.0, e_external=20000.0, duct=10692.0, a_area=None, fd=0.7, CD_VALUE=3, state=STATE.APPROVED)

    def test_n_aarea_not_float(self):
        with pytest.raises(EntityError):
            N_Value(edl=0.66, e_lux=200.0, e_external=20000.0, duct=10692.0, a_area=1, fd=0.7, CD_VALUE=3, state=STATE.APPROVED)

    def test_n_fd_none(self):
        with pytest.raises(EntityError):
            N_Value(edl=0.66, e_lux=200.0, e_external=20000.0, duct=10692.0, a_area=544.0, fd=None, CD_VALUE=3, state=STATE.APPROVED)

    def test_n_fd_not_float(self):
        with pytest.raises(EntityError):
            N_Value(edl=0.66, e_lux=200.0, e_external=20000.0, duct=10692.0, a_area=544.0, fd=1, CD_VALUE=3, state=STATE.APPROVED)

    def test_n_CD_none(self):
        with pytest.raises(EntityError):
            N_Value(edl=0.66, e_lux=200.0, e_external=20000.0, duct=10692.0, a_area=544.0, fd=0.7, CD_VALUE=None, state=STATE.APPROVED)

    def test_n_CD_not_int(self):
        with pytest.raises(EntityError):
            N_Value(edl=0.66, e_lux=200.0, e_external=20000.0, duct=10692.0, a_area=544.0, fd=0.7, CD_VALUE="1", state=STATE.APPROVED)

    def test_n_CD_diff_three(self):
        with pytest.raises(EntityError):
            N_Value(edl=0.66, e_lux=200.0, e_external=20000.0, duct=10692.0, a_area=544.0, fd=0.7, CD_VALUE=2, state=STATE.APPROVED)

    def test_n_state_is_not_state(self):
        with pytest.raises(EntityError):
            N_Value(edl=0.66, e_lux=200.0, e_external=20000.0, duct=10692.0, a_area=544.0, fd=0.7, CD_VALUE=3, state="APPROVED")