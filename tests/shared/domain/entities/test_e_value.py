from src.shared.domain.entities.e_value import E_Value
from src.shared.helpers.errors.domain_errors import EntityError
import pytest

class Test_E_Value:
    def test_e(self):
        E_Value(e_id="f1cdc4ff-0606-4723-846e-0c4d132c99b9", n_value=10, edl_prcnt=66.0, b_section=0.9, e_external=20000.0, a_area=544.0, fd_value=0.7)

    def test_e_nvalue_none(self):
        with pytest.raises(EntityError):
            E_Value(e_id="f1cdc4ff-0606-4723-846e-0c4d132c99b9", n_value=None, edl_prcnt=66.0, b_section=0.9, e_external=20000.0, a_area=544.0, fd_value=0.7)

    def test_e_nvalue_not_int(self):
        with pytest.raises(EntityError):
            E_Value(e_id="f1cdc4ff-0606-4723-846e-0c4d132c99b9", n_value=1.5, edl_prcnt=66.0, b_section=0.9, e_external=20000.0, a_area=544.0, fd_value=0.7)

    def test_e_edl_prcnt_none(self):
        with pytest.raises(EntityError):
            E_Value(e_id="f1cdc4ff-0606-4723-846e-0c4d132c99b9", n_value=10, edl_prcnt=None, b_section=0.9, e_external=20000.0, a_area=544.0, fd_value=0.7)

    def test_e_edl_prcnt_not_float(self):
        with pytest.raises(EntityError):
            E_Value(e_id="f1cdc4ff-0606-4723-846e-0c4d132c99b9", n_value=10, edl_prcnt=50, b_section=0.9, e_external=20000.0, a_area=544.0, fd_value=0.7)

    def test_e_edl_prcnt_out_of_range(self):
        with pytest.raises(EntityError):
            E_Value(e_id="f1cdc4ff-0606-4723-846e-0c4d132c99b9", n_value=10, edl_prcnt=-1.0, b_section=0.9, e_external=20000.0, a_area=544.0, fd_value=0.7)
        with pytest.raises(EntityError):
            E_Value(e_id="f1cdc4ff-0606-4723-846e-0c4d132c99b9", n_value=10, edl_prcnt=101.0, b_section=0.9, e_external=20000.0, a_area=544.0, fd_value=0.7)

    def test_e_b_section_none(self):
        with pytest.raises(EntityError):
            E_Value(e_id="f1cdc4ff-0606-4723-846e-0c4d132c99b9", n_value=10, edl_prcnt=66.0, b_section=None, e_external=20000.0, a_area=544.0, fd_value=0.7)

    def test_e_b_section_not_float(self):
        with pytest.raises(EntityError):
            E_Value(e_id="f1cdc4ff-0606-4723-846e-0c4d132c99b9", n_value=10, edl_prcnt=66.0, b_section="0.9", e_external=20000.0, a_area=544.0, fd_value=0.7)

    def test_e_eexternal_none(self):
        with pytest.raises(EntityError):
            E_Value(e_id="f1cdc4ff-0606-4723-846e-0c4d132c99b9", n_value=10, edl_prcnt=66.0,  b_section=0.9, e_external=None, a_area=544.0, fd_value=0.7)

    def test_e_eexternal_not_float(self):
        with pytest.raises(EntityError):
            E_Value(e_id="f1cdc4ff-0606-4723-846e-0c4d132c99b9", n_value=10, edl_prcnt=66.0,  b_section=0.9, e_external="20000", a_area=544.0, fd_value=0.7)

    def test_e_aarea_none(self):
        with pytest.raises(EntityError):
            E_Value(e_id="f1cdc4ff-0606-4723-846e-0c4d132c99b9", n_value=10, edl_prcnt=66.0,  b_section=0.9, e_external=20000.0, a_area=None, fd_value=0.7)

    def test_e_aarea_not_float(self):
        with pytest.raises(EntityError):
            E_Value(e_id="f1cdc4ff-0606-4723-846e-0c4d132c99b9", n_value=10, edl_prcnt=66.0,  b_section=0.9, e_external=20000.0, a_area="544", fd_value=0.7)

    def test_e_fdvalue_none(self):
        with pytest.raises(EntityError):
            E_Value(e_id="f1cdc4ff-0606-4723-846e-0c4d132c99b9", n_value=10, edl_prcnt=66.0,  b_section=0.9, e_external=20000.0, a_area=544.0, fd_value=None)

    def test_e_fdvalue_not_float(self):
        with pytest.raises(EntityError):
            E_Value(e_id="f1cdc4ff-0606-4723-846e-0c4d132c99b9", n_value=10, edl_prcnt=66.0,  b_section=0.9, e_external=20000.0, a_area=544.0, fd_value="0.7")

    def test_e_fdvalue_equals_zero(self):
        with pytest.raises(EntityError):
            E_Value(e_id="f1cdc4ff-0606-4723-846e-0c4d132c99b9", n_value=10, edl_prcnt=66.0,  b_section=0.9, e_external=20000.0, a_area=544.0, fd_value=0.0)

    def test_e_id_not_str(self):
        with pytest.raises(EntityError):
            E_Value(e_id=123, n_value=10, edl_prcnt=66.0,  b_section=0.9, e_external=20000.0, a_area=544.0, fd_value=0.7)

    def test_e_id_invalid_uuid(self):
        with pytest.raises(EntityError):
            E_Value(e_id="invalid-uuid", n_value=10, edl_prcnt=66.0,  b_section=0.9, e_external=20000.0, a_area=544.0, fd_value=0.7)