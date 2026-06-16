import api from './api';
import { endpoints } from './config';

export async function fetchItems(skip = 0, limit = 100) {
  const response = await api.get(endpoints.items, { params: { skip, limit } });
  return response.data;
}

export async function fetchRecommendations(userId, n = 10) {
  const response = await api.get(endpoints.recommendations(userId), { params: { n } });
  return response.data;
}

export async function submitRating(userId, itemId, rating) {
  const response = await api.post(endpoints.ratings, {
    user_id: userId,
    item_id: itemId,
    rating,
  });
  return response.data;
}
