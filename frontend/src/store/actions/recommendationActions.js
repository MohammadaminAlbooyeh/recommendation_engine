export const SET_RECOMMENDATIONS = 'SET_RECOMMENDATIONS';
export const SET_LOADING = 'SET_LOADING';
export const SET_ERROR = 'SET_ERROR';

export function setRecommendations(recommendations) {
  return { type: SET_RECOMMENDATIONS, payload: recommendations };
}

export function setLoading(loading) {
  return { type: SET_LOADING, payload: loading };
}

export function setError(error) {
  return { type: SET_ERROR, payload: error };
}
