import time
from unittest.mock import MagicMock, patch

class TestPerformance:
    @patch('backend.services.recommendation_service.MatrixFactorization')
    def test_response_time(self, mock_mf_cls):
        mock_db = MagicMock()
        mock_rating = MagicMock()
        mock_rating.user_id = 1
        mock_rating.item_id = 1
        mock_rating.rating = 5.0
        mock_db.query.return_value.all.return_value = [mock_rating] * 1000
        mock_model = MagicMock()
        mock_mf_cls.return_value = mock_model
        mock_model.recommend.return_value = list(range(10))
        mock_item = MagicMock()
        mock_item.id = 1
        mock_db.query.return_value.filter.return_value.all.return_value = [mock_item] * 10
        from backend.services.recommendation_service import get_top_n_recommendations
        start = time.time()
        result = get_top_n_recommendations(1, 10, mock_db)
        elapsed = time.time() - start
        assert len(result) == 10
        assert elapsed < 2.0
