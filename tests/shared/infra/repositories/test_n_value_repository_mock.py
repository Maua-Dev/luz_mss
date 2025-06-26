from src.shared.domain.entities.n_value import N_Value
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.n_value_repository_mock import NValueRepositoryMock
import pytest

class Test_NValueRepositoryMock:
    def test_n_repository_mock(self):
        custom_e_lux = 100.0
        custom_e_external = 10000
        custom_a_area = 400
        custom_fd = 1.0

        n_repo_mock = NValueRepositoryMock(
            e_lux = custom_e_lux,
            e_external = custom_e_external,
            a_area = custom_a_area,
            fd = custom_fd
        )

        retrieved_n_entity = n_repo_mock.get_n_parameters()

        assert retrieved_n_entity.e_lux == custom_e_lux
        assert retrieved_n_entity.e_external == custom_e_external
        assert retrieved_n_entity.a_area == custom_a_area
        assert retrieved_n_entity.fd == custom_fd

    def test_n_repository_mock_default_parameters(self):
        n_repo_mock = nValueRepositoryMock()
        retrieved_n_entity = n_repo_mock.get_n_parameters()
        
        assert retrieved_n_entity.e_lux == 200.0
        assert retrieved_n_entity.h_height == 20000.0
        assert retrieved_n_entity.a_area == 544.0
        assert retrieved_n_entity.fd == 0.7