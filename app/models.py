# Pydantic models for requests/responses
from pydantic import BaseModel

class SearchQuery(BaseModel):
    query: str

class SearchResult(BaseModel):
    title: str
    abstract: str
    score: float