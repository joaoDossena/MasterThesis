import pandas as pd
from bertopic import BERTopic
from cuml.manifold import UMAP
from cuml.cluster import HDBSCAN


df = pd.read_csv("tatoeba_with_preds.csv")

print(df.head())
docs = df["PT"]

# Load model
# topic_model = BERTopic.load("bertopic_portuguese_tatoeba")

print("Instantiating custom UMAP...")
umap_model = UMAP(n_components=5, n_neighbors=15, min_dist=0.0)
print("Instantiating custom HDBSCAN...")
hdbscan_model = HDBSCAN(min_samples=10, gen_min_span_tree=True, prediction_data=True)
print("Loading model...")
topic_model = BERTopic(language="portuguese", umap_model=umap_model, hdbscan_model=hdbscan_model, calculate_probabilities=True, verbose=True)
print("Model loaded. Fitting model to data...")
topics, probs = topic_model.fit_transform(docs)

print("Model fitted. Saving model...")
topic_model.save("bertopic_portuguese_tatoeba_full_model")
print("Model saved!!")
print("Saving topics...")
pd.DataFrame(topics).to_pickle("topics.pkl")
print("Saving probabilities...")
pd.DataFrame(probs).to_pickle("probs.pkl")
