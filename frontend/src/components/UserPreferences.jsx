import React from 'react';
import { GENRES } from '../utils/constants';

export default function UserPreferences({ preferences, onSave }) {
  const [localPrefs, setLocalPrefs] = React.useState(preferences || {
    favoriteGenres: [],
    ratingRange: [1, 5],
    notifications: true,
  });

  const handleGenreToggle = (genre) => {
    const current = localPrefs.favoriteGenres || [];
    const updated = current.includes(genre)
      ? current.filter((g) => g !== genre)
      : [...current, genre];
    setLocalPrefs({ ...localPrefs, favoriteGenres: updated });
  };

  const handleNotificationChange = () => {
    setLocalPrefs({ ...localPrefs, notifications: !localPrefs.notifications });
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
      <h3 style={{ color: 'var(--text)', fontSize: '1rem', fontWeight: 600 }}>Preferences</h3>

      <div>
        <label style={{ color: 'var(--text-muted)', fontSize: '0.85rem', display: 'block', marginBottom: 'var(--spacing-sm)' }}>
          Favorite Genres
        </label>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: 'var(--spacing-xs)' }}>
          {GENRES.map((genre) => (
            <button
              key={genre}
              onClick={() => handleGenreToggle(genre)}
              style={{
                padding: '4px 10px',
                borderRadius: 'var(--radius-full)',
                border: '1px solid var(--border)',
                backgroundColor: (localPrefs.favoriteGenres || []).includes(genre) ? 'var(--primary)' : 'transparent',
                color: (localPrefs.favoriteGenres || []).includes(genre) ? '#fff' : 'var(--text)',
                fontSize: '0.8rem',
                cursor: 'pointer',
              }}
            >
              {genre}
            </button>
          ))}
        </div>
      </div>

      <div>
        <label style={{ color: 'var(--text-muted)', fontSize: '0.85rem', display: 'block', marginBottom: 'var(--spacing-xs)' }}>
          Rating Range
        </label>
        <div style={{ display: 'flex', alignItems: 'center', gap: 'var(--spacing-sm)' }}>
          <input
            type="number"
            min={1}
            max={5}
            value={localPrefs.ratingRange[0]}
            onChange={(e) => setLocalPrefs({ ...localPrefs, ratingRange: [parseInt(e.target.value), localPrefs.ratingRange[1]] })}
            style={{
              width: 60,
              padding: '4px 8px',
              borderRadius: 'var(--radius-sm)',
              border: '1px solid var(--border)',
              backgroundColor: 'var(--bg)',
              color: 'var(--text)',
            }}
          />
          <span style={{ color: 'var(--text-muted)' }}>to</span>
          <input
            type="number"
            min={1}
            max={5}
            value={localPrefs.ratingRange[1]}
            onChange={(e) => setLocalPrefs({ ...localPrefs, ratingRange: [localPrefs.ratingRange[0], parseInt(e.target.value)] })}
            style={{
              width: 60,
              padding: '4px 8px',
              borderRadius: 'var(--radius-sm)',
              border: '1px solid var(--border)',
              backgroundColor: 'var(--bg)',
              color: 'var(--text)',
            }}
          />
        </div>
      </div>

      <label style={{ display: 'flex', alignItems: 'center', gap: 'var(--spacing-sm)', color: 'var(--text)', fontSize: '0.9rem' }}>
        <input
          type="checkbox"
          checked={localPrefs.notifications}
          onChange={handleNotificationChange}
        />
        Enable notifications
      </label>

      <button
        onClick={() => onSave?.(localPrefs)}
        style={{
          alignSelf: 'flex-start',
          padding: '8px 20px',
          borderRadius: 'var(--radius-md)',
          border: 'none',
          backgroundColor: 'var(--primary)',
          color: '#fff',
          fontWeight: 600,
          cursor: 'pointer',
          fontSize: '0.9rem',
        }}
      >
        Save Preferences
      </button>
    </div>
  );
}
