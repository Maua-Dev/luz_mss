from src.shared.helpers.external_interfaces.http_models import HttpRequest, HttpResponse
from src.modules.calculate_edl_value.app.calculate_edl_value_presenter import CalculateEdlValuePresenter

class CalculateEdlValueController:
    def __init__(self, presenter: CalculateEdlValuePresenter):
        self.presenter = presenter

    def __call__(self, request: HttpRequest) -> HttpResponse:
        """
        Controller recieve the HTTP request and delegates the handling to the presenter.
        """
        return self.presenter.handle(request)