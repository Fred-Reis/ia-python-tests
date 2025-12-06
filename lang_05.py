import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

api_key = os.getenv("API_KEY")

os.environ["OPENAI_API_KEY"] = api_key

model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, max_tokens=256)

prompt_template = PromptTemplate.from_template("Me fale sobre p carro: {car_model}")

runable_sequence = prompt_template | model | StrOutputParser()

response = runable_sequence.invoke({"car_model": "Chevrolet Tracker 2022"})

print(response)
