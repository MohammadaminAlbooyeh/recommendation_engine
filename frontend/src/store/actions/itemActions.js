export const SET_ITEMS = 'SET_ITEMS';
export const SET_LOADING = 'SET_LOADING';
export const SET_ERROR = 'SET_ERROR';

export function setItems(items) {
  return { type: SET_ITEMS, payload: items };
}

export function setLoading(loading) {
  return { type: SET_LOADING, payload: loading };
}

export function setError(error) {
  return { type: SET_ERROR, payload: error };
}
