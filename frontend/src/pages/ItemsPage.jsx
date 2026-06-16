import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { useItems } from '../hooks/useItems';
import { useStore } from '../store/store';
import { setGenreFilter } from '../store/actions/filterActions';
import ItemCard from '../components/ItemCard';
import FilterPanel from '../components/FilterPanel';
import SearchBar from '../components/SearchBar';
import Pagination from '../components/Pagination';
import LoadingSpinner from '../components/LoadingSpinner';
import { submitRating } from '../services/recommendation_api';
import { PAGE_SIZE } from '../utils/constants';

export default function ItemsPage() {
  const { items, loading, refreshItems } = useItems();
  const { state, dispatch } = useStore();
  const [currentPage, setCurrentPage] = useState(1);
  const [searchQuery, setSearchQuery] = useState('');

  const filtered = items.filter((item) => {
    if (state.filters.genres.length > 0 && !state.filters.genres.includes(item.genre)) return false;
    if (searchQuery && !item.title.toLowerCase().includes(searchQuery.toLowerCase())) return false;
    return true;
  });

  const totalPages = Math.ceil(filtered.length / PAGE_SIZE);
  const paginatedItems = filtered.slice((currentPage - 1) * PAGE_SIZE, currentPage * PAGE_SIZE);

  const handleRate = async (itemId, rating) => {
    try {
      await submitRating(1, itemId, rating);
      refreshItems();
    } catch (err) {
      console.error('Rating failed:', err);
    }
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--spacing-md)' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h1 style={{ color: 'var(--text)', fontSize: '1.5rem', fontWeight: 700 }}>All Items</h1>
      </div>

      <div style={{ display: 'flex', gap: 'var(--spacing-md)' }}>
        <div style={{ flex: 1, maxWidth: 400 }}>
          <SearchBar onSearch={setSearchQuery} placeholder="Search items..." />
        </div>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '250px 1fr', gap: 'var(--spacing-md)' }}>
        <FilterPanel
          filters={state.filters}
          onFilterChange={(f) => {
            Object.entries(f).forEach(([key, value]) => {
              if (key === 'genres') dispatch(setGenreFilter(value));
            });
            setCurrentPage(1);
          }}
        />

        <div>
          {loading ? <LoadingSpinner /> : (
            <>
              <p style={{ color: 'var(--text-muted)', fontSize: '0.85rem', marginBottom: 'var(--spacing-md)' }}>
                Showing {paginatedItems.length} of {filtered.length} items
              </p>
              <div style={{
                display: 'grid',
                gridTemplateColumns: 'repeat(auto-fill, minmax(220px, 1fr))',
                gap: 'var(--spacing-md)',
              }}>
                {paginatedItems.map((item) => (
                  <Link key={item.id} to={`/items/${item.id}`} style={{ textDecoration: 'none' }}>
                    <ItemCard item={item} onRate={handleRate} />
                  </Link>
                ))}
              </div>
              {filtered.length === 0 && (
                <p style={{ color: 'var(--text-muted)', textAlign: 'center', padding: 'var(--spacing-xl)' }}>
                  No items found.
                </p>
              )}
              <Pagination currentPage={currentPage} totalPages={totalPages} onPageChange={setCurrentPage} />
            </>
          )}
        </div>
      </div>
    </div>
  );
}
