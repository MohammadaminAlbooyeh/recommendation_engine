class RecommendationEngineError(Exception):
    pass


class ModelNotFittedError(RecommendationEngineError):
    def __init__(self, message="Model has not been fitted yet. Call fit() first."):
        super().__init__(message)


class InvalidUserError(RecommendationEngineError):
    def __init__(self, user_id, message="User not found"):
        self.user_id = user_id
        super().__init__(f"{message}: {user_id}")


class InvalidItemError(RecommendationEngineError):
    def __init__(self, item_id, message="Item not found"):
        self.item_id = item_id
        super().__init__(f"{message}: {item_id}")


class InsufficientDataError(RecommendationEngineError):
    def __init__(self, message="Insufficient data to generate recommendations"):
        super().__init__(message)


class CacheError(RecommendationEngineError):
    pass


class ValidationError(RecommendationEngineError):
    def __init__(self, field, message):
        self.field = field
        super().__init__(f"Validation error on {field}: {message}")
