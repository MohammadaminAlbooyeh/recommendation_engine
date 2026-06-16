export function getTopRecommendations(recommendations, n = 10) {
  return recommendations.slice(0, n);
}
