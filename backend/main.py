from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os
import sys

# Add current directory to path so utils can be imported
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import utils (direct import)
from utils import load_and_embed_quotes, search_quotes

app = FastAPI(title="Quote Recommender")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get absolute path to current directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Mount static files
app.mount("/static", StaticFiles(directory=BASE_DIR), name="static")

class QueryRequest(BaseModel):
    query: str
    top_k: int = 5

@app.on_event("startup")
async def startup_event():
    load_and_embed_quotes()

# Serve index.html at root URL
@app.get("/")
async def serve_frontend():
    index_path = os.path.join(BASE_DIR, "index.html")
    return FileResponse(index_path)

@app.get("/recommend")
async def recommend_get(query: str = Query(..., min_length=1), top_k: int = 5):
    results = search_quotes(query, top_k)
    return {"query": query, "results": results}

@app.post("/recommend")
async def recommend_post(request: QueryRequest):
    results = search_quotes(request.query, request.top_k)
    return {"query": request.query, "results": results}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)