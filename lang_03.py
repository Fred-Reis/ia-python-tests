import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

api_key = os.getenv("API_KEY")

model = ChatOpenAI(model="gpt-4o-mini")

TEMPLATE = """
Traduza o text do {idiom1} para o {idiom2}:
{text}
"""

prompt_template = PromptTemplate.from_template(template=TEMPLATE)

prompt = prompt_template.format(
    idiom1="português", idiom2="francês", text="Olá, como vai você?"
)

print(f"Prompt gerado:\n{prompt}\n")

response = model.invoke(prompt)

print(response.content)
