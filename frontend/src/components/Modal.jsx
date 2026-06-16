import React, { useEffect, useRef } from 'react';

export default function Modal({ title, children, onClose }) {
  const overlayRef = useRef();

  useEffect(() => {
    const handleEscape = (e) => {
      if (e.key === 'Escape') onClose?.();
    };
    document.addEventListener('keydown', handleEscape);
    document.body.style.overflow = 'hidden';
    return () => {
      document.removeEventListener('keydown', handleEscape);
      document.body.style.overflow = '';
    };
  }, [onClose]);

  const handleOverlayClick = (e) => {
    if (e.target === overlayRef.current) onClose?.();
  };

  return (
    <div
      ref={overlayRef}
      onClick={handleOverlayClick}
      style={{
        position: 'fixed',
        inset: 0,
        backgroundColor: 'rgba(0,0,0,0.6)',
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        zIndex: 1000,
        animation: 'fadeIn 0.2s ease',
      }}
    >
      <div style={{
        backgroundColor: 'var(--bg-card)',
        borderRadius: 'var(--radius-lg)',
        padding: 'var(--spacing-lg)',
        minWidth: 320,
        maxWidth: 500,
        width: '90%',
        boxShadow: 'var(--shadow-xl)',
        animation: 'slideUp 0.2s ease',
      }}>
        <div style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          marginBottom: 'var(--spacing-md)',
        }}>
          <h2 style={{ color: 'var(--text)', fontSize: '1.25rem', fontWeight: 600 }}>{title}</h2>
          <button
            onClick={onClose}
            style={{
              background: 'none',
              border: 'none',
              color: 'var(--text-muted)',
              fontSize: '1.25rem',
              cursor: 'pointer',
              padding: 4,
            }}
          >
            ✕
          </button>
        </div>
        {children}
      </div>
    </div>
  );
}
