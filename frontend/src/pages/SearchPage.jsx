import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { useSearch } from '../hooks/useSearch';
import ItemCard from '../components/ItemCard';
import SearchBar from '../components/SearchBar';
import FilterPanel from '../components/FilterPanel';
import Pagination from '../components/Pagination';
import LoadingSpinner from '../components/LoadingSpinner';
import { PAGE_SIZE } from '../utils/constants';

export default function SearchPage() {
  const { query, results, loading, setQuery } = useSearch();
  const [filters, setFilters] = useState({ genres: [], minRating: null, sortBy: '' });
  const [currentPage, setCurrentPage] = useState(1);

  const filtered = results.filter((item) => {
    if (filters.genres.length > 0 && !filters.genres.includes(item.genre)) return false;
    return true;
  });

  const totalPages = Math.ceil(filtered.length / PAGE_SIZE);
  const paginatedItems = filtered.slice((currentPage - 1) * PAGE_SIZE, currentPage * PAGE_SIZE);

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--spacing-md)' }}>
      <h1 style={{ color: 'var(--text)', fontSize: '1.5rem', fontWeight: 700 }}>Search</h1>

      <div style={{ maxWidth: 500 }}>
        <SearchBar onSearch={setQuery} placeholder="Search items by title or description..." />
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: '250px 1fr', gap: 'var(--spacing-md)' }}>
        <FilterPanel filters={filters} onFilterChange={(f) => { setFilters(f); setCurrentPage(1); }} />

        <div>
          {loading ? (
            <LoadingSpinner />
          ) : (
            <>
              {query && (
                <p style={{ color: 'var(--text-muted)', fontSize: '0.85rem', marginBottom: 'var(--spacing-md)' }}>
                  {filtered.length} results for "{query}"
                </p>
              )}
              <div style={{
                display: 'grid',
                gridTemplateColumns: 'repeat(auto-fill, minmax(220px, 1fr))',
                gap: 'var(--spacing-md)',
              }}>
                {paginatedItems.map((item) => (
                  <Link key={item.id} to={`/items/${item.id}`} style={{ textDecoration: 'none' }}>
                    <ItemCard item={item} />
                  </Link>
                ))}
              </div>
              {query && filtered.length === 0 && (
                <p style={{ color: 'var(--text-muted)', textAlign: 'center', padding: 'var(--spacing-xl)' }}>
                  No results found for "{query}"
                </p>
              )}
              {!query && (
                <p style={{ color: 'var(--text-muted)', textAlign: 'center', padding: 'var(--spacing-xl)' }}>
                  Start typing to search items
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
