import React from 'react';
import RecommendationCard from './RecommendationCard';
import LoadingSpinner from './LoadingSpinner';

export default function RecommendationList({ recommendations, loading, error, onRate }) {
  if (loading) return <LoadingSpinner />;

  if (error) {
    return (
      <div style={{
        padding: 'var(--spacing-lg)',
        textAlign: 'center',
        color: 'var(--error)',
      }}>
        Error: {error}
      </div>
    );
  }

  if (!recommendations || recommendations.length === 0) {
    return (
      <div style={{
        padding: 'var(--spacing-xl)',
        textAlign: 'center',
        color: 'var(--text-muted)',
      }}>
        <p style={{ fontSize: '1.1rem', marginBottom: 'var(--spacing-sm)' }}>No recommendations yet</p>
        <p style={{ fontSize: '0.9rem' }}>Rate some items to get personalized recommendations.</p>
      </div>
    );
  }

  return (
    <div style={{
      display: 'flex',
      flexDirection: 'column',
      gap: 'var(--spacing-md)',
    }}>
      {recommendations.map((item) => (
        <RecommendationCard
          key={item.id}
          item={item}
          score={item.score}
          onRate={onRate}
        />
      ))}
    </div>
  );
}
