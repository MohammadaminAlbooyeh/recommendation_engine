class TestEndToEnd:
    def test_full_workflow(self, client, sample_users, sample_items):
        for user in sample_users:
            for item in sample_items[:3]:
                resp = client.post("/ratings", json={
                    "user_id": user.id,
                    "item_id": item.id,
                    "rating": 4.0
                })
                assert resp.status_code == 200
        items_resp = client.get("/items")
        assert items_resp.status_code == 200
        assert len(items_resp.json()) == 5
        user_id = sample_users[0].id
        recs_resp = client.get(f"/recommendations/{user_id}")
        assert recs_resp.status_code == 200
        recs = recs_resp.json()
        assert isinstance(recs, list)
        for rec in recs:
            assert "id" in rec
            assert "title" in rec
