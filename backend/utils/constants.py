DEFAULT_RECOMMENDATION_COUNT = 10
MAX_RECOMMENDATION_COUNT = 100

RATING_MIN = 1.0
RATING_MAX = 5.0
RATING_STEP = 0.5

SIMILARITY_METRICS = ["cosine", "pearson", "euclidean"]
CACHE_STRATEGIES = ["lru", "ttl", "fifo"]

RECOMMENDATION_ALGORITHMS = [
    "matrix_factorization",
    "user_based_cf",
    "item_based_cf",
    "als",
    "content_based",
    "weighted_hybrid",
    "ensemble",
]

EVENT_TYPES = ["view", "rate", "purchase", "click", "search"]
