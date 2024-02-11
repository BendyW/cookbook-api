import requests
from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from dotenv import dotenv_values
from bs4 import BeautifulSoup
from chatgptmax import send

app = FastAPI()
print("test")

config = dotenv_values()

client = OpenAI(
    api_key=config["OPENAI_API_KEY"],
)

modelTokenLimit = 4096
sendTokenLimit = 2000
testingURL = "https://joyfoodsunshine.com/the-most-amazing-chocolate-chip-cookies/"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

r = requests.get(testingURL, headers=headers)
soup = BeautifulSoup(r.content.decode(), 'html.parser')
soup = soup.get_text().strip()

responses = send(prompt="Return the recipe from this text:", text_data=soup, chat_model="gpt-3.5-turbo", model_token_limit=modelTokenLimit, max_tokens=sendTokenLimit)
allResponses = ""
for response in responses:
    allResponses = allResponses + response.content

print(allResponses)
print("--------------------")
print("Removing unnecessary text")
print("--------------------")
cleanResponses = send(prompt="Return most correct instructions:", text_data=allResponses, chat_model="gpt-3.5-turbo", model_token_limit=modelTokenLimit, max_tokens=sendTokenLimit)
for cleanResponses in cleanResponses:
    print(cleanResponses.content)
print("End of test")

# class Recipe(BaseModel):
#     recipe_url: str

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}

# @app.post("/find-recipe")
# async def find_recipe(recipe: Recipe):
#     headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
#     try:
#         r = requests.get(recipe.recipe_url, headers=headers)
#     except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError):
#         return {"error": "Error"}
#     soup = BeautifulSoup(r.content.decode(), 'html.parser')
#     soup = soup.get_text().strip()
#     print(len(soup))
#     try:
#         completion = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content": f"Return the recipe from this text: {soup}."}
#             ]
#         )
#     except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError):
#         return {"error": "Error"}
#     print(completion)
#     return completion
