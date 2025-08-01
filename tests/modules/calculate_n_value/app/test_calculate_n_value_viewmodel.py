from src.modules.calculate_n_value.app.calculate_n_value_viewmodel import CalculateNValueViewModel
import pytest

class TestCalculateNValueViewModel:

    def test_to_dict(self):
        calculated_value = 66.0
        viewmodel = CalculateNValueViewModel(calculated_value=calculated_value)

        result_dict = viewmodel.to_dict()

        assert isinstance(result_dict, dict)
        assert "calculated_n_value" in result_dict
        assert result_dict["calculated_n_value"] == calculated_value