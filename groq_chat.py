from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template("Explain {topic} in simple words")
model = ChatGroq(model="llama-3.3-70b-versatile")
parser = StrOutputParser()

chain = prompt | model | parser

if __name__ == "__main__":
    result = chain.invoke({"topic": "machine learning"})
    print(result)
