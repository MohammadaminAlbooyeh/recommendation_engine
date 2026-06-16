class TestSearchFlow:
    def test_search_items(self, client, sample_items):
        response = client.get("/items")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 5
        titles = [item["title"] for item in data]
        assert "Item 0" in titles
        assert "Item 4" in titles
