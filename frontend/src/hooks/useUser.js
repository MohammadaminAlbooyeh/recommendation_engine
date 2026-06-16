import { useCallback } from 'react';
import { useStore } from '../store/store';
import { setUser, updatePreferences } from '../store/actions/userActions';

export function useUser() {
  const { state, dispatch } = useStore();

  const handleSetUser = useCallback(
    (user) => {
      dispatch(setUser(user));
    },
    [dispatch]
  );

  const handleUpdatePreferences = useCallback(
    (preferences) => {
      dispatch(updatePreferences(preferences));
    },
    [dispatch]
  );

  return {
    user: state.user.user,
    preferences: state.user.preferences,
    setUser: handleSetUser,
    updatePreferences: handleUpdatePreferences,
  };
}
