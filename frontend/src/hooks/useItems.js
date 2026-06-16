import { useEffect, useCallback } from 'react';
import { useStore } from '../store/store';
import { setItems, setLoading, setError } from '../store/actions/itemActions';
import { fetchItems as fetchItemsApi } from '../services/recommendation_api';

export function useItems() {
  const { state, dispatch } = useStore();

  const fetchItems = useCallback(async () => {
    dispatch(setLoading(true));
    try {
      const items = await fetchItemsApi();
      dispatch(setItems(items));
    } catch (err) {
      dispatch(setError(err.response?.data?.detail || err.message));
    }
  }, [dispatch]);

  useEffect(() => {
    if (state.items.items.length === 0) {
      fetchItems();
    }
  }, [fetchItems, state.items.items.length]);

  return {
    items: state.items.items,
    loading: state.items.loading,
    error: state.items.error,
    fetchItems,
    refreshItems: fetchItems,
  };
}
