# image_generator.py
import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_images(prompts: list):
    urls = []
    for prompt in prompts:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512"
        )
        urls.append(response['data'][0]['url'])
    return urls