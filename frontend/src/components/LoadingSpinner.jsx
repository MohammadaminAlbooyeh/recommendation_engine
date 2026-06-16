import React from 'react';

export default function LoadingSpinner({ size = 40, color = 'var(--primary)' }) {
  return (
    <div style={{
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      padding: 'var(--spacing-lg)',
    }}>
      <div style={{
        width: size,
        height: size,
        border: `3px solid var(--border)`,
        borderTopColor: color,
        borderRadius: '50%',
        animation: 'spin 0.8s linear infinite',
      }} />
    </div>
  );
}
