# Recommendation Algorithms

## Collaborative Filtering

### Matrix Factorization
- Cosine similarity-based item-item collaborative filtering
- Sparse matrix representation with scipy CSR
- Weighted average of similarity scores

### User-Based CF
- Finds similar users using cosine similarity
- Aggregates ratings from nearest neighbors

### Item-Based CF
- Computes item-item similarity matrix
- Recommends items similar to user's rated items

### ALS (Alternating Least Squares)
- Matrix factorization with regularization
- Alternating optimization of user/item factors
- Supports configurable latent factors and iterations

### Deep Learning CF
- MLP-based collaborative filtering
- User and item embeddings as input
- Configurable hidden layer architecture

## Content-Based

### TF-IDF Recommender
- Uses TF-IDF vectorization on item descriptions/genres
- Builds user profile from rated items
- Recommends items with similar text profiles

### Content Similarity
- Combines genre one-hot encoding with TF-IDF descriptions
- Cosine similarity between item feature vectors

### Embedding Recommender
- Truncated SVD on similarity matrix
- Generates dense item embeddings
- Cosine similarity in embedding space

### Content-Based Hybrid
- Weighted combination of TF-IDF and embedding recommenders
- Configurable weights per model

## Hybrid Systems

### Weighted Hybrid
- Combines multiple models with configurable weights
- Reciprocal rank fusion scoring

### Ensemble (Voting)
- Majority voting across multiple models
- Each model recommends, votes are aggregated

### Stacking
- Meta-model learns to combine base model predictions
- Logistic regression as default meta-model
- Feature engineering from base model ranks

### Context-Aware
- Incorporates time-based context (hour, day of week)
- Combines collaborative filtering with context bonus

## Advanced

### Sequential Recommender
- Markov chain-based sequential prediction
- Configurable order for sequence length
- Handles cold-start via popularity fallback

### Session-Based
- Co-occurrence matrix within sliding windows
- Session-aware recommendations
- Fallback to popularity for new sessions

### Knowledge Graph
- Multi-modal similarity (text, genre, title)
- Weighted fusion of similarity matrices
- Graph-based propagation of user preferences

### Transformer CF
- Attention-weighted neighborhood aggregation
- MLP with attention features (user/item norms, attended ratings)
- Combines collaborative and content signals

### Neural CF (GMF + MLP)
- Dual-tower architecture (GMF and MLP)
- Element-wise product for GMF path
- Concatenation + dense layers for MLP path
- Ensemble of both outputs
