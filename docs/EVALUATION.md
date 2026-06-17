# Evaluation Metrics

## Core Metrics

- **Precision@K**: Fraction of recommended items that are relevant
- **Recall@K**: Fraction of relevant items that are recommended
- **F1@K**: Harmonic mean of precision and recall
- **RMSE**: Root mean squared error for rating prediction
- **MAE**: Mean absolute error for rating prediction

## Ranking Metrics

- **NDCG@K**: Normalized Discounted Cumulative Gain
- **MRR@K**: Mean Reciprocal Rank
- **Hit Rate@K**: Whether any relevant item is in top-K
- **MAP**: Mean Average Precision across users

## Diversity Metrics

- **Coverage**: Fraction of catalog items recommended
- **Intra-list Similarity**: Average similarity among recommended items
- **Diversity Score**: 1 - Intra-list Similarity
- **Catalog Coverage**: Overall catalog coverage across all users

## Serendipity Metrics

- **Unexpectedness**: Fraction of recommendations not expected from user history
- **Serendipity Score**: Fraction of unexpected recommendations that are relevant
- **Novelty**: Average negative log popularity of recommendations

## A/B Testing

- Statistical significance testing with Welch's t-test
- Configurable control/treatment variants
- Metric comparison with relative change reporting
