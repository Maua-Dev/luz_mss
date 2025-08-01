from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse
from src.modules.calculate_n_value.app.calculate_n_value_presenter import CalculateNValuePresenter

class CalculateNValueController:
    def __init__(self, presenter: CalculateNValuePresenter):
        self.presenter = presenter

    def __call__(self, request: HttpRequest) -> HttpResponse:
        """
        Controller receive the HTTP request and delegates the handling to the presenter.
        """
        return self.presenter.handle(request)