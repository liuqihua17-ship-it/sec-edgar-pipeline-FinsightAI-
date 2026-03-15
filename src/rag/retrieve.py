import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer
from pathlib import Path

INDEX_DIR = Path("data/index")

model = SentenceTransformer("all-MiniLM-L6-v2")

index = faiss.read_index(str(INDEX_DIR / "faiss_index.bin"))

with open(INDEX_DIR / "metadata.pkl", "rb") as f:
    metadata = pickle.load(f)


def search(query, top_k=5):
    q_embedding = model.encode([query])
    distances, indices = index.search(q_embedding, top_k)

    results = []

    for idx in indices[0]:
        results.append(metadata[idx])

    return results