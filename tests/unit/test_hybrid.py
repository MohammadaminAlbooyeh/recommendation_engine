class WeightedHybrid:
    def __init__(self):
        self.models = []
    def add_model(self, model, weight):
        self.models.append((model, weight))
    def fit(self, df):
        for model, _ in self.models:
            model.fit(df)
    def recommend(self, user_id, n=10):
        return []

class Ensemble:
    def __init__(self):
        self.models = []
    def add_model(self, model):
        self.models.append(model)
    def fit(self, df):
        for model in self.models:
            model.fit(df)
    def recommend(self, user_id, n=10):
        return []

class Stacking:
    def __init__(self):
        self.base_models = []
        self.meta_model = None
    def add_base_model(self, model):
        self.base_models.append(model)
    def set_meta_model(self, model):
        self.meta_model = model
    def fit(self, df):
        for model in self.base_models:
            model.fit(df)
    def recommend(self, user_id, n=10):
        return []

class TestHybrid:
    def test_weighted_hybrid_interface(self):
        hybrid = WeightedHybrid()
        assert hasattr(hybrid, 'fit')
        assert hasattr(hybrid, 'recommend')
        assert hasattr(hybrid, 'add_model')

    def test_ensemble_interface(self):
        ensemble = Ensemble()
        assert hasattr(ensemble, 'fit')
        assert hasattr(ensemble, 'recommend')
        assert hasattr(ensemble, 'add_model')

    def test_stacking_interface(self):
        stacking = Stacking()
        assert hasattr(stacking, 'fit')
        assert hasattr(stacking, 'recommend')
        assert hasattr(stacking, 'add_base_model')
        assert hasattr(stacking, 'set_meta_model')
