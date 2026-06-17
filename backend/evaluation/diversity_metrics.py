from typing import List, Set, Callable
import itertools


def coverage(recommended: List[int], all_items: Set[int]) -> float:
    if not all_items:
        return 0.0
    return len(set(recommended) & all_items) / len(all_items)


def intra_list_similarity(recommended: List[int], similarity_func: Callable) -> float:
    if len(recommended) < 2:
        return 0.0
    sim_sum = 0.0
    count = 0
    for a, b in itertools.combinations(recommended, 2):
        sim_sum += similarity_func(a, b)
        count += 1
    return sim_sum / count if count > 0 else 0.0


def diversity_score(recommended: List[int], similarity_func: Callable) -> float:
    return 1.0 - intra_list_similarity(recommended, similarity_func)


def catalog_coverage(recommended_items: List[List[int]], catalog: Set[int]) -> float:
    recommended_set = set()
    for rec_list in recommended_items:
        recommended_set.update(rec_list)
    return len(recommended_set & catalog) / len(catalog) if catalog else 0.0
