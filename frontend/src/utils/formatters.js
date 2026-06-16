export function formatRating(rating) {
  return Number(rating).toFixed(1);
}

export function truncateText(text, maxLength = 100) {
  if (!text || text.length <= maxLength) return text || '';
  return text.slice(0, maxLength).trimEnd() + '...';
}

export function pluralize(count, singular, plural) {
  return count === 1 ? singular : plural || `${singular}s`;
}
