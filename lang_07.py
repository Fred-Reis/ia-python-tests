import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.document_loaders import TextLoader, PyPDFLoader, CSVLoader

load_dotenv()

api_key = os.getenv("API_KEY")

os.environ["OPENAI_API_KEY"] = api_key

model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, max_tokens=256)

# loader = TextLoader("base_conhecimento.txt")
# document = loader.load()

# loader = PyPDFLoader("base_conhecimento.pdf")
# document = loader.load()

loader = CSVLoader("base_conhecimento.csv")
document = loader.load()

prompt_base_conhecimento = PromptTemplate(
    input_variables=["context", "question"],
    template="""
    Use o seguinte contexto para responder à pergunta.
    Responda apenas com base nasinformações fornecidas.
    Não utilize informações externas ao contexto:
    Contexto: {context}
    Pergunta: {question}
    """,
)

chain = prompt_base_conhecimento | model | StrOutputParser()

response = chain.invoke(
    {
        "context": "\n".join(doc.page_content for doc in document),
        "question": "Qual carro é mais caro?",
    }
)

print(response)
