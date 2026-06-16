import React from 'react';
import { useLocalStorage } from '../hooks/useLocalStorage';
import SuccessMessage from '../components/SuccessMessage';

export default function SettingsPage() {
  const [theme, setTheme] = useLocalStorage('theme', 'dark');
  const [notifications, setNotifications] = useLocalStorage('notifications', true);
  const [defaultRecCount, setDefaultRecCount] = useLocalStorage('defaultRecCount', 10);
  const [algorithm, setAlgorithm] = useLocalStorage('algorithm', 'default');
  const [saved, setSaved] = React.useState(false);

  const handleSave = () => {
    setSaved(true);
    setTimeout(() => setSaved(false), 2000);
  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--spacing-lg)' }}>
      <h1 style={{ color: 'var(--text)', fontSize: '1.5rem', fontWeight: 700 }}>Settings</h1>

      {saved && <SuccessMessage message="Settings saved!" onClose={() => setSaved(false)} />}

      <div style={{
        backgroundColor: 'var(--bg-card)',
        borderRadius: 'var(--radius-lg)',
        padding: 'var(--spacing-lg)',
        display: 'flex',
        flexDirection: 'column',
        gap: 'var(--spacing-md)',
      }}>
        <div>
          <label style={{ color: 'var(--text-muted)', fontSize: '0.85rem', display: 'block', marginBottom: 'var(--spacing-xs)' }}>
            Theme
          </label>
          <select
            value={theme}
            onChange={(e) => setTheme(e.target.value)}
            style={{
              padding: '8px 12px',
              borderRadius: 'var(--radius-sm)',
              border: '1px solid var(--border)',
              backgroundColor: 'var(--bg)',
              color: 'var(--text)',
              width: 200,
            }}
          >
            <option value="dark">Dark</option>
            <option value="light">Light</option>
            <option value="system">System</option>
          </select>
        </div>

        <div>
          <label style={{ display: 'flex', alignItems: 'center', gap: 'var(--spacing-sm)', color: 'var(--text)', fontSize: '0.9rem' }}>
            <input
              type="checkbox"
              checked={notifications}
              onChange={(e) => setNotifications(e.target.checked)}
            />
            Enable notifications
          </label>
        </div>

        <div>
          <label style={{ color: 'var(--text-muted)', fontSize: '0.85rem', display: 'block', marginBottom: 'var(--spacing-xs)' }}>
            Default Recommendation Count
          </label>
          <input
            type="number"
            min={1}
            max={50}
            value={defaultRecCount}
            onChange={(e) => setDefaultRecCount(parseInt(e.target.value) || 10)}
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
          <label style={{ color: 'var(--text-muted)', fontSize: '0.85rem', display: 'block', marginBottom: 'var(--spacing-xs)' }}>
            Default Algorithm
          </label>
          <select
            value={algorithm}
            onChange={(e) => setAlgorithm(e.target.value)}
            style={{
              padding: '8px 12px',
              borderRadius: 'var(--radius-sm)',
              border: '1px solid var(--border)',
              backgroundColor: 'var(--bg)',
              color: 'var(--text)',
              width: 200,
            }}
          >
            <option value="default">Default</option>
            <option value="collaborative">Collaborative Filtering</option>
            <option value="content">Content-Based</option>
            <option value="hybrid">Hybrid</option>
          </select>
        </div>

        <button
          onClick={handleSave}
          style={{
            alignSelf: 'flex-start',
            padding: '10px 24px',
            borderRadius: 'var(--radius-md)',
            border: 'none',
            backgroundColor: 'var(--primary)',
            color: '#fff',
            fontWeight: 600,
            cursor: 'pointer',
            fontSize: '0.9rem',
          }}
        >
          Save Settings
        </button>
      </div>
    </div>
  );
}
