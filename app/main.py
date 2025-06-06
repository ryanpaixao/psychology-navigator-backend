# FastAPI entrypoint
from fastapi import FastAPI, Query
from app.models import SearchQuery, SearchResult
from app.search import search_similar

app = FastAPI()

@app.get("/search", response_model=list[SearchResult])
def search_route(q: str = Query(..., description="Your semantic search query")):
    return search_similar(q)