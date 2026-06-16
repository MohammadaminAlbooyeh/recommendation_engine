import React from 'react';

export default function EngagementMetrics({ data }) {
  if (!data || data.length === 0) {
    return <div style={{ color: 'var(--text-muted)', textAlign: 'center', padding: 'var(--spacing-lg)' }}>No data</div>;
  }

  const maxVal = Math.max(...data.map((d) => d.value));

  return (
    <div style={{ backgroundColor: 'var(--bg-card)', borderRadius: 'var(--radius-lg)', padding: 'var(--spacing-md)' }}>
      <h3 style={{ color: 'var(--text)', fontSize: '1rem', fontWeight: 600, marginBottom: 'var(--spacing-md)' }}>
        Engagement Over Time
      </h3>
      <div style={{ display: 'flex', alignItems: 'flex-end', gap: 4, height: 120 }}>
        {data.map((point, idx) => {
          const pct = maxVal > 0 ? (point.value / maxVal) * 100 : 0;
          return (
            <div key={idx} style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 4 }}>
              <div
                title={`${point.label}: ${point.value}`}
                style={{
                  width: '100%',
                  height: `${pct}%`,
                  backgroundColor: 'var(--primary)',
                  borderRadius: 'var(--radius-sm) var(--radius-sm) 0 0',
                  minHeight: 4,
                  transition: 'height 0.5s ease',
                }}
              />
              <span style={{ fontSize: '0.65rem', color: 'var(--text-muted)', transform: 'rotate(-45deg)', whiteSpace: 'nowrap' }}>
                {point.label}
              </span>
            </div>
          );
        })}
      </div>
    </div>
  );
}
