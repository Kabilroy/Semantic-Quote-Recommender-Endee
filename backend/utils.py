import os
import pandas as pd
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings

# Get absolute paths relative to this file's location
# Get absolute paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Go to project root
BASE_DIR = os.path.dirname(SCRIPT_DIR)

# Correct path to CSV
DATA_PATH = os.path.join(BASE_DIR, "data", "quotes.csv")

# Vector DB stays in backend
CHROMA_PATH = os.path.join(SCRIPT_DIR, "vectordb")

# Create vectordb directory if it doesn't exist
os.makedirs(CHROMA_PATH, exist_ok=True)

# Load model (downloads automatically first time)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Initialize ChromaDB
client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = client.get_or_create_collection(name="quotes")

def load_and_embed_quotes():
    if collection.count() > 0:
        print(f"✅ Vector DB already contains {collection.count()} quotes.")
        return

    print(f"Loading quotes from {DATA_PATH}...")
    
    if not os.path.exists(DATA_PATH):
        print(f"❌ Error: {DATA_PATH} not found!")
        return
    
    df = pd.read_csv(DATA_PATH, encoding='utf-8-sig')

# Clean column names
    df.columns = df.columns.str.strip().str.lower()

    documents = df['quote'].fillna("").tolist()
    metadatas = df[['author', 'tags']].fillna("").to_dict('records')
    ids = [str(i) for i in range(len(documents))]

    # Generate embeddings
    print("Generating embeddings...")
    embeddings = model.encode(documents, show_progress_bar=True).tolist()

    # Add to Chroma
    collection.add(
        embeddings=embeddings,
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )
    print(f"✅ Successfully added {len(documents)} quotes to vector DB.")


def search_quotes(query: str, top_k: int = 5):
    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=["documents", "metadatas", "distances"]
    )

    quotes = []
    for i in range(len(results['documents'][0])):
        quotes.append({
            "quote": results['documents'][0][i],
            "author": results['metadatas'][0][i]['author'],
            "tags": results['metadatas'][0][i].get('tags', ''),
            "similarity": round(1 / (1 + results['distances'][0][i]), 4)  # higher = better
        })
    return quotes
df = pd.read_csv(DATA_PATH)

print("COLUMNS:", df.columns)