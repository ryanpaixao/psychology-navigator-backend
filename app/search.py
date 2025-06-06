# Search logic (embedding + FAISS)
import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer
from pathlib import Path

MODEL = SentenceTransformer('all-MiniLM-L6-v2')
DATA_PATH = Path("app/db/data.csv")
INDEX_PATH = Path("app/db/faiss_index/index.faiss")

# Load data and index
data = pd.read_csv(DATA_PATH)
index = faiss.read_index(str(INDEX_PATH))

def search_similar(query: str, top_k: int = 5):
    q_embed = MODEL.encode([query])
    scores, ids = index.search(q_embed, top_k)

    results = []
    for i, score in zip(ids[0], scores[0]):
        results.append({
            "title": data.iloc[i]["title"],
            "abstract": data.iloc[i]["abstract"],
            "score": float(score)
        })
    return results