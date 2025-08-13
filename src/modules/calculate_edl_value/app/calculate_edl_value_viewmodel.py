from typing import Dict, Any

class CalculateEdlValueViewModel:
    def __init__(self, calculated_value: float):
        self.calculated_value = calculated_value

    def to_dict(self) -> Dict[str, Any]:
        # Convert ViewModel to a JSON serializable dictionary
        return {
            "calculated_edl_value": self.calculated_value
        }