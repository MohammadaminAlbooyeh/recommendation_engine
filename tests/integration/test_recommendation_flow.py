class TestRecommendationFlow:
    def test_recommendation_after_ratings(self, client, sample_ratings):
        user_id = sample_ratings[0].user_id
        response = client.get(f"/recommendations/{user_id}")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)

    def test_recommendation_for_new_user(self, client, sample_ratings):
        response = client.get("/recommendations/999")
        assert response.status_code == 200
        data = response.json()
        assert data == []

    def test_recommendation_limit(self, client, sample_ratings):
        user_id = sample_ratings[0].user_id
        response = client.get(f"/recommendations/{user_id}?n=3")
        assert response.status_code == 200
        data = response.json()
        assert len(data) <= 3
