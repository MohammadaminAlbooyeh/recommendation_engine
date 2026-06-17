import os


class ModelConfig:
    MODELS_DIR: str = os.getenv("MODELS_DIR", "models")
    COLLABORATIVE_FILTERING_PATH: str = os.path.join(MODELS_DIR, "collaborative_filtering_model.pkl")
    CONTENT_BASED_PATH: str = os.path.join(MODELS_DIR, "content_based_model.pkl")
    EMBEDDINGS_PATH: str = os.path.join(MODELS_DIR, "embeddings_model.bin")
    ENSEMBLE_PATH: str = os.path.join(MODELS_DIR, "ensemble_model.pkl")
    NEURAL_NETWORK_PATH: str = os.path.join(MODELS_DIR, "trained_neural_network.h5")
    AUTO_SAVE: bool = os.getenv("AUTO_SAVE_MODELS", "true").lower() == "true"


model_config = ModelConfig()
