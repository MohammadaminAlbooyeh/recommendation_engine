import React, { useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { useItems } from '../hooks/useItems';
import RatingComponent from '../components/RatingComponent';
import { submitRating } from '../services/recommendation_api';
import { formatRating } from '../utils/formatters';
import SuccessMessage from '../components/SuccessMessage';

export default function ItemDetailPage() {
  const { id } = useParams();
  const { items, refreshItems } = useItems();
  const item = items.find((i) => i.id === parseInt(id));
  const [notification, setNotification] = useState(null);

  const similarItems = items
    .filter((i) => i.id !== item?.id && i.genre === item?.genre)
    .slice(0, 4);

  const handleRate = async (rating) => {
    try {
      await submitRating(1, parseInt(id), rating);
      setNotification({ message: 'Rating submitted!', type: 'success' });
      refreshItems();
    } catch {
      setNotification({ message: 'Failed to submit rating', type: 'error' });
    }
  };

  if (!item) {
    return <div style={{ color: 'var(--text-muted)', textAlign: 'center', padding: 'var(--spacing-xl)' }}>Item not found</div>;
  }

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--spacing-lg)' }}>
      {notification && (
        <SuccessMessage
          message={notification.message}
          type={notification.type}
          onClose={() => setNotification(null)}
        />
      )}

      <Link to="/items" style={{ color: 'var(--accent)', fontSize: '0.9rem' }}>← Back to Items</Link>

      <div style={{
        backgroundColor: 'var(--bg-card)',
        borderRadius: 'var(--radius-lg)',
        padding: 'var(--spacing-lg)',
        display: 'flex',
        flexDirection: 'column',
        gap: 'var(--spacing-md)',
      }}>
        <h1 style={{ color: 'var(--text)', fontSize: '2rem', fontWeight: 700 }}>{item.title}</h1>

        <span style={{
          alignSelf: 'flex-start',
          backgroundColor: 'var(--primary)',
          color: '#fff',
          padding: '4px 12px',
          borderRadius: 'var(--radius-full)',
          fontSize: '0.85rem',
        }}>{item.genre || 'Unknown'}</span>

        <p style={{ color: 'var(--text)', fontSize: '1rem', lineHeight: 1.7 }}>
          {item.description || 'No description available.'}
        </p>

        <div style={{ display: 'flex', alignItems: 'center', gap: 'var(--spacing-md)' }}>
          <span style={{ color: 'var(--text-muted)', fontSize: '0.9rem' }}>Average Rating:</span>
          <span style={{ color: 'var(--accent)', fontSize: '1.25rem', fontWeight: 700 }}>
            {item.average_rating ? formatRating(item.average_rating) : 'N/A'}
          </span>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: 'var(--spacing-md)' }}>
          <span style={{ color: 'var(--text-muted)', fontSize: '0.9rem' }}>Your Rating:</span>
          <RatingComponent value={0} onChange={handleRate} />
        </div>
      </div>

      {similarItems.length > 0 && (
        <section>
          <h2 style={{ color: 'var(--text)', fontSize: '1.25rem', fontWeight: 600, marginBottom: 'var(--spacing-md)' }}>
            Similar Items
          </h2>
          <div style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fill, minmax(200px, 1fr))',
            gap: 'var(--spacing-md)',
          }}>
            {similarItems.map((si) => (
              <Link key={si.id} to={`/items/${si.id}`} style={{ textDecoration: 'none' }}>
                <div style={{
                  backgroundColor: 'var(--bg-card)',
                  border: '1px solid var(--border)',
                  borderRadius: 'var(--radius-lg)',
                  padding: 'var(--spacing-md)',
                }}>
                  <h3 style={{ color: 'var(--text)', fontSize: '0.95rem', fontWeight: 600 }}>{si.title}</h3>
                  <span style={{ color: 'var(--text-muted)', fontSize: '0.8rem' }}>{si.genre}</span>
                </div>
              </Link>
            ))}
          </div>
        </section>
      )}
    </div>
  );
}
