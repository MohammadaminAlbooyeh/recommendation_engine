import math


def precision_at_k(recommended, relevant, k):
    if k <= 0 or not recommended:
        return 0.0
    top_k = recommended[:k]
    hits = len(set(top_k) & set(relevant))
    return hits / k


def recall_at_k(recommended, relevant, k):
    if not relevant or not recommended:
        return 0.0
    top_k = recommended[:k]
    hits = len(set(top_k) & set(relevant))
    return hits / len(relevant)


def rmse(predictions, targets):
    if len(predictions) != len(targets) or len(predictions) == 0:
        return 0.0
    squared_errors = [(p - t) ** 2 for p, t in zip(predictions, targets)]
    return math.sqrt(sum(squared_errors) / len(predictions))


def mae(predictions, targets):
    if len(predictions) != len(targets) or len(predictions) == 0:
        return 0.0
    return sum(abs(p - t) for p, t in zip(predictions, targets)) / len(predictions)


def f1_at_k(precision, recall):
    if precision + recall == 0:
        return 0.0
    return 2 * precision * recall / (precision + recall)
