import { useState, useCallback, useRef, useEffect } from 'react';
import api from '../services/api';

export function useSearch() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const debounceRef = useRef();

  useEffect(() => {
    return () => clearTimeout(debounceRef.current);
  }, []);

  const search = useCallback((q) => {
    clearTimeout(debounceRef.current);
    debounceRef.current = setTimeout(async () => {
      if (!q.trim()) {
        setResults([]);
        return;
      }
      setLoading(true);
      try {
        const response = await api.get('/items', { params: { skip: 0, limit: 50 } });
        const filtered = response.data.filter(
          (item) =>
            item.title.toLowerCase().includes(q.toLowerCase()) ||
            (item.description && item.description.toLowerCase().includes(q.toLowerCase()))
        );
        setResults(filtered);
      } catch {
        setResults([]);
      } finally {
        setLoading(false);
      }
    }, 300);
  }, []);

  const handleSetQuery = useCallback(
    (q) => {
      setQuery(q);
      search(q);
    },
    [search]
  );

  return { query, results, loading, setQuery: handleSetQuery, search };
}
