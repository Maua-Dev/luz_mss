from src.modules.calculate_e_value.app.calculate_e_value_viewmodel import CalculateEValueViewModel
import pytest

class TestCalculateEValueViewModel:

    def test_to_dict(self):
        calculated_value = 413.0
        viewmodel = CalculateEValueViewModel(calculated_value=calculated_value)

        result_dict = viewmodel.to_dict()

        assert isinstance(result_dict, dict)
        assert "calculated_e_value" in result_dict
        assert result_dict["calculated_e_value"] == calculated_value