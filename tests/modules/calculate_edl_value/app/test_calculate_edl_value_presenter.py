import pytest
import json
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse

from src.modules.calculate_edl_value.app.calculate_edl_value_presenter import lambda_handler

class TestCalculateEdlValuePresenter:

    def test_lambda_handler_calculate_edl_value_success(self):
        event = {
            "version": "2.0",
            "routeKey": "POST /calculate-edl",
            "rawPath": "/calculate-edl",
            "body": json.dumps({ # O corpo vem como uma string JSON
                'b_section': 0.9,
                'h_height': 6.0,
                'p_reflectance': 0.95
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
        assert json.loads(response['body']) == {"calculated_edl_value": 66.0}
        assert response['headers']['Content-Type'] == 'application/json'


    def test_lambda_handler_missing_b_section(self):
        event = {
            "version": "2.0",
            "routeKey": "POST /calculate-edl",
            "rawPath": "/calculate-edl",
            "body": json.dumps({
                'h_height': 2.0,
                'p_reflectance': 0.5
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
        assert json.loads(response['body']) == {"message": "Campo 'b_section' ausente."}


    def test_lambda_handler_invalid_body_json(self):
        event = {
            "version": "2.0",
            "routeKey": "POST /calculate-edl",
            "rawPath": "/calculate-edl",
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
        assert json.loads(response['body']) == {"message": "Campo 'b_section' ausente."}


    def test_lambda_handler_invalid_type_input(self):
        event = {
            "version": "2.0",
            "routeKey": "POST /calculate-edl",
            "rawPath": "/calculate-edl",
            "body": json.dumps({
                'b_section': 'abc',
                'h_height': 2.0,
                'p_reflectance': 0.5
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
            "routeKey": "POST /calculate-edl",
            "rawPath": "/calculate-edl",
            "body": json.dumps({
                'b_section': -1.0,
                'h_height': 2.0,
                'p_reflectance': 0.5
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
            "routeKey": "POST /calculate-edl",
            "rawPath": "/calculate-edl",
            "body": json.dumps({
                'b_section': 0.9,
                'h_height': 0.0,
                'p_reflectance': 0.95
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