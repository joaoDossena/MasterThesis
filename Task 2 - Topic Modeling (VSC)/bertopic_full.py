import pandas as pd
from bertopic import BERTopic

df = pd.read_csv("tatoeba_with_preds.csv")

print(df.head())
docs = df["PT"]

# Load model
# topic_model = BERTopic.load("bertopic_portuguese_tatoeba")
print("Loading model...")
topic_model = BERTopic(language="portuguese", calculate_probabilities=True, verbose=True)
print("Model loaded. Fitting model to data...")
topics, probs = topic_model.fit_transform(docs)

print("Model fitted. Saving model...")
topic_model.save("bertopic_portuguese_tatoeba_full_model")
print("Model saved!!")