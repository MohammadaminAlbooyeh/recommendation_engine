# Troubleshooting

## Common Issues

### Database connection fails
- Ensure PostgreSQL is running
- Check DATABASE_URL environment variable
- Verify network connectivity in Docker

### Recommendations return empty
- Ensure seed data has been run: `python scripts/seed_data.py`
- Check that ratings exist in the database
- Verify user_id exists

### Frontend can't reach API
- Check CORS configuration
- Verify API is running on expected port
- Check proxy settings in package.json

### Docker build fails
- Ensure Docker is running
- Clear Docker cache: `docker system prune -a`
- Check Dockerfile for errors

### Model training fails
- Ensure scikit-learn is installed
- Check that data has sufficient ratings
- Reduce model complexity if memory issues
