import pandas as pd
from bertopic import BERTopic
from cuml.manifold import UMAP
from cuml.cluster import HDBSCAN

umap_model = UMAP(n_components=5, n_neighbors=15, min_dist=0.0)
hdbscan_model = HDBSCAN(min_samples=10, gen_min_span_tree=True, prediction_data=True)
topic_model = BERTopic(language="portuguese", umap_model=umap_model, hdbscan_model=hdbscan_model, calculate_probabilities=True, verbose=True)

print(f"All imported correctly")