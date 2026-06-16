import React, { createContext, useContext, useReducer } from 'react';
import { itemReducer } from './reducers/itemReducer';
import { recommendationReducer } from './reducers/recommendationReducer';
import { userReducer } from './reducers/userReducer';
import { filterReducer } from './reducers/filterReducer';

const StoreContext = createContext();

const initialState = {
  items: { items: [], loading: false, error: null },
  recommendations: { recommendations: [], loading: false, error: null },
  user: { user: null, preferences: { favoriteGenres: [], ratingRange: [1, 5], notifications: true } },
  filters: { genres: [], ratingRange: [1, 5], searchQuery: '' },
};

function combineReducers(state, action) {
  return {
    items: itemReducer(state.items, action),
    recommendations: recommendationReducer(state.recommendations, action),
    user: userReducer(state.user, action),
    filters: filterReducer(state.filters, action),
  };
}

export function StoreProvider({ children }) {
  const [state, dispatch] = useReducer(combineReducers, initialState);

  return (
    <StoreContext.Provider value={{ state, dispatch }}>
      {children}
    </StoreContext.Provider>
  );
}

export function useStore() {
  const context = useContext(StoreContext);
  if (!context) {
    throw new Error('useStore must be used within a StoreProvider');
  }
  return context;
}
