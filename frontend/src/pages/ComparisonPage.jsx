import React, { useState } from 'react';
import { useRecommendations } from '../hooks/useRecommendations';
import RecommendationList from '../components/RecommendationList';
import AlgorithmComparison from '../charts/AlgorithmComparison';

export default function ComparisonPage() {
  const [userId, setUserId] = useState(1);
  const { recommendations, loading, error } = useRecommendations(userId);

  const algoData = [
    { name: 'Collaborative Filtering', score: 0.92 },
    { name: 'Content-Based', score: 0.78 },
    { name: 'Hybrid', score: 0.88 },
    { name: 'Popularity', score: 0.65 },
  ];

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--spacing-lg)' }}>
      <h1 style={{ color: 'var(--text)', fontSize: '1.5rem', fontWeight: 700 }}>Algorithm Comparison</h1>

      <div style={{
        backgroundColor: 'var(--bg-card)',
        borderRadius: 'var(--radius-lg)',
        padding: 'var(--spacing-md)',
        display: 'flex',
        alignItems: 'flex-end',
        gap: 'var(--spacing-md)',
      }}>
        <div>
          <label style={{ color: 'var(--text-muted)', fontSize: '0.85rem', display: 'block', marginBottom: 4 }}>User ID</label>
          <input
            type="number"
            min={1}
            value={userId}
            onChange={(e) => setUserId(parseInt(e.target.value) || 1)}
            style={{
              padding: '8px 12px',
              borderRadius: 'var(--radius-sm)',
              border: '1px solid var(--border)',
              backgroundColor: 'var(--bg)',
              color: 'var(--text)',
              width: 80,
            }}
          />
        </div>
      </div>

      <div style={{
        display: 'grid',
        gridTemplateColumns: '1fr 1fr',
        gap: 'var(--spacing-md)',
      }}>
        <AlgorithmComparison data={algoData} />

        <div style={{ backgroundColor: 'var(--bg-card)', borderRadius: 'var(--radius-lg)', padding: 'var(--spacing-md)' }}>
          <h3 style={{ color: 'var(--text)', fontSize: '1rem', fontWeight: 600, marginBottom: 'var(--spacing-md)' }}>
            Recommendations (Default)
          </h3>
          <RecommendationList
            recommendations={recommendations}
            loading={loading}
            error={error}
          />
        </div>
      </div>
    </div>
  );
}
