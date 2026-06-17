class AlgorithmConfig:
    MATRIX_FACTORIZATION = {"n_factors": 20, "regularization": 0.1, "n_iterations": 15}
    ALS = {"n_factors": 20, "regularization": 0.1, "n_iterations": 15}
    USER_BASED_CF = {"similarity": "cosine"}
    ITEM_BASED_CF = {"similarity": "cosine"}
    DEEP_LEARNING_CF = {"hidden_layers": [64, 32], "max_iter": 200}
    CONTENT_BASED = {"tfidf_max_features": 100, "n_components": 20}
    WEIGHTED_HYBRID = {"default_weights": None}
    ENSEMBLE = {"voting": "majority"}
    STACKING = {"meta_model": "logistic_regression"}
    SEQUENTIAL = {"order": 1}
    SESSION_BASED = {"window_size": 3}
    TRANSFORMER_CF = {"attention_heads": 1, "hidden_layers": [32, 16]}
    NEURAL_CF = {"gmf_layers": [16, 8], "mlp_layers": [64, 32, 16]}


algorithm_config = AlgorithmConfig()
