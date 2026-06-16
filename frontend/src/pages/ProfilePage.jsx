import React from 'react';
import { useUser } from '../hooks/useUser';
import { useItems } from '../hooks/useItems';
import UserPreferences from '../components/UserPreferences';
import { formatDate } from '../utils/date_utils';

export default function ProfilePage() {
  const { user, preferences, setUser, updatePreferences } = useUser();
  const { items } = useItems();

  const dummyRatings = items.slice(0, 5).map((item) => ({
    item,
    rating: Math.floor(Math.random() * 5) + 1,
    date: new Date(Date.now() - Math.random() * 7 * 86400000).toISOString(),
  }));

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--spacing-lg)' }}>
      <h1 style={{ color: 'var(--text)', fontSize: '1.5rem', fontWeight: 700 }}>Profile</h1>

      <div style={{
        backgroundColor: 'var(--bg-card)',
        borderRadius: 'var(--radius-lg)',
        padding: 'var(--spacing-lg)',
        display: 'flex',
        alignItems: 'center',
        gap: 'var(--spacing-lg)',
      }}>
        <div style={{
          width: 64,
          height: 64,
          borderRadius: 'var(--radius-full)',
          backgroundColor: 'var(--primary)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          color: '#fff',
          fontSize: '1.5rem',
          fontWeight: 700,
        }}>
          {user?.username ? user.username[0].toUpperCase() : '?'}
        </div>
        <div>
          <h2 style={{ color: 'var(--text)', fontSize: '1.25rem', fontWeight: 600 }}>
            {user?.username || 'Guest User'}
          </h2>
          <p style={{ color: 'var(--text-muted)', fontSize: '0.9rem' }}>
            {user?.email || 'guest@example.com'}
          </p>
        </div>
        <button
          onClick={() => setUser({ username: 'Demo User', email: 'demo@example.com' })}
          style={{
            marginLeft: 'auto',
            padding: '6px 16px',
            borderRadius: 'var(--radius-sm)',
            border: '1px solid var(--border)',
            backgroundColor: 'transparent',
            color: 'var(--text)',
            cursor: 'pointer',
            fontSize: '0.85rem',
          }}
        >
          Set Demo User
        </button>
      </div>

      <UserPreferences
        preferences={preferences}
        onSave={updatePreferences}
      />

      <div style={{
        backgroundColor: 'var(--bg-card)',
        borderRadius: 'var(--radius-lg)',
        padding: 'var(--spacing-md)',
      }}>
        <h3 style={{ color: 'var(--text)', fontSize: '1rem', fontWeight: 600, marginBottom: 'var(--spacing-md)' }}>
          Recent Ratings
        </h3>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--spacing-sm)' }}>
          {dummyRatings.map((r, idx) => (
            <div key={idx} style={{
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
              padding: 'var(--spacing-sm) 0',
              borderBottom: '1px solid var(--border)',
            }}>
              <span style={{ color: 'var(--text)', fontSize: '0.9rem' }}>{r.item.title}</span>
              <div style={{ display: 'flex', alignItems: 'center', gap: 'var(--spacing-sm)' }}>
                <span style={{ color: 'var(--warning)', fontSize: '0.9rem' }}>{'★'.repeat(r.rating)}{'☆'.repeat(5 - r.rating)}</span>
                <span style={{ color: 'var(--text-muted)', fontSize: '0.8rem' }}>{formatDate(r.date)}</span>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
