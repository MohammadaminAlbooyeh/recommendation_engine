import React, { useState } from 'react';
import { useRecommendations } from '../hooks/useRecommendations';
import RecommendationList from '../components/RecommendationList';
import { submitRating } from '../services/recommendation_api';
import SuccessMessage from '../components/SuccessMessage';

export default function RecommendationsPage() {
  const [userId, setUserId] = useState(1);
  const [algorithm, setAlgorithm] = useState('default');
  const { recommendations, loading, error, fetchRecommendations } = useRecommendations(userId);
  const [notification, setNotification] = useState(null);

  const handleRate = async (itemId, rating) => {
    try {
      await submitRating(userId, itemId, rating);
      setNotification({ message: 'Rating submitted!', type: 'success' });
    } catch {
      setNotification({ message: 'Failed to submit rating', type: 'error' });
    }
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--spacing-md)' }}>
      {notification && (
        <SuccessMessage
          message={notification.message}
          type={notification.type}
          onClose={() => setNotification(null)}
        />
      )}

      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <h1 style={{ color: 'var(--text)', fontSize: '1.5rem', fontWeight: 700 }}>Recommendations</h1>
      </div>

      <div style={{
        backgroundColor: 'var(--bg-card)',
        borderRadius: 'var(--radius-lg)',
        padding: 'var(--spacing-md)',
        display: 'flex',
        gap: 'var(--spacing-md)',
        alignItems: 'flex-end',
        flexWrap: 'wrap',
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

        <div>
          <label style={{ color: 'var(--text-muted)', fontSize: '0.85rem', display: 'block', marginBottom: 4 }}>Algorithm</label>
          <select
            value={algorithm}
            onChange={(e) => setAlgorithm(e.target.value)}
            style={{
              padding: '8px 12px',
              borderRadius: 'var(--radius-sm)',
              border: '1px solid var(--border)',
              backgroundColor: 'var(--bg)',
              color: 'var(--text)',
            }}
          >
            <option value="default">Default</option>
            <option value="collaborative">Collaborative Filtering</option>
            <option value="content">Content-Based</option>
            <option value="hybrid">Hybrid</option>
          </select>
        </div>

        <button
          onClick={fetchRecommendations}
          style={{
            padding: '8px 20px',
            borderRadius: 'var(--radius-md)',
            border: 'none',
            backgroundColor: 'var(--primary)',
            color: '#fff',
            fontWeight: 600,
            cursor: 'pointer',
          }}
        >
          Refresh
        </button>
      </div>

      <RecommendationList
        recommendations={recommendations}
        loading={loading}
        error={error}
        onRate={handleRate}
      />
    </div>
  );
}
