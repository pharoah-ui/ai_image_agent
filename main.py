# main.py
from fastapi import FastAPI, Request
from pydantic import BaseModel
from content_analyzer import analyze_text
from image_generator import generate_images

app = FastAPI()

class BlogInput(BaseModel):
    text: str

@app.post("/generate-images")
async def generate_images_endpoint(blog: BlogInput):
    analysis = analyze_text(blog.text)
    images = generate_images(analysis['prompts'])
    
    result = []
    for i in range(len(images)):
        result.append({
            "prompt": analysis['prompts'][i],
            "image_url": images[i],
            "insert_after_paragraph": analysis['positions'][i]
        })
    
    return {"results": result}