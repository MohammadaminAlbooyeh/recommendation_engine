import { SET_ITEMS, SET_LOADING, SET_ERROR } from '../actions/itemActions';

const initialState = {
  items: [],
  loading: false,
  error: null,
};

export function itemReducer(state = initialState, action) {
  switch (action.type) {
    case SET_ITEMS:
      return { ...state, items: action.payload, loading: false, error: null };
    case SET_LOADING:
      return { ...state, loading: action.payload };
    case SET_ERROR:
      return { ...state, error: action.payload, loading: false };
    default:
      return state;
  }
}
