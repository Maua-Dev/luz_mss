from src.shared.domain.entities.edl_value import Edl_Value
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.edl_value_repository_mock import EdlValueRepositoryMock
import pytest

class Test_EdlValueRepositoryMock:
    def test_edl_repository_mock(self):
        # Instancia o mock, injetando os valores que você quer que ele retorne para este teste
        custom_b_section = 1.0
        custom_h_height = 2.0
        custom_p_reflectance = 0.5
        
        edl_repo_mock = EdlValueRepositoryMock(
            b_section = custom_b_section,
            h_height = custom_h_height,
            p_reflectance = custom_p_reflectance
        )

        # O caso de uso (ou o código que usa o repositório) chamaria get_edl_parameters
        retrieved_edl_entity = edl_repo_mock.get_edl_parameters()

        assert retrieved_edl_entity.b_section == custom_b_section
        assert retrieved_edl_entity.h_height == custom_h_height
        assert retrieved_edl_entity.p_reflectance == custom_p_reflectance

    def test_edl_repository_mock_default_parameters(self):
        edl_repo_mock = EdlValueRepositoryMock()
        retrieved_edl_entity = edl_repo_mock.get_edl_parameters()
        
        # Verifica se são os valores padrão (0.9, 6.0, 0.95)
        assert retrieved_edl_entity.b_section == 0.9
        assert retrieved_edl_entity.h_height == 6.0
        assert retrieved_edl_entity.p_reflectance == 0.95
