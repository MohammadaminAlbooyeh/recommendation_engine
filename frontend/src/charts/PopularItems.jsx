import React from 'react';

const COLORS = ['#6366f1', '#06b6d4', '#22c55e', '#eab308', '#f97316'];

export default function PopularItems({ data }) {
  if (!data || data.length === 0) {
    return <div style={{ color: 'var(--text-muted)', textAlign: 'center', padding: 'var(--spacing-lg)' }}>No data</div>;
  }

  const maxVal = Math.max(...data.map((d) => d.count));

  return (
    <div style={{ backgroundColor: 'var(--bg-card)', borderRadius: 'var(--radius-lg)', padding: 'var(--spacing-md)' }}>
      <h3 style={{ color: 'var(--text)', fontSize: '1rem', fontWeight: 600, marginBottom: 'var(--spacing-md)' }}>
        Popular Items
      </h3>
      <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--spacing-sm)' }}>
        {data.map((item, idx) => {
          const pct = maxVal > 0 ? (item.count / maxVal) * 100 : 0;
          return (
            <div key={item.name || idx} style={{ display: 'flex', alignItems: 'center', gap: 'var(--spacing-sm)' }}>
              <span style={{ width: 100, fontSize: '0.8rem', color: 'var(--text)', textAlign: 'right', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                {item.name}
              </span>
              <div style={{ flex: 1, height: 20, backgroundColor: 'var(--bg)', borderRadius: 'var(--radius-full)', overflow: 'hidden' }}>
                <div style={{
                  height: '100%',
                  width: `${pct}%`,
                  backgroundColor: COLORS[idx % COLORS.length],
                  borderRadius: 'var(--radius-full)',
                  transition: 'width 0.5s ease',
                  display: 'flex',
                  alignItems: 'center',
                  paddingLeft: 8,
                }}>
                  <span style={{ fontSize: '0.7rem', color: '#fff', fontWeight: 600 }}>{item.count}</span>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
