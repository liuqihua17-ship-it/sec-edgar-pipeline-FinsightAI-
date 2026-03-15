import faiss
import numpy as np
import pickle
from pathlib import Path

INDEX_DIR = Path("data/index")

embeddings = np.load(INDEX_DIR / "embeddings.npy")

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

faiss.write_index(index, str(INDEX_DIR / "faiss_index.bin"))

print("FAISS index saved")