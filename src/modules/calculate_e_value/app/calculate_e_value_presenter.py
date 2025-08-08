from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from .calculate_e_value_controller import CalculateEValueController
from .calculate_e_value_usecase import CalculateEValueUseCase

# --- Instantiation of Dependencies ---
repo = Environments.get_e_value_repo()() 

usecase = CalculateEValueUseCase(repo)
controller = CalculateEValueController(usecase)

# --- Lambda Handler Function ---
def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(request=httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()