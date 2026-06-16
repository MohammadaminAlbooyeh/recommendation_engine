import React, { useState } from 'react';

export default function RatingComponent({ value, onChange, readOnly = false }) {
  const [hovered, setHovered] = useState(0);

  return (
    <div style={{ display: 'flex', gap: 2 }}>
      {[1, 2, 3, 4, 5].map((star) => (
        <button
          key={star}
          disabled={readOnly}
          onClick={() => !readOnly && onChange?.(star)}
          onMouseEnter={() => !readOnly && setHovered(star)}
          onMouseLeave={() => !readOnly && setHovered(0)}
          style={{
            background: 'none',
            border: 'none',
            cursor: readOnly ? 'default' : 'pointer',
            fontSize: '1.1rem',
            padding: '2px',
            color: (hovered || value) >= star ? '#f59e0b' : 'var(--border)',
            transition: 'color var(--transition-fast)',
          }}
        >
          ★
        </button>
      ))}
    </div>
  );
}
