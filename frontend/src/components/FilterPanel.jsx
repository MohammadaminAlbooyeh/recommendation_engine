import React from 'react';
import { GENRES, RATING_OPTIONS } from '../utils/constants';

export default function FilterPanel({ filters, onFilterChange }) {
  const handleGenreToggle = (genre) => {
    const current = filters?.genres || [];
    const updated = current.includes(genre)
      ? current.filter((g) => g !== genre)
      : [...current, genre];
    onFilterChange?.({ ...filters, genres: updated });
  };

  const handleRatingChange = (rating) => {
    onFilterChange?.({ ...filters, minRating: rating });
  };

  const handleSortChange = (e) => {
    onFilterChange?.({ ...filters, sortBy: e.target.value });
  };

  return (
    <div style={{
      backgroundColor: 'var(--bg-card)',
      borderRadius: 'var(--radius-lg)',
      padding: 'var(--spacing-md)',
      display: 'flex',
      flexDirection: 'column',
      gap: 'var(--spacing-md)',
    }}>
      <h3 style={{ color: 'var(--text)', fontSize: '0.9rem', fontWeight: 600 }}>Filters</h3>

      <div>
        <label style={{ color: 'var(--text-muted)', fontSize: '0.85rem', display: 'block', marginBottom: 'var(--spacing-xs)' }}>
          Genres
        </label>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 'var(--spacing-xs)' }}>
          {GENRES.slice(0, 6).map((genre) => (
            <button
              key={genre}
              onClick={() => handleGenreToggle(genre)}
              style={{
                padding: '4px 10px',
                borderRadius: 'var(--radius-full)',
                border: '1px solid var(--border)',
                backgroundColor: (filters?.genres || []).includes(genre) ? 'var(--primary)' : 'transparent',
                color: (filters?.genres || []).includes(genre) ? '#fff' : 'var(--text)',
                fontSize: '0.8rem',
                cursor: 'pointer',
                transition: 'all var(--transition-fast)',
              }}
            >
              {genre}
            </button>
          ))}
        </div>
      </div>

      <div>
        <label style={{ color: 'var(--text-muted)', fontSize: '0.85rem', display: 'block', marginBottom: 'var(--spacing-xs)' }}>
          Min Rating
        </label>
        <div style={{ display: 'flex', gap: 'var(--spacing-xs)' }}>
          {RATING_OPTIONS.map((r) => (
            <button
              key={r}
              onClick={() => handleRatingChange(r)}
              style={{
                padding: '4px 8px',
                borderRadius: 'var(--radius-sm)',
                border: '1px solid var(--border)',
                backgroundColor: filters?.minRating === r ? 'var(--accent)' : 'transparent',
                color: filters?.minRating === r ? '#fff' : 'var(--text)',
                fontSize: '0.8rem',
                cursor: 'pointer',
              }}
            >
              {r}★
            </button>
          ))}
        </div>
      </div>

      <div>
        <label style={{ color: 'var(--text-muted)', fontSize: '0.85rem', display: 'block', marginBottom: 'var(--spacing-xs)' }}>
          Sort By
        </label>
        <select
          value={filters?.sortBy || ''}
          onChange={handleSortChange}
          style={{
            width: '100%',
            padding: '6px 8px',
            borderRadius: 'var(--radius-sm)',
            border: '1px solid var(--border)',
            backgroundColor: 'var(--bg)',
            color: 'var(--text)',
            fontSize: '0.85rem',
          }}
        >
          <option value="">Default</option>
          <option value="rating">Highest Rated</option>
          <option value="title">Title A-Z</option>
          <option value="newest">Newest</option>
        </select>
      </div>
    </div>
  );
}
