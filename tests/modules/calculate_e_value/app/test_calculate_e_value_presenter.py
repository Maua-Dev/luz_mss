import pytest
import json
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

from src.modules.calculate_e_value.app.calculate_e_value_presenter import lambda_handler

class TestCalculateEValuePresenter:
    def test_lambda_handler_calculate_e_value_success(self):
        event = {
            "version": "2.0",
            "routeKey": "POST /calculate-e",
            "rawPath": "/calculate-e",
            "body": json.dumps({
                "n_value": 10,
                "edl_prcnt": 66.0,
                "b_section": 0.9,
                "e_external": 20000.0,
                "a_area": 544.0,
                "fd_value": 0.7
            }),
            "headers": {
                "content-type": "application/json"
            },
            "requestContext": {
                "http": {
                    "method": "POST"
                }
            },
            "isBase64Encoded": False
        }
        context = {}

        response = lambda_handler(event, context)

        assert response['statusCode'] == 200
        assert json.loads(response['body']) == {"calculated_e_value": 413.0}
        assert response['headers']['Content-Type'] == 'application/json'


    def test_lambda_handler_missing_b_section(self):
        event = {
            "version": "2.0",
            "routeKey": "POST /calculate-n",
            "rawPath": "/calculate-n",
            "body": json.dumps({
                "n_value": 10,
                "edl_prcnt": 66.0,
                "e_external": 20000.0,
                "a_area": 544.0,
                "fd_value": 0.7
            }),
            "headers": {
                "content-type": "application/json"
            },
            "requestContext": { "http": { "method": "POST" } },
            "isBase64Encoded": False
        }
        context = {}

        response = lambda_handler(event, context)

        assert response['statusCode'] == 400
        assert json.loads(response['body']) == {"message": "Campo 'b_section' ausente ou inválido."}


    def test_lambda_handler_invalid_body_json(self):
        event = {
            "version": "2.0",
            "routeKey": "POST /calculate-n",
            "rawPath": "/calculate-n",
            "body": "isso não é um json {invalido",
            "headers": {
                "content-type": "application/json"
            },
            "requestContext": { "http": { "method": "POST" } },
            "isBase64Encoded": False
        }
        context = {}

        response = lambda_handler(event, context)

        assert response['statusCode'] == 400
        assert json.loads(response['body']) == {"message": "Campo 'n_value' ausente ou inválido."}


    def test_lambda_handler_invalid_type_input(self):
        event = {
            "version": "2.0",
            "routeKey": "POST /calculate-n",
            "rawPath": "/calculate-n",
            "body": json.dumps({
                "n_value": 10,
                "edl_prcnt": 66.0,
                "b_section": "invalid_type",
                "e_external": 20000.0,
                "a_area": 544.0,
                "fd_value": 0.7
            }),
            "headers": {
                "content-type": "application/json"
            },
            "requestContext": { "http": { "method": "POST" } },
            "isBase64Encoded": False
        }
        context = {}

        response = lambda_handler(event, context)

        assert response['statusCode'] == 400
        assert "Erro de tipo de dados" in json.loads(response['body'])['message']


    def test_lambda_handler_domain_error(self):
        event = {
            "version": "2.0",
            "routeKey": "POST /calculate-n",
            "rawPath": "/calculate-n",
            "body": json.dumps({
                "n_value": 10,
                "edl_prcnt": 66.0,
                "b_section": -0.9,
                "e_external": 20000.0,
                "a_area": 544.0,
                "fd_value": 0.7
            }),
            "headers": {
                "content-type": "application/json"
            },
            "requestContext": { "http": { "method": "POST" } },
            "isBase64Encoded": False
        }
        context = {}

        response = lambda_handler(event, context)

        assert response['statusCode'] == 400
        assert json.loads(response['body']) == {"message": "Campo 'b_section' deve ser um número positivo."}


    def test_lambda_handler_internal_server_error(self):
        event = {
            "version": "2.0",
            "routeKey": "POST /calculate-n",
            "rawPath": "/calculate-n",
            "body": json.dumps({
                "n_value": 10,
                "edl_prcnt": 66.0,
                "b_section": 0.9,
                "e_external": 20000.0,
                "a_area": 544.0,
                "fd_value": 0.0
            }),
            "headers": {
                "content-type": "application/json"
            },
            "requestContext": { "http": { "method": "POST" } },
            "isBase64Encoded": False
        }
        context = {}

        response = lambda_handler(event, context)

        assert response['statusCode'] == 500
        assert "Erro interno do servidor:" in json.loads(response['body'])['message']