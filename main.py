from fastapi import FastAPI
import requests
import json
import os


app = FastAPI()

@app.get("/CMSAI/IsImageGenKeyAvailable")
def isAPIKeyAvailable():
    if 'IMAGEGEN_API_KEY' in os.environ:
        return("API key is set in environment variable.")        
    else:
        print("API key is not set in environment variable.")   


@app.post("/CMSAI/GenerateImage")
def GenerateImage(input:str):
    api_key = os.getenv('IMAGEGEN_API_KEY')   

    # Define the API endpoint and request payload
    api_url = 'https://api.openai.com/v1/images/generations'
    headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}'
    }
    data = {
    "model": "dall-e-3",
    "prompt": input,
    "n": 1,
    "size": "1024x1024"
    }

    # Make the API request
    response = requests.post(api_url, headers=headers, data=json.dumps(data))

    # Check if the request was successful
    if response.status_code == 200:
        result = response.json()
        return result['data'][0]['url']
    else:
        return "Error:", response.status_code, response.text

