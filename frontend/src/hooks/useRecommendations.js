import { useEffect, useCallback } from 'react';
import { useStore } from '../store/store';
import { setRecommendations, setLoading, setError } from '../store/actions/recommendationActions';
import { fetchRecommendations as fetchRecsApi } from '../services/recommendation_api';

export function useRecommendations(userId) {
  const { state, dispatch } = useStore();

  const fetchRecommendations = useCallback(async () => {
    if (!userId) return;
    dispatch(setLoading(true));
    try {
      const recs = await fetchRecsApi(userId);
      dispatch(setRecommendations(recs));
    } catch (err) {
      dispatch(setError(err.response?.data?.detail || err.message));
    }
  }, [userId, dispatch]);

  useEffect(() => {
    fetchRecommendations();
  }, [fetchRecommendations]);

  return {
    recommendations: state.recommendations.recommendations,
    loading: state.recommendations.loading,
    error: state.recommendations.error,
    fetchRecommendations,
  };
}
