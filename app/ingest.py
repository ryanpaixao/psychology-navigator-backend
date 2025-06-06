# Data ingestion and embedding
import pandas as pd
import faiss
from sentence_transformers import SentenceTransformer
from pathlib import Path

MODEL = SentenceTransformer('all-MiniLM-L6-v2')
DATA_PATH = Path("app/db/data.csv")
INDEX_PATH = Path("app/db/faiss_index")
INDEX_PATH.mkdir(parents=True, exist_ok=True)

def build_index():
    df = pd.read_csv(DATA_PATH)
    embeddings = MODEL.encode(df["abstract"].tolist())
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    faiss.write_index(index, str(INDEX_PATH / "index.faiss"))

if __name__ == "__main__":
    build_index()