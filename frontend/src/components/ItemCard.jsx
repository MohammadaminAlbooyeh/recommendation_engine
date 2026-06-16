import React from 'react';
import RatingComponent from './RatingComponent';
import { truncateText, formatRating } from '../utils/formatters';

export default function ItemCard({ item, onRate }) {
  return (
    <div style={{
      backgroundColor: 'var(--bg-card)',
      border: '1px solid var(--border)',
      borderRadius: 'var(--radius-lg)',
      padding: 'var(--spacing-md)',
      display: 'flex',
      flexDirection: 'column',
      gap: 'var(--spacing-sm)',
      transition: 'transform var(--transition-fast), box-shadow var(--transition-fast)',
      cursor: 'default',
    }}
      onMouseEnter={(e) => {
        e.currentTarget.style.transform = 'translateY(-2px)';
        e.currentTarget.style.boxShadow = 'var(--shadow-lg)';
      }}
      onMouseLeave={(e) => {
        e.currentTarget.style.transform = 'none';
        e.currentTarget.style.boxShadow = 'none';
      }}
    >
      <h3 style={{ color: 'var(--text)', fontSize: '1rem', fontWeight: 600 }}>{item.title}</h3>
      <span style={{
        alignSelf: 'flex-start',
        backgroundColor: 'var(--primary)',
        color: '#fff',
        padding: '2px 8px',
        borderRadius: 'var(--radius-full)',
        fontSize: '0.75rem',
        fontWeight: 500,
      }}>{item.genre || 'Unknown'}</span>
      <p style={{ color: 'var(--text-muted)', fontSize: '0.85rem', lineHeight: 1.4 }}>
        {truncateText(item.description, 80)}
      </p>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginTop: 'auto' }}>
        <span style={{ color: 'var(--accent)', fontWeight: 600, fontSize: '0.9rem' }}>
          {item.average_rating ? formatRating(item.average_rating) : 'N/A'}
        </span>
        {onRate && <RatingComponent value={0} onChange={(r) => onRate(item.id, r)} />}
      </div>
    </div>
  );
}
