# A/B Testing

## Overview

The A/B testing framework allows comparing recommendation algorithms in production.

## Running an Experiment

```bash
python scripts/a_b_test.py
```

## Framework

- **Control**: Current production algorithm
- **Treatment**: New algorithm to evaluate
- **Metric**: Configurable success metric (precision, recall, clicks, etc.)
- **Statistical Test**: Welch's t-test for significance

## Interpreting Results

- p < 0.05: Statistically significant difference
- Relative change: Percentage improvement over control
- Run experiments for sufficient duration to gather data
- Consider novelty effect when deploying new algorithms
