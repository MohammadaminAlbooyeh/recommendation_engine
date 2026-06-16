class TestRatingFlow:
    def test_create_and_retrieve_rating(self, client, sample_users, sample_items):
        create_resp = client.post("/ratings", json={
            "user_id": sample_users[0].id,
            "item_id": sample_items[0].id,
            "rating": 3.5
        })
        assert create_resp.status_code == 200
        created = create_resp.json()
        assert created["rating"] == 3.5
        assert created["user_id"] == sample_users[0].id
        assert created["item_id"] == sample_items[0].id
        items_resp = client.get("/items")
        assert items_resp.status_code == 200

    def test_multiple_ratings(self, client, sample_users, sample_items):
        for i, user in enumerate(sample_users):
            for j, item in enumerate(sample_items):
                resp = client.post("/ratings", json={
                    "user_id": user.id,
                    "item_id": item.id,
                    "rating": float((i + j) % 5 + 1)
                })
                assert resp.status_code == 200
        items_resp = client.get("/items")
        assert len(items_resp.json()) == 5

    def test_invalid_rating_values(self, client, sample_users, sample_items):
        resp = client.post("/ratings", json={
            "user_id": 999,
            "item_id": sample_items[0].id,
            "rating": 5.0
        })
        assert resp.status_code == 200
