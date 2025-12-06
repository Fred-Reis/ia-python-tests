import os
from dotenv import load_dotenv

from openai import OpenAI

load_dotenv()  # This loads variables from .env into os.environ

api_key = os.getenv("API_KEY")

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "system",
            "content": "Você é um assitente de mecânica automotiva experiente e dá respostas técnicas, objetivas e concisas.",
        },
        {"role": "user", "content": "Me fale sobre o fiat Uno 2009."},
    ],
)

print(response.choices[0].message.content)
