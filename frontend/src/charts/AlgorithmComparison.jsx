import React from 'react';

const COLORS = ['#6366f1', '#ec4899', '#06b6d4', '#22c55e', '#eab308'];

export default function AlgorithmComparison({ data }) {
  if (!data || data.length === 0) {
    return <div style={{ color: 'var(--text-muted)', textAlign: 'center', padding: 'var(--spacing-lg)' }}>No data</div>;
  }

  return (
    <div style={{ backgroundColor: 'var(--bg-card)', borderRadius: 'var(--radius-lg)', padding: 'var(--spacing-md)' }}>
      <h3 style={{ color: 'var(--text)', fontSize: '1rem', fontWeight: 600, marginBottom: 'var(--spacing-md)' }}>
        Algorithm Comparison
      </h3>
      <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--spacing-md)' }}>
        {data.map((algo, idx) => {
          const maxVal = Math.max(...data.map((d) => d.score));
          const pct = maxVal > 0 ? (algo.score / maxVal) * 100 : 0;
          return (
            <div key={algo.name || idx}>
              <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 4 }}>
                <span style={{ color: 'var(--text)', fontSize: '0.85rem' }}>{algo.name}</span>
                <span style={{ color: 'var(--text-muted)', fontSize: '0.85rem' }}>{algo.score?.toFixed(2) || 'N/A'}</span>
              </div>
              <div style={{ height: 16, backgroundColor: 'var(--bg)', borderRadius: 'var(--radius-full)', overflow: 'hidden' }}>
                <div style={{
                  height: '100%',
                  width: `${pct}%`,
                  backgroundColor: COLORS[idx % COLORS.length],
                  borderRadius: 'var(--radius-full)',
                  transition: 'width 0.5s ease',
                }} />
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
