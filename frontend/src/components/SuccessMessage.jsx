import React, { useEffect } from 'react';

const typeStyles = {
  success: { backgroundColor: '#22c55e', color: '#fff' },
  error: { backgroundColor: '#ef4444', color: '#fff' },
  info: { backgroundColor: '#3b82f6', color: '#fff' },
};

export default function SuccessMessage({ message, type = 'success', onClose }) {
  useEffect(() => {
    if (!onClose) return;
    const timer = setTimeout(onClose, 3000);
    return () => clearTimeout(timer);
  }, [onClose]);

  return (
    <div style={{
      ...typeStyles[type] || typeStyles.info,
      padding: '12px 16px',
      borderRadius: 'var(--radius-md)',
      display: 'flex',
      justifyContent: 'space-between',
      alignItems: 'center',
      animation: 'slideDown 0.3s ease',
      boxShadow: 'var(--shadow-md)',
      marginBottom: 'var(--spacing-sm)',
    }}>
      <span style={{ fontSize: '0.9rem' }}>{message}</span>
      {onClose && (
        <button
          onClick={onClose}
          style={{
            background: 'none',
            border: 'none',
            color: 'inherit',
            cursor: 'pointer',
            fontSize: '1rem',
            marginLeft: 8,
            opacity: 0.8,
          }}
        >
          ✕
        </button>
      )}
    </div>
  );
}
