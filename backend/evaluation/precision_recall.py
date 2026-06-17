from typing import List


def precision_at_k(recommended: List[int], relevant: List[int], k: int) -> float:
    if k <= 0 or not recommended:
        return 0.0
    top_k = recommended[:k]
    hits = len(set(top_k) & set(relevant))
    return hits / k


def recall_at_k(recommended: List[int], relevant: List[int], k: int) -> float:
    if not relevant or not recommended:
        return 0.0
    top_k = recommended[:k]
    hits = len(set(top_k) & set(relevant))
    return hits / len(relevant)


def average_precision(recommended: List[int], relevant: List[int]) -> float:
    hits = 0
    sum_precisions = 0.0
    for i, item in enumerate(recommended):
        if item in relevant:
            hits += 1
            sum_precisions += hits / (i + 1)
    if hits == 0:
        return 0.0
    return sum_precisions / hits


def mean_average_precision(recommendations: List[List[int]], relevant_sets: List[List[int]]) -> float:
    if not recommendations:
        return 0.0
    aps = [average_prerecision(rec, rel) for rec, rel in zip(recommendations, relevant_sets)]
    return sum(aps) / len(aps)
