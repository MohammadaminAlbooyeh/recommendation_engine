import React from 'react';

export default function Pagination({ currentPage, totalPages, onPageChange }) {
  if (totalPages <= 1) return null;

  const pages = [];
  const start = Math.max(1, currentPage - 2);
  const end = Math.min(totalPages, currentPage + 2);

  for (let i = start; i <= end; i++) {
    pages.push(i);
  }

  return (
    <div style={{
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      gap: 'var(--spacing-xs)',
      padding: 'var(--spacing-md) 0',
    }}>
      <button
        onClick={() => onPageChange(currentPage - 1)}
        disabled={currentPage === 1}
        style={{
          padding: '6px 12px',
          borderRadius: 'var(--radius-sm)',
          border: '1px solid var(--border)',
          backgroundColor: 'var(--bg-card)',
          color: currentPage === 1 ? 'var(--text-muted)' : 'var(--text)',
          cursor: currentPage === 1 ? 'not-allowed' : 'pointer',
        }}
      >
        Prev
      </button>

      {start > 1 && (
        <>
          <button onClick={() => onPageChange(1)} style={pageBtnStyle(1 === currentPage)}>1</button>
          {start > 2 && <span style={{ color: 'var(--text-muted)' }}>...</span>}
        </>
      )}

      {pages.map((page) => (
        <button
          key={page}
          onClick={() => onPageChange(page)}
          style={pageBtnStyle(page === currentPage)}
        >
          {page}
        </button>
      ))}

      {end < totalPages && (
        <>
          {end < totalPages - 1 && <span style={{ color: 'var(--text-muted)' }}>...</span>}
          <button onClick={() => onPageChange(totalPages)} style={pageBtnStyle(totalPages === currentPage)}>
            {totalPages}
          </button>
        </>
      )}

      <button
        onClick={() => onPageChange(currentPage + 1)}
        disabled={currentPage === totalPages}
        style={{
          padding: '6px 12px',
          borderRadius: 'var(--radius-sm)',
          border: '1px solid var(--border)',
          backgroundColor: 'var(--bg-card)',
          color: currentPage === totalPages ? 'var(--text-muted)' : 'var(--text)',
          cursor: currentPage === totalPages ? 'not-allowed' : 'pointer',
        }}
      >
        Next
      </button>
    </div>
  );
}

function pageBtnStyle(isActive) {
  return {
    padding: '6px 12px',
    borderRadius: 'var(--radius-sm)',
    border: '1px solid var(--border)',
    backgroundColor: isActive ? 'var(--primary)' : 'var(--bg-card)',
    color: isActive ? '#fff' : 'var(--text)',
    cursor: 'pointer',
    fontWeight: isActive ? 600 : 400,
  };
}
