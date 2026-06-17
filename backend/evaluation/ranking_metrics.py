import math
from typing import List


def ndcg_at_k(recommended: List[int], relevant: List[int], k: int) -> float:
    dcg = 0.0
    for i, item in enumerate(recommended[:k]):
        if item in relevant:
            dcg += 1.0 / math.log2(i + 2)
    idcg = sum(1.0 / math.log2(i + 2) for i in range(min(k, len(relevant))))
    return dcg / idcg if idcg > 0 else 0.0


def mrr_at_k(recommended: List[int], relevant: List[int], k: int) -> float:
    for i, item in enumerate(recommended[:k]):
        if item in relevant:
            return 1.0 / (i + 1)
    return 0.0


def mean_reciprocal_rank(recommendations: List[List[int]], relevant_sets: List[List[int]], k: int = 10) -> float:
    if not recommendations:
        return 0.0
    rr_sum = sum(mrr_at_k(rec, rel, k) for rec, rel in zip(recommendations, relevant_sets))
    return rr_sum / len(recommendations)


def hit_rate_at_k(recommended: List[int], relevant: List[int], k: int) -> float:
    return 1.0 if len(set(recommended[:k]) & set(relevant)) > 0 else 0.0
