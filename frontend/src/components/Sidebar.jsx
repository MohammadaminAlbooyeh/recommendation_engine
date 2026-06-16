import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { GENRES } from '../utils/constants';

export default function Sidebar({ filters, onFilterChange, collapsed, onToggle }) {
  const [ratingRange, setRatingRange] = useState(filters?.ratingRange || [1, 5]);

  const handleGenreToggle = (genre) => {
    const current = filters?.genres || [];
    const updated = current.includes(genre)
      ? current.filter((g) => g !== genre)
      : [...current, genre];
    onFilterChange?.({ ...filters, genres: updated });
  };

  const handleRatingChange = (e) => {
    const value = parseInt(e.target.value);
    const newRange = [value, ratingRange[1]];
    setRatingRange(newRange);
    onFilterChange?.({ ...filters, ratingRange: newRange });
  };

  const navLinks = [
    { to: '/', label: 'Home' },
    { to: '/items', label: 'Items' },
    { to: '/recommendations', label: 'Recommendations' },
    { to: '/dashboard', label: 'Dashboard' },
    { to: '/profile', label: 'Profile' },
    { to: '/settings', label: 'Settings' },
    { to: '/compare', label: 'Compare' },
  ];

  return (
    <>
      {collapsed && (
        <button
          onClick={onToggle}
          style={{
            position: 'fixed',
            left: 8,
            top: '50%',
            transform: 'translateY(-50%)',
            zIndex: 90,
            background: 'var(--primary)',
            border: 'none',
            color: '#fff',
            borderRadius: 'var(--radius-full)',
            width: 32,
            height: 32,
            cursor: 'pointer',
            fontSize: 16,
          }}
        >
          ▶
        </button>
      )}

      <aside style={{
        width: collapsed ? 0 : 240,
        overflow: 'hidden',
        backgroundColor: 'var(--bg-card)',
        borderRight: collapsed ? 'none' : '1px solid var(--border)',
        padding: collapsed ? 0 : 'var(--spacing-md)',
        transition: 'all var(--transition-normal)',
        display: 'flex',
        flexDirection: 'column',
        gap: 'var(--spacing-md)',
      }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <h3 style={{ color: 'var(--text)', fontSize: '0.9rem', fontWeight: 600 }}>Navigation</h3>
          <button onClick={onToggle} style={{
            background: 'none', border: 'none', color: 'var(--text-muted)', cursor: 'pointer', fontSize: 16,
          }}>✕</button>
        </div>

        <nav style={{ display: 'flex', flexDirection: 'column', gap: 'var(--spacing-xs)' }}>
          {navLinks.map((link) => (
            <Link
              key={link.to}
              to={link.to}
              style={{
                color: 'var(--text)',
                textDecoration: 'none',
                padding: 'var(--spacing-xs) var(--spacing-sm)',
                borderRadius: 'var(--radius-sm)',
                fontSize: '0.9rem',
              }}
              onMouseEnter={(e) => e.target.style.backgroundColor = 'var(--bg-hover)'}
              onMouseLeave={(e) => e.target.style.backgroundColor = 'transparent'}
            >
              {link.label}
            </Link>
          ))}
        </nav>

        <hr style={{ border: 'none', borderTop: '1px solid var(--border)' }} />

        <h3 style={{ color: 'var(--text)', fontSize: '0.9rem', fontWeight: 600 }}>Genres</h3>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--spacing-xs)' }}>
          {GENRES.slice(0, 8).map((genre) => (
            <label key={genre} style={{ display: 'flex', alignItems: 'center', gap: 'var(--spacing-xs)', fontSize: '0.85rem', color: 'var(--text-muted)', cursor: 'pointer' }}>
              <input
                type="checkbox"
                checked={(filters?.genres || []).includes(genre)}
                onChange={() => handleGenreToggle(genre)}
              />
              {genre}
            </label>
          ))}
        </div>

        <hr style={{ border: 'none', borderTop: '1px solid var(--border)' }} />

        <h3 style={{ color: 'var(--text)', fontSize: '0.9rem', fontWeight: 600 }}>Min Rating</h3>
        <input
          type="range"
          min={1}
          max={5}
          step={1}
          value={ratingRange[0]}
          onChange={handleRatingChange}
          style={{ width: '100%' }}
        />
        <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>⭐ {ratingRange[0]}+</span>
      </aside>
    </>
  );
}
