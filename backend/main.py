from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os
import sys

# Fix import path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

from utils import load_and_embed_quotes, search_quotes

app = FastAPI(title="QuoteSense AI Recommender")

# -------------------------------
# CORS (for frontend)
# -------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------
# Static Files (CSS + JS)
# -------------------------------
app.mount("/static", StaticFiles(directory=BASE_DIR), name="static")


# -------------------------------
# Request Model
# -------------------------------
class QueryRequest(BaseModel):
    query: str
    top_k: int = 5


# -------------------------------
# Startup (Load data)
# -------------------------------
@app.on_event("startup")
async def startup_event():
    print("🚀 Starting QuoteSense...")
    load_and_embed_quotes()
    print("✅ System ready")


# -------------------------------
# Frontend Route
# -------------------------------
@app.get("/")
async def serve_frontend():
    return FileResponse(os.path.join(BASE_DIR, "index.html"))


# -------------------------------
# GET API
# -------------------------------
@app.get("/recommend")
async def recommend_get(query: str = Query(..., min_length=1), top_k: int = 5):
    try:
        results = search_quotes(query, top_k)
        return {
            "status": "success",
            "query": query,
            "count": len(results),
            "results": results
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
            "results": []
        }


# -------------------------------
# POST API
# -------------------------------
@app.post("/recommend")
async def recommend_post(request: QueryRequest):
    try:
        results = search_quotes(request.query, request.top_k)
        return {
            "status": "success",
            "query": request.query,
            "count": len(results),
            "results": results
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
            "results": []
        }


# -------------------------------
# Run Server
# -------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)