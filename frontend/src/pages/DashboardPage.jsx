import React from 'react';
import { useItems } from '../hooks/useItems';
import PopularItems from '../charts/PopularItems';
import RatingDistribution from '../charts/RatingDistribution';
import UserActivity from '../charts/UserActivity';
import EngagementMetrics from '../charts/EngagementMetrics';

export default function DashboardPage() {
  const { items } = useItems();

  const popularItemsData = items.slice(0, 5).map((item) => ({
    name: item.title,
    count: Math.floor(Math.random() * 50) + 5,
  }));

  const ratingDistData = [1, 2, 3, 4, 5].map((r) => ({
    rating: r,
    count: items.filter((i) => Math.floor(Math.random() * 5) + 1 === r).length || Math.floor(Math.random() * 20) + 5,
  }));

  const activityData = Array.from({ length: 30 }, (_, i) => ({
    date: `Day ${i + 1}`,
    count: Math.floor(Math.random() * 15),
  }));

  const engagementData = Array.from({ length: 12 }, (_, i) => ({
    label: `W${i + 1}`,
    value: Math.floor(Math.random() * 100) + 20,
  }));

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: 'var(--spacing-lg)' }}>
      <h1 style={{ color: 'var(--text)', fontSize: '1.5rem', fontWeight: 700 }}>Dashboard</h1>

      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
        gap: 'var(--spacing-md)',
      }}>
        <div style={{ backgroundColor: 'var(--bg-card)', borderRadius: 'var(--radius-lg)', padding: 'var(--spacing-md)', textAlign: 'center' }}>
          <p style={{ color: 'var(--text-muted)', fontSize: '0.85rem' }}>Total Items</p>
          <p style={{ color: 'var(--text)', fontSize: '2rem', fontWeight: 700 }}>{items.length}</p>
        </div>
        <div style={{ backgroundColor: 'var(--bg-card)', borderRadius: 'var(--radius-lg)', padding: 'var(--spacing-md)', textAlign: 'center' }}>
          <p style={{ color: 'var(--text-muted)', fontSize: '0.85rem' }}>Ratings</p>
          <p style={{ color: 'var(--text)', fontSize: '2rem', fontWeight: 700 }}>--</p>
        </div>
        <div style={{ backgroundColor: 'var(--bg-card)', borderRadius: 'var(--radius-lg)', padding: 'var(--spacing-md)', textAlign: 'center' }}>
          <p style={{ color: 'var(--text-muted)', fontSize: '0.85rem' }}>Avg Rating</p>
          <p style={{ color: 'var(--text)', fontSize: '2rem', fontWeight: 700 }}>--</p>
        </div>
        <div style={{ backgroundColor: 'var(--bg-card)', borderRadius: 'var(--radius-lg)', padding: 'var(--spacing-md)', textAlign: 'center' }}>
          <p style={{ color: 'var(--text-muted)', fontSize: '0.85rem' }}>Users</p>
          <p style={{ color: 'var(--text)', fontSize: '2rem', fontWeight: 700 }}>--</p>
        </div>
      </div>

      <div style={{
        display: 'grid',
        gridTemplateColumns: 'repeat(auto-fit, minmax(350px, 1fr))',
        gap: 'var(--spacing-md)',
      }}>
        <PopularItems data={popularItemsData} />
        <RatingDistribution data={ratingDistData} />
        <EngagementMetrics data={engagementData} />
        <UserActivity data={activityData} />
      </div>
    </div>
  );
}
