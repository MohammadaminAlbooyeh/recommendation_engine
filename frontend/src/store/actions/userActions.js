export const SET_USER = 'SET_USER';
export const UPDATE_PREFERENCES = 'UPDATE_PREFERENCES';

export function setUser(user) {
  return { type: SET_USER, payload: user };
}

export function updatePreferences(preferences) {
  return { type: UPDATE_PREFERENCES, payload: preferences };
}
