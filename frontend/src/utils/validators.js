export function validateEmail(email) {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(email);
}

export function validateRating(rating) {
  return Number.isFinite(rating) && rating >= 1 && rating <= 5;
}

export function validateUserId(userId) {
  return Number.isInteger(userId) && userId > 0;
}
