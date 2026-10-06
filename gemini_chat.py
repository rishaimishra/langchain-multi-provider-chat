from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template("Explain {topic} in simple words")
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")
parser = StrOutputParser()

chain = prompt | model | parser

if __name__ == "__main__":
    result = chain.invoke({"topic": "machine learning"})
    print(result)
