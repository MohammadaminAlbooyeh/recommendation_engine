import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

function App() {
  const [items, setItems] = useState([]);
  const [recommendations, setRecommendations] = useState([]);
  const [userId, setUserId] = useState(1);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchItems();
  }, []);

  const fetchItems = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/items`);
      setItems(response.data);
    } catch (error) {
      console.error("Error fetching items:", error);
    }
  };

  const fetchRecommendations = async () => {
    setLoading(true);
    try {
      const response = await axios.get(`${API_BASE_URL}/recommendations/${userId}`);
      setRecommendations(response.data);
    } catch (error) {
      console.error("Error fetching recommendations:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleRate = async (itemId, rating) => {
    try {
      await axios.post(`${API_BASE_URL}/ratings`, {
        user_id: userId,
        item_id: itemId,
        rating: rating
      });
      alert("Rating submitted!");
    } catch (error) {
      console.error("Error submitting rating:", error);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Recommendation Engine</h1>
        <div className="user-selector">
          <label>User ID: </label>
          <input 
            type="number" 
            value={userId} 
            onChange={(e) => setUserId(parseInt(e.target.value))} 
          />
          <button onClick={fetchRecommendations}>Get Recommendations</button>
        </div>
      </header>

      <main>
        <section className="recommendations">
          <h2>Your Recommendations</h2>
          {loading ? <p>Loading...</p> : (
            <ul>
              {recommendations.map(item => (
                <li key={item.id}>{item.title} ({item.genre})</li>
              ))}
              {recommendations.length === 0 && !loading && <p>No recommendations yet. Rate some movies!</p>}
            </ul>
          )}
        </section>

        <section className="all-items">
          <h2>All Movies</h2>
          <div className="item-grid">
            {items.map(item => (
              <div key={item.id} className="item-card">
                <h3>{item.title}</h3>
                <p>{item.genre}</p>
                <div className="rating-buttons">
                  {[1, 2, 3, 4, 5].map(r => (
                    <button key={r} onClick={() => handleRate(item.id, r)}>{r}★</button>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;
