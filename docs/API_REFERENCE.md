# API Reference

The Recommendation Engine API is built with FastAPI and serves at `http://localhost:8000`.

## Endpoints

### Items
- **GET /items**: List all items (movies).
    - Query Params: `skip` (int), `limit` (int).
    - Response: List of Item objects.

### Ratings
- **POST /ratings**: Submit a new rating.
    - Body:
      ```json
      {
        "user_id": 1,
        "item_id": 5,
        "rating": 4.5
      }
      ```
    - Response: Created Rating object.

### Recommendations
- **GET /recommendations/{user_id}**: Get personalized recommendations for a user.
    - Path Params: `user_id` (int).
    - Query Params: `n` (int) - Number of recommendations to return.
    - Response: List of Item objects.

## Data Models

### Item
```json
{
  "id": 1,
  "title": "Inception",
  "genre": "Sci-Fi",
  "description": "..."
}
```

### Rating
```json
{
  "id": 1,
  "user_id": 1,
  "item_id": 5,
  "rating": 4.5,
  "timestamp": "2023-01-01T00:00:00"
}
```
