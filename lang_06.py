import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

api_key = os.getenv("API_KEY")

os.environ["OPENAI_API_KEY"] = api_key

model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, max_tokens=256)

classification_chain = (
    PromptTemplate.from_template(
        """
		Classifique a pegunta do usuário em um dos seguintes setores:
		- Financeiro
		- Suporte Técnico
		- Outras Informações

		Pergunta: {question}
		"""
    )
    | model
    | StrOutputParser()
)

financial_chain = (
    PromptTemplate.from_template(
        """
		Você é um especialista financeiro.
		Sempre responda as perguntas começando com "Bem-vindo ao Setor Financeiro".
		Responda a pergunta do usuário:
		Pergunta: {question}
		"""
    )
    | model
    | StrOutputParser()
)

support_chain = (
    PromptTemplate.from_template(
        """
		Você é um especialista em suporte técnico.
		Sempre responda as perguntas começando com "Bem-vindo ao Suporte Técnico".
		Responda a pergunta do usuário:
		Pergunta: {question}
		"""
    )
    | model
    | StrOutputParser()
)

other_chain = (
    PromptTemplate.from_template(
        """
		Você é um assistente de informações gerais.
		Sempre responda as perguntas começando com "Bem-vindo ao Setor de Central de Informações".
		Responda a pergunta do usuário:
		Pergunta: {question}
		"""
    )
    | model
    | StrOutputParser()
)


def route(topic):
    """function to route to the correct chain based on classification"""
    topic = topic.lower()
    if "financeiro" in topic:
        return financial_chain
    if "técnico" in topic:
        return support_chain
    else:
        return other_chain


QUESTION = input("Digite sua pergunta: ")

classification = classification_chain.invoke({"question": QUESTION})

response_chain = route(topic=classification)

response = response_chain.invoke({"question": QUESTION})

print(response)
