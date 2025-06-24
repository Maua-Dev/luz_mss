from src.shared.domain.entities.n_value import N_Value
from src.shared.helpers.errors.domain_errors import EntityError
import pytest

class Test_N_Value:
    def test_n(self):
        N_Value(e_lux=200.0, e_external=20000.0, a_area=544.0, fd=0.7, cd_value=3.0)

    def test_n_elux_none(self):
        with pytest.raises(EntityError):
            N_Value(e_lux=None, e_external=20000.0, a_area=544.0, fd=0.7, cd_value=3.0)

    def test_n_elux_not_float(self):
        with pytest.raises(EntityError):
            N_Value(e_lux=1, e_external=20000.0, a_area=544.0, fd=0.7, cd_value=3.0)

    def test_n_eexternal_none(self):
        with pytest.raises(EntityError):
            N_Value(e_lux=200.0, e_external=None, a_area=544.0, fd=0.7, cd_value=3.0)

    def test_n_eexternal_not_float(self):
        with pytest.raises(EntityError):
            N_Value(e_lux=200.0, e_external=1, a_area=544.0, fd=0.7, cd_value=3.0)

    def test_n_aarea_none(self):
        with pytest.raises(EntityError):
            N_Value(e_lux=200.0, e_external=20000.0, a_area=None, fd=0.7, cd_value=3.0)

    def test_n_aarea_not_float(self):
        with pytest.raises(EntityError):
            N_Value(e_lux=200.0, e_external=20000.0, a_area=1, fd=0.7, cd_value=3.0)

    def test_n_fd_none(self):
        with pytest.raises(EntityError):
            N_Value(e_lux=200.0, e_external=20000.0, a_area=544.0, fd=None, cd_value=3.0)

    def test_n_fd_not_float(self):
        with pytest.raises(EntityError):
            N_Value(e_lux=200.0, e_external=20000.0, a_area=544.0, fd=1, cd_value=3.0)

    def test_n_CD_none(self):
        with pytest.raises(EntityError):
            N_Value(e_lux=200.0, e_external=20000.0, a_area=544.0, fd=0.7, cd_value=None)

    def test_n_CD_not_float(self):
        with pytest.raises(EntityError):
            N_Value(e_lux=200.0, e_external=20000.0, a_area=544.0, fd=0.7, cd_value="1")