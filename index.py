from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Post(BaseModel):
    id: int
    name: str
    description: str
    
posts = []
    
@app.get("/test")
async def test_Db():
  return {"message":"All ser go ahead"}
    

@app.post("/post")
async def create_post(post: Post):
  data = post.model_dump()
  posts.append(data)
  return data

