import os
import pandas as pd
from endee import Endee
from sentence_transformers import SentenceTransformer

# -------------------------------
# Paths
# -------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(SCRIPT_DIR)
DATA_PATH = os.path.join(BASE_DIR, "data", "quotes.csv")

# -------------------------------
# Endee Config
# -------------------------------
INDEX_NAME = "quotes_index"

# Initialize Endee client
client = Endee()

# ✅ LAZY LOADING: Don't load model at import time
_model = None

def get_model():
    """Lazy load the embedding model - download only when needed"""
    global _model
    
    if _model is not None:
        return _model
    
    try:
        print("🔄 Loading embedding model (first time only)...")
        _model = SentenceTransformer("all-MiniLM-L6-v2")
        print("✅ Model loaded successfully")
        return _model
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        print("   Make sure you have internet connection")
        print("   Or run: python -c \"from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')\"")
        return None


# -------------------------------
# Create Index
# -------------------------------
def create_index():
    try:
        print("📋 Creating index...")

        indexes = client.list_indexes()
        index_names = [idx.get('name') for idx in indexes] if indexes else []

        if INDEX_NAME in index_names:
            print(f"   ✅ Index '{INDEX_NAME}' already exists")
            return True

        client.create_index(
            name=INDEX_NAME,
            dimension=384,
            space_type="cosine"
        )

        print(f"   ✅ Index '{INDEX_NAME}' created successfully")
        return True

    except Exception as e:
        if "already exists" in str(e).lower():
            print(f"   ✅ Index '{INDEX_NAME}' already exists")
            return True

        print(f"   ❌ Error creating index: {e}")
        return False


# -------------------------------
# Load + Embed + Upload
# -------------------------------
def load_and_embed_quotes():
    """Load quotes from CSV, generate embeddings, and upload to Endee"""
    
    # Load the model (lazy load)
    model = get_model()
    if model is None:
        print("❌ Cannot proceed without embedding model")
        return []
    
    if not create_index():
        print("⚠️ Skipping upload due to index error")
        return []

    print(f"\n📂 Loading quotes from {DATA_PATH}...")

    if not os.path.exists(DATA_PATH):
        print(f"❌ CSV file not found at {DATA_PATH}")
        return []

    df = pd.read_csv(DATA_PATH, encoding="utf-8-sig")
    df.columns = df.columns.str.strip().str.lower()

    if "quote" not in df.columns:
        print(f"❌ 'quote' column missing! Columns: {df.columns.tolist()}")
        return []

    documents = df["quote"].fillna("").tolist()
    authors = df["author"].fillna("").tolist()
    tags = df["tags"].fillna("").tolist()

    print(f"   ✓ Loaded {len(documents)} quotes")

    # Generate embeddings
    print("\n🧠 Generating embeddings...")
    try:
        embeddings = model.encode(documents)
        print(f"   ✓ Generated {len(embeddings)} embeddings")
    except Exception as e:
        print(f"   ❌ Error generating embeddings: {e}")
        return []

    print("🚀 Uploading to Endee...")

    try:
        index = client.get_index(name=INDEX_NAME)

        batch_size = 1000
        for i in range(0, len(documents), batch_size):
            batch = []

            for j in range(i, min(i + batch_size, len(documents))):
                batch.append({
                    "id": str(j),
                    "vector": embeddings[j].tolist(),
                    "meta": {
                        "quote": documents[j],
                        "author": authors[j],
                        "tags": tags[j]
                    }
                })

            index.upsert(batch)
            print(f"   ✓ Uploaded batch {i//batch_size + 1}")

        print(f"\n✅ Successfully uploaded {len(documents)} quotes")
        return documents

    except Exception as e:
        print(f"❌ Upload error: {e}")
        import traceback
        traceback.print_exc()
        return []


# -------------------------------
# Search Quotes
# -------------------------------
def search_quotes(query: str, top_k: int = 5):
    """Search for quotes similar to the query"""
    
    if not query.strip():
        return []

    # Load the model (lazy load)
    model = get_model()
    if model is None:
        return []

    try:
        print(f"\n🔍 Searching for: '{query}'")

        # Generate query embedding
        query_embedding = model.encode(query).tolist()

        # Get index
        index = client.get_index(name=INDEX_NAME)

        # Query - returns a list directly
        response = index.query(
            vector=query_embedding,
            top_k=top_k
        )

        # Debug logging (optional)
        # print(f"Response type: {type(response)}")
        # print(f"Response: {response}")

        # Response is already a list
        if not isinstance(response, list):
            print(f"⚠️  Unexpected response type: {type(response)}")
            return []

        quotes = []

        for result in response:
            # Extract metadata correctly
            meta = result.get("meta") or result.get("metadata") or {}
            
            score = result.get("score", 0)
            
            # Cosine similarity is between -1 and 1
            # Normalize to 0-1 range
            similarity = round((score + 1) / 2, 4)

            quotes.append({
                "quote": meta.get("quote", "") or "",
                "author": meta.get("author", "") or "",
                "tags": meta.get("tags", "") or "",
                "similarity": similarity
            })

        print(f"✅ Found {len(quotes)} results")
        return quotes

    except Exception as e:
        print(f"❌ Search error: {e}")
        import traceback
        traceback.print_exc()
        return []


# Test function for debugging
def debug_search():
    """Run a test search to verify everything works"""
    print("\n" + "="*60)
    print("DEBUG MODE - Testing QuoteSense")
    print("="*60)
    
    # First load data
    print("\n1️⃣  Loading data...")
    load_and_embed_quotes()
    
    # Then try searches
    test_queries = [
        "happiness",
        "success",
        "love",
    ]
    
    for query in test_queries:
        print(f"\n2️⃣  Testing query: '{query}'")
        results = search_quotes(query, top_k=3)
        
        if results:
            print(f"\n✅ Results for '{query}':")
            for i, quote in enumerate(results, 1):
                print(f"   {i}. {quote['quote'][:60]}...")
                print(f"      Author: {quote['author']}")
                print(f"      Similarity: {quote['similarity']}\n")
        else:
            print(f"   ⚠️  No results found")

    print("="*60)
    print("✅ Debug complete!")
    print("="*60)


if __name__ == "__main__":
    debug_search()