from src.shared.domain.entities.n_value import N_Value
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.n_value_repository_mock import NValueRepositoryMock
import pytest

class Test_NValueRepositoryMock:
    def test_save_n_value(self):
        n_value = N_Value(n_id="29d2fabd-5bc9-4db7-b372-2eadca80af87", edl_prcnt=66.0, b_section=0.9, e_lux=200, e_external=20000.0, a_area=544.0, fd_value=0.7)
        repo = NValueRepositoryMock()
        saved_value = repo.save_n_value(n_value)
        assert saved_value == n_value

    def test_get_n_value_by_id(self):
        n_value = N_Value(n_id="29d2fabd-5bc9-4db7-b372-2eadca80af87",  edl_prcnt=66.0, b_section=0.9, e_lux=200, e_external=20000.0, a_area=544.0, fd_value=0.7)
        repo = NValueRepositoryMock(n_value)
        retrieved_value = repo.get_n_value_by_id("29d2fabd-5bc9-4db7-b372-2eadca80af87")
        assert retrieved_value == n_value