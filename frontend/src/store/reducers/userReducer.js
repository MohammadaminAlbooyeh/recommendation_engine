import { SET_USER, UPDATE_PREFERENCES } from '../actions/userActions';

const initialState = {
  user: null,
  preferences: {
    favoriteGenres: [],
    ratingRange: [1, 5],
    notifications: true,
  },
};

export function userReducer(state = initialState, action) {
  switch (action.type) {
    case SET_USER:
      return { ...state, user: action.payload };
    case UPDATE_PREFERENCES:
      return { ...state, preferences: { ...state.preferences, ...action.payload } };
    default:
      return state;
  }
}
