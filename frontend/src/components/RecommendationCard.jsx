import React from 'react';
import RatingComponent from './RatingComponent';
import { formatRating } from '../utils/formatters';

export default function RecommendationCard({ item, score, onRate }) {
  return (
    <div style={{
      backgroundColor: 'var(--bg-card)',
      border: '1px solid var(--border)',
      borderRadius: 'var(--radius-lg)',
      padding: 'var(--spacing-md)',
      display: 'flex',
      flexDirection: 'column',
      gap: 'var(--spacing-sm)',
    }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
        <h3 style={{ color: 'var(--text)', fontSize: '1rem', fontWeight: 600 }}>{item.title}</h3>
        {score !== undefined && (
          <span style={{
            backgroundColor: 'var(--accent)',
            color: '#fff',
            padding: '2px 8px',
            borderRadius: 'var(--radius-full)',
            fontSize: '0.75rem',
            fontWeight: 700,
          }}>
            {formatRating(score)}
          </span>
        )}
      </div>

      <span style={{
        alignSelf: 'flex-start',
        backgroundColor: 'var(--primary)',
        color: '#fff',
        padding: '2px 8px',
        borderRadius: 'var(--radius-full)',
        fontSize: '0.75rem',
      }}>{item.genre || 'Unknown'}</span>

      <p style={{ color: 'var(--text-muted)', fontSize: '0.85rem' }}>{item.description}</p>

      {score !== undefined && (
        <div>
          <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.75rem', color: 'var(--text-muted)', marginBottom: 4 }}>
            <span>Match</span>
            <span>{formatRating(score * 100)}%</span>
          </div>
          <div style={{
            height: 6,
            backgroundColor: 'var(--bg)',
            borderRadius: 'var(--radius-full)',
            overflow: 'hidden',
          }}>
            <div style={{
              height: '100%',
              width: `${Math.min(100, (score || 0) * 100)}%`,
              backgroundColor: 'var(--primary)',
              borderRadius: 'var(--radius-full)',
              transition: 'width var(--transition-normal)',
            }} />
          </div>
        </div>
      )}

      {onRate && (
        <div style={{ display: 'flex', alignItems: 'center', gap: 'var(--spacing-sm)', marginTop: 'auto' }}>
          <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>Rate:</span>
          <RatingComponent value={0} onChange={(r) => onRate(item.id, r)} />
        </div>
      )}
    </div>
  );
}
