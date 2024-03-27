import requests
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import dotenv_values
from bs4 import BeautifulSoup
from chatgptmax import send
# from psql_app.connect import connect


app = FastAPI()

config = dotenv_values()

client = OpenAI(
    api_key=config["OPENAI_API_KEY"],
)

modelTokenLimit = 4096
sendTokenLimit = 2000
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}



class Recipe(BaseModel):
    url: str

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@app.post("/find-recipe")
def find_recipe(recipe: Recipe):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    r = requests.get(recipe.url, headers=headers)
    soup = BeautifulSoup(r.content.decode(), 'html.parser')
    soup = soup.get_text().strip()
    print(soup)
    findIngredientsAndInstructionsResponses = send(prompt="Check if this text contains an exact list of ingredients with measurements. Return ingredients if it is a match. Check if this text contains exact instructions to a recipe. Return instructions if so. Do not return text if no matches", text_data=soup, chat_model="gpt-3.5-turbo", model_token_limit=modelTokenLimit, max_tokens=sendTokenLimit)
    allResponses = ""
    for response in findIngredientsAndInstructionsResponses:
        allResponses = allResponses + response.content
    print(allResponses)
    return {"recipe": allResponses}
