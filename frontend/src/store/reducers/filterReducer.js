import { SET_GENRE_FILTER, SET_RATING_FILTER, SET_SEARCH_QUERY } from '../actions/filterActions';

const initialState = {
  genres: [],
  ratingRange: [1, 5],
  searchQuery: '',
};

export function filterReducer(state = initialState, action) {
  switch (action.type) {
    case SET_GENRE_FILTER:
      return { ...state, genres: action.payload };
    case SET_RATING_FILTER:
      return { ...state, ratingRange: action.payload };
    case SET_SEARCH_QUERY:
      return { ...state, searchQuery: action.payload };
    default:
      return state;
  }
}
