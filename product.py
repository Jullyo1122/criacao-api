from pydantic import BaseModel

class Movies(BaseModel):
    title: str
    year: int