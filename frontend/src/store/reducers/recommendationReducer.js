import { SET_RECOMMENDATIONS, SET_LOADING, SET_ERROR } from '../actions/recommendationActions';

const initialState = {
  recommendations: [],
  loading: false,
  error: null,
};

export function recommendationReducer(state = initialState, action) {
  switch (action.type) {
    case SET_RECOMMENDATIONS:
      return { ...state, recommendations: action.payload, loading: false, error: null };
    case SET_LOADING:
      return { ...state, loading: action.payload };
    case SET_ERROR:
      return { ...state, error: action.payload, loading: false };
    default:
      return state;
  }
}
