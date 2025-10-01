from src.shared.domain.entities.edl_value import Edl_Value
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.edl_value_repository_mock import EdlValueRepositoryMock
import pytest

class TestEdlValueRepositoryMock:
    def test_save_edl_value(self):
        edl_value = Edl_Value(edl_id="9958b019-d6c6-4cc8-84c0-66d4527efd7e", b_section=0.9, h_height=6.0, p_reflectance=0.95)
        repo = EdlValueRepositoryMock()
        saved_value = repo.save_edl_value(edl_value)
        assert saved_value == edl_value
        assert repo._edl_values_db["9958b019-d6c6-4cc8-84c0-66d4527efd7e"] == edl_value

    def test_save_edl_value_duplicate_id(self):
        edl_value = Edl_Value(edl_id="9958b019-d6c6-4cc8-84c0-66d4527efd7e", b_section=0.9, h_height=6.0, p_reflectance=0.95)
        repo = EdlValueRepositoryMock()
        repo.save_edl_value(edl_value)
        # Attempt to save the same value again should raise ValueError
        edl_value_duplicate = Edl_Value(edl_id="9958b019-d6c6-4cc8-84c0-66d4527efd7e", b_section=0.1, h_height=4.0, p_reflectance=0.9)
        with pytest.raises(ValueError):
            repo.save_edl_value(edl_value_duplicate)

    def test_get_edl_value_by_id(self):
        edl_value = Edl_Value(edl_id="9958b019-d6c6-4cc8-84c0-66d4527efd7e", b_section=0.9, h_height=6.0, p_reflectance=0.95)
        repo = EdlValueRepositoryMock()
        # Save the value first
        repo.save_edl_value(edl_value)
        # Retrieve the value by ID
        retrieved_value = repo.get_edl_value_by_id("9958b019-d6c6-4cc8-84c0-66d4527efd7e")
        assert retrieved_value == edl_value

    def test_get_edl_value_by_id_not_found(self):
        edl_value = Edl_Value(edl_id="9958b019-d6c6-4cc8-84c0-66d4527efd7e", b_section=0.9, h_height=6.0, p_reflectance=0.95)
        repo = EdlValueRepositoryMock()
        # Save the value first
        repo.save_edl_value(edl_value)
        # Retrieve an inexistent ID value
        with pytest.raises(NoItemsFound):
            repo.get_edl_value_by_id("non_existent_id")
        

    def test_calculate_edl_value(self):
        repo = EdlValueRepositoryMock()
        edl_value = Edl_Value(edl_id="00000000-0000-0000-0000-000000000000", b_section=0.9, h_height=6.0, p_reflectance=0.95)
        calculated_value = repo.calculate_edl_value(edl_value)
        assert isinstance(calculated_value, int)

    def test_calculate_edl_value_none(self):
        repo = EdlValueRepositoryMock()
        with pytest.raises(ValueError):
            repo.calculate_edl_value(None)