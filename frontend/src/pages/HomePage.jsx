import React from 'react';
import { Link } from 'react-router-dom';
import { useItems } from '../hooks/useItems';
import { useUser } from '../hooks/useUser';
import ItemCard from '../components/ItemCard';
import LoadingSpinner from '../components/LoadingSpinner';

export default function HomePage() {
  const { items, loading } = useItems();
  const { user } = useUser();

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--spacing-xl)' }}>
      <section style={{
        textAlign: 'center',
        padding: 'var(--spacing-2xl) var(--spacing-lg)',
        background: 'linear-gradient(135deg, var(--primary), var(--secondary))',
        borderRadius: 'var(--radius-xl)',
      }}>
        <h1 style={{ fontSize: '2.5rem', fontWeight: 700, color: '#fff', marginBottom: 'var(--spacing-md)' }}>
          Discover Your Next Favorite
        </h1>
        <p style={{ fontSize: '1.1rem', color: 'rgba(255,255,255,0.8)', marginBottom: 'var(--spacing-lg)', maxWidth: 600, margin: '0 auto var(--spacing-lg)' }}>
          Personalized recommendations powered by machine learning. Rate items and get suggestions tailored to your taste.
        </p>
        <Link to="/items"
          style={{
            display: 'inline-block',
            padding: '12px 32px',
            backgroundColor: '#fff',
            color: 'var(--primary)',
            borderRadius: 'var(--radius-full)',
            fontWeight: 600,
            textDecoration: 'none',
          }}
        >
          Browse Items
        </Link>
      </section>

      {user && (
        <section>
          <h2 style={{ color: 'var(--text)', fontSize: '1.5rem', fontWeight: 600, marginBottom: 'var(--spacing-md)' }}>
            Recommended For You
          </h2>
          <Link to="/recommendations" style={{ color: 'var(--accent)', fontSize: '0.9rem', display: 'block', marginBottom: 'var(--spacing-md)' }}>
            View all recommendations →
          </Link>
        </section>
      )}

      <section>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 'var(--spacing-md)' }}>
          <h2 style={{ color: 'var(--text)', fontSize: '1.5rem', fontWeight: 600 }}>Popular Items</h2>
          <Link to="/items" style={{ color: 'var(--accent)', fontSize: '0.9rem' }}>View all →</Link>
        </div>
        {loading ? <LoadingSpinner /> : (
          <div style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fill, minmax(220px, 1fr))',
            gap: 'var(--spacing-md)',
          }}>
            {items.slice(0, 8).map((item) => (
              <Link key={item.id} to={`/items/${item.id}`} style={{ textDecoration: 'none' }}>
                <ItemCard item={item} />
              </Link>
            ))}
          </div>
        )}
      </section>
    </div>
  );
}
