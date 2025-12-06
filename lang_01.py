import os
from dotenv import load_dotenv

from langchain_openai import OpenAI, ChatOpenAI

load_dotenv()

api_key = os.getenv("API_KEY")

os.environ["OPENAI_API_KEY"] = api_key
# model = OpenAI()

# response = model.invoke(
#     input="quem foi albert einstein?",
#     temperature=0.7,
#     max_tokens=256,
# )

# print(response)

model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, max_tokens=256)

messages = [
    {
        "role": "system",
        "content": "Você é um assitente de mecânica automotiva experiente e dá respostas técnicas, objetivas e concisas.",
    },
    {"role": "user", "content": "Me fale sobre o fiat Uno 2009."},
]

response = model.invoke(messages)

print(response.content)
