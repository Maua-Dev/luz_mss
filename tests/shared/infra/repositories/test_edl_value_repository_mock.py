from src.shared.domain.entities.edl_value import Edl_Value
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.infra.repositories.edl_value_repository_mock import EdlValueRepositoryMock
import pytest

class TestEdlValueRepositoryMock:
    def test_save_edl_value(self):
        edl_value = Edl_Value(edl_id=1, b_section=0.9, h_height=6.0, p_reflectance=0.95)
        repo = EdlValueRepositoryMock()
        saved_value = repo.save_edl_value(edl_value)
        assert saved_value == edl_value

    def test_get_edl_value_by_id(self):
        edl_value = Edl_Value(edl_id=1, b_section=0.9, h_height=6.0, p_reflectance=0.95)
        repo = EdlValueRepositoryMock(edl_value)
        retrieved_value = repo.get_edl_value_by_id(1)
        assert retrieved_value == edl_value