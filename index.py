from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Post(BaseModel):
    id: int
    name: str
    description: str
    
posts = []
    
    
    

@app.post("/test")
async def create_post(post: Post):
  data = post.model_dump()
  posts.append(data)
  return data

