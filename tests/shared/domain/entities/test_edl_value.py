from src.shared.domain.entities.edl_value import Edl_Value
from src.shared.helpers.errors.domain_errors import EntityError
import pytest

class Test_Edl_Value:
    def test_edl(self):
        Edl_Value(edl_id="ed871dcc-d6c2-4296-b3dc-df086bf90902", b_section=0.9, h_height=6.0, p_reflectance=0.95)

    def test_edl_b_none(self):
        with pytest.raises(EntityError):
            Edl_Value(edl_id="ed871dcc-d6c2-4296-b3dc-df086bf90902", b_section=None, h_height=6, p_reflectance=0.95)

    def test_edl_b_not_float(self):
        with pytest.raises(EntityError):
            Edl_Value(edl_id="ed871dcc-d6c2-4296-b3dc-df086bf90902", b_section="1", h_height=6, p_reflectance=0.95)

    def test_edl_h_none(self):
        with pytest.raises(EntityError):
            Edl_Value(edl_id="ed871dcc-d6c2-4296-b3dc-df086bf90902", b_section=0.9, h_height=None, p_reflectance=0.95)

    def test_edl_h_not_float(self):
        with pytest.raises(EntityError):
            Edl_Value(edl_id="ed871dcc-d6c2-4296-b3dc-df086bf90902", b_section=0.9, h_height="6", p_reflectance=0.95)

    def test_edl_p_none(self):
        with pytest.raises(EntityError):
            Edl_Value(edl_id="ed871dcc-d6c2-4296-b3dc-df086bf90902", b_section=0.9, h_height=6, p_reflectance=None)

    def test_edl_p_not_float(self):
        with pytest.raises(EntityError):
            Edl_Value(edl_id="ed871dcc-d6c2-4296-b3dc-df086bf90902", b_section=0.9, h_height=6, p_reflectance="1")

    def test_edl_id_not_str(self):
        with pytest.raises(EntityError):
            Edl_Value(edl_id=123, b_section=0.9, h_height=6, p_reflectance=0.95)

    def test_edl_id_invalid_uuid(self):
        with pytest.raises(EntityError):
            Edl_Value(edl_id="invalid-uuid", b_section=0.9, h_height=6, p_reflectance=0.95)