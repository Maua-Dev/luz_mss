from typing import Dict, Any

class CalculateEValueViewModel:
    def __init__(self, calculated_value: float):
        self.calculated_value = calculated_value

    def to_dict(self) -> Dict[str, Any]:
        return {
            "calculated_e_value": self.calculated_value
        }