from src.modules.calculate_edl_value.app.calculate_edl_value_viewmodel import CalculateEdlValueViewModel
import pytest

class TestCalculateEdlValueViewModel:

    def test_to_dict(self):
        # Create an instance of the ViewModel with a sample calculated value
        calculated_value = 66.0
        viewmodel = CalculateEdlValueViewModel(calculated_value=calculated_value)

        # Convert the ViewModel to a dictionary
        result_dict = viewmodel.to_dict()

        # Assert that the dictionary contains the expected key and value
        assert isinstance(result_dict, dict)
        assert "calculated_edl_value" in result_dict
        assert result_dict["calculated_edl_value"] == calculated_value