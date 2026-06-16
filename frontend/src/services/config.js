export const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

export const endpoints = {
  items: '/items',
  ratings: '/ratings',
  recommendations: (userId) => `/recommendations/${userId}`,
};
