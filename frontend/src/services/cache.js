const cache = new Map();

export function get(key) {
  const entry = cache.get(key);
  if (!entry) return null;
  if (Date.now() > entry.expiry) {
    cache.delete(key);
    return null;
  }
  return entry.value;
}

export function set(key, value, ttl = 300000) {
  cache.set(key, {
    value,
    expiry: Date.now() + ttl,
  });
}

export function clear() {
  cache.clear();
}
