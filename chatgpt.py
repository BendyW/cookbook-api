from openai import OpenAI
from dotenv import dotenv_values

config = dotenv_values()

client = OpenAI(
    # This is the default and can be omitted
    api_key=config["OPENAI_API_KEY"],
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)