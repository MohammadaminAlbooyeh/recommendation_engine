class TestApiEndpoints:
    def test_read_root(self, client):
        response = client.get("/")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "status" in data

    def test_read_items(self, client, sample_items):
        response = client.get("/items")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 5

    def test_create_rating(self, client, sample_users, sample_items):
        response = client.post("/ratings", json={
            "user_id": sample_users[0].id,
            "item_id": sample_items[0].id,
            "rating": 4.5
        })
        assert response.status_code == 200
        data = response.json()
        assert data["rating"] == 4.5
        assert data["user_id"] == sample_users[0].id
        assert data["item_id"] == sample_items[0].id
        assert "id" in data
        assert "timestamp" in data

    def test_get_recommendations(self, client, sample_ratings):
        user_id = sample_ratings[0].user_id
        response = client.get(f"/recommendations/{user_id}")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)

    def test_get_recommendations_no_ratings(self, client):
        response = client.get("/recommendations/1")
        assert response.status_code == 200
        data = response.json()
        assert data == []
