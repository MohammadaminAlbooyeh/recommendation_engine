export function getFilteredItems(items, filters) {
  return items.filter((item) => {
    if (filters.genres && filters.genres.length > 0) {
      if (!filters.genres.includes(item.genre)) return false;
    }
    if (filters.searchQuery) {
      const q = filters.searchQuery.toLowerCase();
      if (!item.title.toLowerCase().includes(q) && !item.description?.toLowerCase().includes(q)) return false;
    }
    return true;
  });
}

export function getItemById(items, id) {
  return items.find((item) => item.id === id) || null;
}
