import React from 'react';

export default function RatingDistribution({ data }) {
  if (!data || data.length === 0) {
    return <div style={{ color: 'var(--text-muted)', textAlign: 'center', padding: 'var(--spacing-lg)' }}>No data</div>;
  }

  const maxVal = Math.max(...data.map((d) => d.count));

  return (
    <div style={{ backgroundColor: 'var(--bg-card)', borderRadius: 'var(--radius-lg)', padding: 'var(--spacing-md)' }}>
      <h3 style={{ color: 'var(--text)', fontSize: '1rem', fontWeight: 600, marginBottom: 'var(--spacing-md)' }}>
        Rating Distribution
      </h3>
      <div style={{ display: 'flex', alignItems: 'flex-end', gap: 'var(--spacing-sm)', height: 120, justifyContent: 'center' }}>
        {[1, 2, 3, 4, 5].map((star) => {
          const point = data.find((d) => d.rating === star);
          const count = point?.count || 0;
          const pct = maxVal > 0 ? (count / maxVal) * 100 : 0;
          return (
            <div key={star} style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 4, flex: 1, maxWidth: 60 }}>
              <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>{count}</span>
              <div style={{
                width: '100%',
                height: `${pct}%`,
                backgroundColor: star <= 2 ? '#ef4444' : star === 3 ? '#eab308' : '#22c55e',
                borderRadius: 'var(--radius-sm) var(--radius-sm) 0 0',
                minHeight: 4,
                transition: 'height 0.5s ease',
              }} />
              <span style={{ fontSize: '0.85rem', color: 'var(--text)' }}>{star}★</span>
            </div>
          );
        })}
      </div>
    </div>
  );
}
