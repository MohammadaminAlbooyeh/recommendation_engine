import React, { useState, useEffect } from 'react';
import { Routes, Route } from 'react-router-dom';
import './App.css';
import './styles/index.css';

import { StoreProvider } from './store/store';

import Header from './components/Header';
import Sidebar from './components/Sidebar';

import HomePage from './pages/HomePage';
import ItemsPage from './pages/ItemsPage';
import ItemDetailPage from './pages/ItemDetailPage';
import RecommendationsPage from './pages/RecommendationsPage';
import DashboardPage from './pages/DashboardPage';
import SearchPage from './pages/SearchPage';
import ProfilePage from './pages/ProfilePage';
import SettingsPage from './pages/SettingsPage';
import ComparisonPage from './pages/ComparisonPage';

function App() {
  const [sidebarOpen, setSidebarOpen] = useState(true);
  const [filters, setFilters] = useState({
    genres: [],
    ratingRange: [1, 5],
    searchQuery: '',
  });

  useEffect(() => {
    const handleResize = () => {
      if (window.innerWidth < 768) setSidebarOpen(false);
    };
    handleResize();
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  return (
    <StoreProvider>
      <div className="App" style={{
        display: 'flex',
        flexDirection: 'column',
        minHeight: '100vh',
        backgroundColor: 'var(--bg)',
      }}>
        <Header />

        <div style={{
          display: 'flex',
          flex: 1,
          position: 'relative',
        }}>
          <Sidebar
            filters={filters}
            onFilterChange={setFilters}
            collapsed={!sidebarOpen}
            onToggle={() => setSidebarOpen(!sidebarOpen)}
          />

          <main style={{
            flex: 1,
            padding: 'var(--spacing-lg)',
            maxWidth: 1200,
            margin: '0 auto',
            width: '100%',
          }}>
            <Routes>
              <Route path="/" element={<HomePage />} />
              <Route path="/items" element={<ItemsPage />} />
              <Route path="/items/:id" element={<ItemDetailPage />} />
              <Route path="/recommendations" element={<RecommendationsPage />} />
              <Route path="/dashboard" element={<DashboardPage />} />
              <Route path="/search" element={<SearchPage />} />
              <Route path="/profile" element={<ProfilePage />} />
              <Route path="/settings" element={<SettingsPage />} />
              <Route path="/compare" element={<ComparisonPage />} />
            </Routes>
          </main>
        </div>
      </div>
    </StoreProvider>
  );
}

export default App;
