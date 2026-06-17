import random
import numpy as np
from typing import Callable, Dict, List, Any
from scipy import stats


def assign_variant(user_id: int, variants: List[str]) -> str:
    return random.choice(variants)


def compute_metric_difference(
    control_metrics: List[float],
    treatment_metrics: List[float]
) -> Dict[str, Any]:
    control_mean = np.mean(control_metrics)
    treatment_mean = np.mean(treatment_metrics)
    diff = treatment_mean - control_mean
    t_stat, p_value = stats.ttest_ind(treatment_metrics, control_metrics, equal_var=False)
    return {
        "control_mean": float(control_mean),
        "treatment_mean": float(treatment_mean),
        "difference": float(diff),
        "relative_change": float(diff / control_mean * 100) if control_mean != 0 else 0.0,
        "t_statistic": float(t_stat),
        "p_value": float(p_value),
        "significant": p_value < 0.05,
    }


def run_experiment(
    control_func: Callable,
    treatment_func: Callable,
    test_users: List[int],
    metric_func: Callable
) -> Dict[str, Any]:
    control_metrics = []
    treatment_metrics = []
    for user_id in test_users:
        variant = assign_variant(user_id, ["control", "treatment"])
        if variant == "control":
            result = control_func(user_id)
            control_metrics.append(metric_func(result))
        else:
            result = treatment_func(user_id)
            treatment_metrics.append(metric_func(result))
    return compute_metric_difference(control_metrics, treatment_metrics)
