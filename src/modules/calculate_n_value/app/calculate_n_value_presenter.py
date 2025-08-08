from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from .calculate_n_value_controller import CalculateNValueController
from .calculate_n_value_usecase import CalculateNValueUseCase

# --- Instantiation of Dependencies ---
repo = Environments.get_n_value_repo()() 

usecase = CalculateNValueUseCase(repo)
controller = CalculateNValueController(usecase)

# --- Lambda Handler Function ---
def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(request=httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()
