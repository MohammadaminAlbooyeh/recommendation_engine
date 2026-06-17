from backend.utils.constants import RATING_MIN, RATING_MAX


def validate_rating(rating: float) -> bool:
    return RATING_MIN <= rating <= RATING_MAX


def validate_user_id(user_id: int) -> bool:
    return isinstance(user_id, int) and user_id > 0


def validate_item_id(item_id: int) -> bool:
    return isinstance(item_id, int) and item_id > 0


def validate_recommendation_count(n: int) -> bool:
    return isinstance(n, int) and 1 <= n <= 100
