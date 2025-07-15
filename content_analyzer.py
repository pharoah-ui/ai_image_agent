# content_analyzer.py
import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_text(text: str):
    prompt = f"""
You are an assistant helping bloggers automate image generation. Read the blog post below. 

Your task:
1. Extract 4 visual scenes that could be turned into images.
2. Suggest after which paragraph each image should be inserted.

Return output as JSON like:
{{
  "prompts": ["image prompt 1", ..., "image prompt 4"],
  "positions": [1, 3, 5, 7]  # paragraph numbers
}}

BLOG POST:
{text}
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    
    import json
    output = response.choices[0].message['content']
    return json.loads(output)