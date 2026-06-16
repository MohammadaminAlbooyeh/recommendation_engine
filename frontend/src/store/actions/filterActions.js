export const SET_GENRE_FILTER = 'SET_GENRE_FILTER';
export const SET_RATING_FILTER = 'SET_RATING_FILTER';
export const SET_SEARCH_QUERY = 'SET_SEARCH_QUERY';

export function setGenreFilter(genres) {
  return { type: SET_GENRE_FILTER, payload: genres };
}

export function setRatingFilter(rating) {
  return { type: SET_RATING_FILTER, payload: rating };
}

export function setSearchQuery(query) {
  return { type: SET_SEARCH_QUERY, payload: query };
}
