from src.shared.domain.entities.e_value import E_Value
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.e_value_repository_mock import EValueRepositoryMock
import pytest

class TestEValueRepositoryMock:
    def test_save_e_value(self):
        e_value = E_Value(e_id="f1cdc4ff-0606-4723-846e-0c4d132c99b9", n_value=10, b_section=0.9, edl_prcnt=66.0, e_external=20000.0, a_area=544.0, fd_value=0.7, cd_value=3.0)
        repo = EValueRepositoryMock()
        saved_value = repo.save_e_value(e_value)
        assert saved_value == e_value
        assert repo._e_values_db["f1cdc4ff-0606-4723-846e-0c4d132c99b9"] == e_value

    def test_save_e_value_duplicate_id(self):
        e_value = E_Value(e_id="f1cdc4ff-0606-4723-846e-0c4d132c99b9", n_value=10, edl_prcnt=66.0, b_section=0.9, e_external=20000.0, a_area=544.0, fd_value=0.7, cd_value=3.0)
        repo = EValueRepositoryMock()
        repo.save_e_value(e_value)
        # Attempt to save the same value again should raise ValueError
        e_value_duplicate = E_Value(e_id="f1cdc4ff-0606-4723-846e-0c4d132c99b9", n_value=1, edl_prcnt=65.0, b_section=0.9, e_external=2000.0, a_area=54.0, fd_value=0.1, cd_value=3.0)
        with pytest.raises(ValueError):
            repo.save_e_value(e_value_duplicate)

    def test_get_e_value_by_id(self):
        e_value = E_Value(e_id="f1cdc4ff-0606-4723-846e-0c4d132c99b9", n_value=10, edl_prcnt=66.0, b_section=0.9, e_external=20000.0, a_area=544.0, fd_value=0.7, cd_value=3.0)
        repo = EValueRepositoryMock()
        # Save the value first
        repo.save_e_value(e_value)
        # Retrieve the value by ID
        retrieved_value = repo.get_e_value_by_id("f1cdc4ff-0606-4723-846e-0c4d132c99b9")
        assert retrieved_value == e_value

    def test_get_e_value_by_id_not_found(self):
        e_value = E_Value(e_id="f1cdc4ff-0606-4723-846e-0c4d132c99b9", n_value=10, edl_prcnt=66.0, b_section=0.9, e_external=20000.0, a_area=544.0, fd_value=0.7, cd_value=3.0)
        repo = EValueRepositoryMock()
        # Save the value first
        repo.save_e_value(e_value)
        # Retrieve an inexistent ID value
        with pytest.raises(NoItemsFound):
            repo.get_e_value_by_id("non_existent_id")

    def test_calculate_e_value(self):
        repo = EValueRepositoryMock()
        e_value = E_Value(e_id="00000000-0000-0000-0000-000000000000", n_value=10, edl_prcnt=66.0, b_section=0.9, e_external=20000.0, a_area=544.0, fd_value=0.7, cd_value=3.0)
        calculated_value = repo.calculate_e_value(e_value)
        assert isinstance(calculated_value, float)

    def test_calculate_e_value_none(self):
        repo = EValueRepositoryMock()
        with pytest.raises(ValueError):
            repo.calculate_e_value(None)