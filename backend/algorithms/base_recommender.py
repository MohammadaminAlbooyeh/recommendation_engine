from abc import ABC, abstractmethod
import pandas as pd

class BaseRecommender(ABC):
    @abstractmethod
    def fit(self, df: pd.DataFrame):
        pass

    @abstractmethod
    def recommend(self, user_id, n: int = 10):
        pass
