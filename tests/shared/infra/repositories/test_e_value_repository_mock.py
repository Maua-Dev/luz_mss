from src.shared.domain.entities.e_value import E_Value
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.e_value_repository_mock import EValueRepositoryMock
import pytest

class TestEValueRepositoryMock:
    def test_save_e_value(self):
        e_value = E_Value(e_id=1, n_value=10, edl_prcnt=66.0, e_external=20000.0, a_area=544.0, fd_value=0.7)
        repo = EValueRepositoryMock()
        saved_value = repo.save_e_value(e_value)
        assert saved_value == e_value

    def test_get_e_value_by_id(self):
        e_value = E_Value(e_id=1, n_value=10, edl_prcnt=66.0, e_external=20000.0, a_area=544.0, fd_value=0.7)
        repo = EValueRepositoryMock(e_value)
        retrieved_value = repo.get_e_value_by_id(1)
        assert retrieved_value == e_value