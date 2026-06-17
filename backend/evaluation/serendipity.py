from typing import List, Set


def unexpectedness(recommended: List[int], expected: Set[int]) -> float:
    if not recommended:
        return 0.0
    unexpected = [item for item in recommended if item not in expected]
    return len(unexpected) / len(recommended)


def serendipity_score(
    recommended: List[int],
    expected: Set[int],
    relevant: Set[int]
) -> float:
    if not recommended:
        return 0.0
    unexpected_relevant = [
        item for item in recommended
        if item not in expected and item in relevant
    ]
    return len(unexpected_relevant) / len(recommended)


def novelty(item_popularity: dict, recommended: List[int]) -> float:
    if not recommended:
        return 0.0
    from math import log2
    scores = []
    for item in recommended:
        p = item_popularity.get(item, 1)
        scores.append(-log2(p + 1))
    return sum(scores) / len(scores)
