import React from 'react';

export default function UserActivity({ data }) {
  if (!data || data.length === 0) {
    return <div style={{ color: 'var(--text-muted)', textAlign: 'center', padding: 'var(--spacing-lg)' }}>No data</div>;
  }

  const maxVal = Math.max(...data.map((d) => d.count));

  return (
    <div style={{ backgroundColor: 'var(--bg-card)', borderRadius: 'var(--radius-lg)', padding: 'var(--spacing-md)' }}>
      <h3 style={{ color: 'var(--text)', fontSize: '1rem', fontWeight: 600, marginBottom: 'var(--spacing-md)' }}>
        User Activity
      </h3>
      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fill, minmax(24px, 1fr))',
        gap: 3,
      }}>
        {data.map((day, idx) => {
          const intensity = maxVal > 0 ? day.count / maxVal : 0;
          const bg = intensity === 0 ? 'var(--bg)' :
            intensity < 0.25 ? '#1e3a5f' :
            intensity < 0.5 ? '#2563eb' :
            intensity < 0.75 ? '#3b82f6' : '#60a5fa';
          return (
            <div
              key={idx}
              title={`${day.date}: ${day.count} actions`}
              style={{
                width: '100%',
                aspectRatio: '1',
                backgroundColor: bg,
                borderRadius: 3,
                transition: 'background-color 0.2s ease',
              }}
            />
          );
        })}
      </div>
    </div>
  );
}
