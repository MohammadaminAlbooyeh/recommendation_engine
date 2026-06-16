import React, { useState, useCallback, useEffect } from 'react';

export function useNotification() {
  const [notifications, setNotifications] = useState([]);

  const notify = useCallback((message, type = 'info', duration = 3000) => {
    const id = Date.now();
    setNotifications((prev) => [...prev, { id, message, type }]);
    setTimeout(() => {
      setNotifications((prev) => prev.filter((n) => n.id !== id));
    }, duration);
  }, []);

  const dismiss = useCallback((id) => {
    setNotifications((prev) => prev.filter((n) => n.id !== id));
  }, []);

  const NotificationComponent = () => {
    if (notifications.length === 0) return null;
    return (
      <div style={{ position: 'fixed', top: 16, right: 16, zIndex: 1000, display: 'flex', flexDirection: 'column', gap: 8 }}>
        {notifications.map((n) => (
          <div
            key={n.id}
            onClick={() => dismiss(n.id)}
            style={{
              padding: '12px 16px',
              borderRadius: 8,
              color: '#fff',
              cursor: 'pointer',
              backgroundColor: n.type === 'error' ? '#ef4444' : n.type === 'success' ? '#22c55e' : '#3b82f6',
              boxShadow: '0 4px 6px rgba(0,0,0,0.3)',
              animation: 'slideIn 0.3s ease',
            }}
          >
            {n.message}
          </div>
        ))}
      </div>
    );
  };

  return { notify, NotificationComponent };
}
