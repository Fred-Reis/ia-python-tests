import os
from dotenv import load_dotenv

from langchain_openai import OpenAI
from langchain_community.cache import InMemoryCache, SQLiteCache
from langchain_core.globals import set_llm_cache

load_dotenv()

api_key = os.getenv("API_KEY")

os.environ["OPENAI_API_KEY"] = api_key

model = OpenAI()
# set_llm_cache(InMemoryCache())
set_llm_cache(SQLiteCache(database_path="llm_cache.db"))

PROMPT = "quem foi alan turing?"

response1 = model.invoke(PROMPT)
print(f"First response: {response1}")

response2 = model.invoke(PROMPT)
print(f"Second response: {response2}")

# response = model.invoke(
#     input="quem foi albert einstein?",
#     temperature=0.7,
#     max_tokens=256,
# )

# print(response)
