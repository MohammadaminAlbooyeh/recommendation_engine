import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import SearchBar from './SearchBar';

export default function Header() {
  const [menuOpen, setMenuOpen] = useState(false);

  return (
    <header style={{
      backgroundColor: 'var(--bg-card)',
      borderBottom: '1px solid var(--border)',
      padding: 'var(--spacing-md) var(--spacing-lg)',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'space-between',
      gap: 'var(--spacing-md)',
      position: 'sticky',
      top: 0,
      zIndex: 100,
    }}>
      <Link to="/" style={{
        fontSize: '1.5rem',
        fontWeight: 700,
        color: 'var(--primary)',
        textDecoration: 'none',
      }}>
        RecEngine
      </Link>

      <nav style={{
        display: 'flex',
        gap: 'var(--spacing-md)',
        alignItems: 'center',
      }} className="hide-mobile">
        <Link to="/" style={{ color: 'var(--text)', textDecoration: 'none', fontSize: '0.9rem' }}>Home</Link>
        <Link to="/items" style={{ color: 'var(--text)', textDecoration: 'none', fontSize: '0.9rem' }}>Items</Link>
        <Link to="/recommendations" style={{ color: 'var(--text)', textDecoration: 'none', fontSize: '0.9rem' }}>Recommendations</Link>
        <Link to="/dashboard" style={{ color: 'var(--text)', textDecoration: 'none', fontSize: '0.9rem' }}>Dashboard</Link>
        <Link to="/profile" style={{ color: 'var(--text)', textDecoration: 'none', fontSize: '0.9rem' }}>Profile</Link>
      </nav>

      <div style={{ flex: 1, maxWidth: 400 }} className="hide-mobile">
        <SearchBar onSearch={() => {}} placeholder="Search items..." />
      </div>

      <button
        onClick={() => setMenuOpen(!menuOpen)}
        style={{
          background: 'none',
          border: 'none',
          color: 'var(--text)',
          fontSize: '1.5rem',
          cursor: 'pointer',
        }}
        className="show-mobile hide-desktop"
      >
        {menuOpen ? '✕' : '☰'}
      </button>

      {menuOpen && (
        <div style={{
          position: 'absolute',
          top: '100%',
          left: 0,
          right: 0,
          backgroundColor: 'var(--bg-card)',
          borderBottom: '1px solid var(--border)',
          padding: 'var(--spacing-md)',
          display: 'flex',
          flexDirection: 'column',
          gap: 'var(--spacing-sm)',
        }}>
          <Link to="/" onClick={() => setMenuOpen(false)}>Home</Link>
          <Link to="/items" onClick={() => setMenuOpen(false)}>Items</Link>
          <Link to="/recommendations" onClick={() => setMenuOpen(false)}>Recommendations</Link>
          <Link to="/dashboard" onClick={() => setMenuOpen(false)}>Dashboard</Link>
          <Link to="/profile" onClick={() => setMenuOpen(false)}>Profile</Link>
          <Link to="/settings" onClick={() => setMenuOpen(false)}>Settings</Link>
          <Link to="/compare" onClick={() => setMenuOpen(false)}>Compare</Link>
        </div>
      )}
    </header>
  );
}
