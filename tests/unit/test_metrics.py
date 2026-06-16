import math
import pytest

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

class TestMetrics:
    def test_precision_at_k(self):
        recs = [1, 2, 3, 4, 5]
        relevant = [1, 2, 6]
        assert precision_at_k(recs, relevant, 2) == 1.0
        assert precision_at_k(recs, relevant, 5) == 0.4
        assert precision_at_k(recs, relevant, 0) == 0.0

    def test_recall_at_k(self):
        recs = [1, 2, 3, 4, 5]
        relevant = [1, 2, 6]
        assert recall_at_k(recs, relevant, 2) == 2 / 3
        assert recall_at_k(recs, relevant, 5) == 2 / 3
        assert recall_at_k([], relevant, 3) == 0.0

    def test_rmse(self):
        preds = [3, 4, 5]
        targets = [3, 4, 5]
        assert rmse(preds, targets) == 0.0
        preds2 = [1, 2, 3]
        targets2 = [4, 5, 6]
        assert rmse(preds2, targets2) == pytest.approx(3.0)

    def test_mae(self):
        preds = [3, 4, 5]
        targets = [3, 4, 5]
        assert mae(preds, targets) == 0.0
        preds2 = [1, 2, 3]
        targets2 = [4, 5, 6]
        assert mae(preds2, targets2) == 3.0
