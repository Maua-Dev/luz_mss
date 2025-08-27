from src.shared.domain.entities.n_value import N_Value
from src.shared.helpers.errors.domain_errors import EntityError
import pytest

class Test_N_Value:
    def test_n(self):
        N_Value(n_id="29d2fabd-5bc9-4db7-b372-2eadca80af87", edl_prcnt=50.0, b_section=0.5, e_lux=200, e_external=20000.0, a_area=544.0, fd_value=0.7, cd_value=3.0)

    def test_n_edl_prcnt_none(self):
        with pytest.raises(EntityError):
            N_Value(n_id="29d2fabd-5bc9-4db7-b372-2eadca80af87", edl_prcnt=None, b_section=0.5, e_lux=200, e_external=20000.0, a_area=544.0, fd_value=0.7, cd_value=3.0)

    def test_n_edl_prcnt_not_float(self):
        with pytest.raises(EntityError):
            N_Value(n_id="29d2fabd-5bc9-4db7-b372-2eadca80af87", edl_prcnt=1, b_section=0.5, e_lux=200, e_external=20000.0, a_area=544.0, fd_value=0.7, cd_value=3.0)

    def test_n_bsection_none(self):
        with pytest.raises(EntityError):
            N_Value(n_id="29d2fabd-5bc9-4db7-b372-2eadca80af87", edl_prcnt=50.0, b_section=None, e_lux=200, e_external=20000.0, a_area=544.0, fd_value=0.7, cd_value=3.0)

    def test_n_bsection_not_float(self):
        with pytest.raises(EntityError):
            N_Value(n_id="29d2fabd-5bc9-4db7-b372-2eadca80af87", edl_prcnt=50.0, b_section=1, e_lux=200, e_external=20000.0, a_area=544.0, fd_value=0.7, cd_value=3.0)

    def test_n_elux_none(self):
        with pytest.raises(EntityError):
            N_Value(n_id="29d2fabd-5bc9-4db7-b372-2eadca80af87", edl_prcnt=50.0, b_section=0.5, e_lux=None, e_external=20000.0, a_area=544.0, fd_value=0.7, cd_value=3.0)

    def test_n_elux_not_int(self):
        with pytest.raises(EntityError):
            N_Value(n_id="29d2fabd-5bc9-4db7-b372-2eadca80af87", edl_prcnt=50.0, b_section=0.5, e_lux=1.5, e_external=20000.0, a_area=544.0, fd_value=0.7, cd_value=3.0)

    def test_n_eexternal_none(self):
        with pytest.raises(EntityError):
            N_Value(n_id="29d2fabd-5bc9-4db7-b372-2eadca80af87", edl_prcnt=50.0, b_section=0.5, e_lux=200, e_external=None, a_area=544.0, fd_value=0.7, cd_value=3.0)

    def test_n_eexternal_not_float(self):
        with pytest.raises(EntityError):
            N_Value(n_id="29d2fabd-5bc9-4db7-b372-2eadca80af87", edl_prcnt=50.0, b_section=0.5, e_lux=200, e_external=1, a_area=544.0, fd_value=0.7, cd_value=3.0)

    def test_n_aarea_none(self):
        with pytest.raises(EntityError):
            N_Value(n_id="29d2fabd-5bc9-4db7-b372-2eadca80af87", edl_prcnt=50.0, b_section=0.5, e_lux=200, e_external=20000.0, a_area=None, fd_value=0.7, cd_value=3.0)

    def test_n_aarea_not_float(self):
        with pytest.raises(EntityError):
            N_Value(n_id="29d2fabd-5bc9-4db7-b372-2eadca80af87", edl_prcnt=50.0, b_section=0.5, e_lux=200, e_external=20000.0, a_area=1, fd_value=0.7, cd_value=3.0)

    def test_n_fdvalue_none(self):
        with pytest.raises(EntityError):
            N_Value(n_id="29d2fabd-5bc9-4db7-b372-2eadca80af87", edl_prcnt=50.0, b_section=0.5, e_lux=200, e_external=20000.0, a_area=544.0, fd_value=None, cd_value=3.0)

    def test_n_fdvalue_not_float(self):
        with pytest.raises(EntityError):
            N_Value(n_id="29d2fabd-5bc9-4db7-b372-2eadca80af87", edl_prcnt=50.0, b_section=0.5, e_lux=200, e_external=20000.0, a_area=544.0, fd_value=1, cd_value=3.0)

    def test_n_cdvalue_none(self):
        with pytest.raises(EntityError):
            N_Value(n_id="29d2fabd-5bc9-4db7-b372-2eadca80af87", edl_prcnt=50.0, b_section=0.5, e_lux=200, e_external=20000.0, a_area=544.0, fd_value=0.7, cd_value=None)

    def test_n_cdvalue_not_float(self):
        with pytest.raises(EntityError):
            N_Value(n_id="29d2fabd-5bc9-4db7-b372-2eadca80af87", edl_prcnt=50.0, b_section=0.5, e_lux=200, e_external=20000.0, a_area=544.0, fd_value=0.7, cd_value=1)

    def test_n_id_not_str(self):
        with pytest.raises(EntityError):
            N_Value(n_id=123, edl_prcnt=50.0, b_section=0.5, e_lux=200, e_external=20000.0, a_area=544.0, fd_value=0.7, cd_value=3.0)

    def test_n_id_invalid_uuid(self):
        with pytest.raises(EntityError):
            N_Value(n_id="invalid-uuid", edl_prcnt=50.0, b_section=0.5, e_lux=200, e_external=20000.0, a_area=544.0, fd_value=0.7, cd_value=3.0)