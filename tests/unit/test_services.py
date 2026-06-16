from unittest.mock import MagicMock, patch
from backend.services.recommendation_service import get_top_n_recommendations

class TestRecommendationService:
    @patch('backend.services.recommendation_service.MatrixFactorization')
    def test_get_top_n_recommendations_returns_items(self, mock_mf_cls):
        mock_db = MagicMock()
        mock_rating1 = MagicMock()
        mock_rating1.user_id = 1
        mock_rating1.item_id = 1
        mock_rating1.rating = 5.0
        mock_rating2 = MagicMock()
        mock_rating2.user_id = 1
        mock_rating2.item_id = 2
        mock_rating2.rating = 3.0
        mock_db.query.return_value.all.return_value = [mock_rating1, mock_rating2]
        mock_model = MagicMock()
        mock_mf_cls.return_value = mock_model
        mock_model.recommend.return_value = [1, 2]
        mock_item1 = MagicMock()
        mock_item1.id = 1
        mock_item2 = MagicMock()
        mock_item2.id = 2
        mock_db.query.return_value.filter.return_value.all.return_value = [mock_item1, mock_item2]
        result = get_top_n_recommendations(1, 5, mock_db)
        assert len(result) == 2
        assert result == [mock_item1, mock_item2]

    def test_get_top_n_recommendations_empty_ratings(self):
        mock_db = MagicMock()
        mock_db.query.return_value.all.return_value = []
        result = get_top_n_recommendations(1, 5, mock_db)
        assert result == []

    @patch('backend.services.recommendation_service.MatrixFactorization')
    def test_get_top_n_recommendations_invalid_user(self, mock_mf_cls):
        mock_db = MagicMock()
        mock_rating1 = MagicMock()
        mock_rating1.user_id = 1
        mock_rating1.item_id = 1
        mock_rating1.rating = 5.0
        mock_db.query.return_value.all.return_value = [mock_rating1]
        mock_model = MagicMock()
        mock_mf_cls.return_value = mock_model
        mock_model.recommend.return_value = []
        mock_db.query.return_value.filter.return_value.all.return_value = []
        result = get_top_n_recommendations(999, 5, mock_db)
        assert result == []
