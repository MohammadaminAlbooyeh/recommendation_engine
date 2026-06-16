import React, { useState, useCallback, useRef, useEffect } from 'react';

export default function SearchBar({ onSearch, placeholder = 'Search...' }) {
  const [value, setValue] = useState('');
  const debounceRef = useRef();

  useEffect(() => {
    return () => clearTimeout(debounceRef.current);
  }, []);

  const debouncedSearch = useCallback(
    (q) => {
      clearTimeout(debounceRef.current);
      debounceRef.current = setTimeout(() => onSearch?.(q), 300);
    },
    [onSearch]
  );

  const handleChange = (e) => {
    const q = e.target.value;
    setValue(q);
    debouncedSearch(q);
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter') onSearch?.(value);
  };

  const handleClear = () => {
    setValue('');
    onSearch?.('');
  };

  return (
    <div style={{
      position: 'relative',
      display: 'flex',
      alignItems: 'center',
      width: '100%',
    }}>
      <span style={{
        position: 'absolute',
        left: 10,
        color: 'var(--text-muted)',
        fontSize: '0.9rem',
        pointerEvents: 'none',
      }}>
        🔍
      </span>
      <input
        type="text"
        value={value}
        onChange={handleChange}
        onKeyDown={handleKeyDown}
        placeholder={placeholder}
        style={{
          width: '100%',
          padding: '8px 32px 8px 34px',
          borderRadius: 'var(--radius-full)',
          border: '1px solid var(--border)',
          backgroundColor: 'var(--bg)',
          color: 'var(--text)',
          fontSize: '0.9rem',
          outline: 'none',
        }}
      />
      {value && (
        <button
          onClick={handleClear}
          style={{
            position: 'absolute',
            right: 10,
            background: 'none',
            border: 'none',
            color: 'var(--text-muted)',
            cursor: 'pointer',
            fontSize: '0.9rem',
          }}
        >
          ✕
        </button>
      )}
    </div>
  );
}
