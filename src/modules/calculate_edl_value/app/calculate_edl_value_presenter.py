from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse
from src.modules.calculate_edl_value.app.calculate_edl_value_controller import CalculateEdlValueController
# from src.modules.calculate_edl_value.app.calculate_edl_value_presenter import CalculateEdlValuePresenter
from src.modules.calculate_edl_value.app.calculate_edl_value_usecase import CalculateEdlValueUseCase

# --- Instantiation of Dependencies ---
repo = Environments.get_edl_value_repo()() 

usecase = CalculateEdlValueUseCase(repo)
controller = CalculateEdlValueController(usecase)

# --- Lambda Handler Function ---
def lambda_handler(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(request=httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()