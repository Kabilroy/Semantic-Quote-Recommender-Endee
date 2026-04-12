import os
import pandas as pd
import requests
from sentence_transformers import SentenceTransformer

# Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
DATA_PATH = os.path.join(BASE_DIR, "data", "quotes.csv")

# Endee API URL
ENDEE_URL = "http://localhost:8080"

# Load model
model = SentenceTransformer('all-MiniLM-L6-v2')


def create_index():
    url = f"{ENDEE_URL}/indexes"
    payload = {
        "name": "quotes_index",
        "dimension": 384,
        "space_type": "cosine"
    }
    try:
        requests.post(url, json=payload)
        print("✅ Index created")
    except:
        print("Index may already exist")


def load_and_embed_quotes():
    create_index()

    print(f"Loading quotes from {DATA_PATH}...")

    df = pd.read_csv(DATA_PATH, encoding='utf-8-sig')
    df.columns = df.columns.str.strip().str.lower()

    documents = df['quote'].fillna("").tolist()
    metadatas = df[['author', 'tags']].fillna("").to_dict('records')

    print("Generating embeddings...")
    embeddings = model.encode(documents).tolist()

    vectors = []
    for i, (doc, meta, emb) in enumerate(zip(documents, metadatas, embeddings)):
        vectors.append({
            "id": str(i),
            "vector": emb,
            "meta": {
                "quote": doc,
                "author": meta['author'],
                "tags": meta['tags']
            }
        })

    # Upload to Endee
    url = f"{ENDEE_URL}/indexes/quotes_index/vectors"
    requests.post(url, json={"vectors": vectors})

    print(f"✅ Added {len(vectors)} quotes to Endee")


def search_quotes(query: str, top_k: int = 5):
    query_embedding = model.encode(query).tolist()

    url = f"{ENDEE_URL}/indexes/quotes_index/query"

    payload = {
        "vector": query_embedding,
        "top_k": top_k
    }

    response = requests.post(url, json=payload)
    results = response.json()["results"]

    quotes = []
    for r in results:
        quotes.append({
            "quote": r["meta"]["quote"],
            "author": r["meta"]["author"],
            "tags": r["meta"]["tags"],
            "similarity": round(r["score"], 4)
        })

    return quotes