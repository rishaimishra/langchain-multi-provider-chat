"""
Runs the same prompt through OpenAI, Mistral, Groq, and Gemini — all via
LangChain's shared chat-model interface. Any provider whose API key is
missing from .env is skipped rather than failing the whole run.
"""
import os
from dotenv import load_dotenv

load_dotenv()

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

PROMPT = ChatPromptTemplate.from_template("Explain {topic} in one sentence")
PARSER = StrOutputParser()
TOPIC = "machine learning"


def build_providers():
    providers = []

    if os.getenv("OPENAI_API_KEY"):
        from langchain_openai import ChatOpenAI
        providers.append(("OpenAI", ChatOpenAI(model="gpt-4o-mini")))

    if os.getenv("MISTRAL_API_KEY"):
        from langchain_mistralai import ChatMistralAI
        providers.append(("Mistral", ChatMistralAI(model="mistral-small-2506")))

    if os.getenv("GROQ_API_KEY"):
        from langchain_groq import ChatGroq
        providers.append(("Groq", ChatGroq(model="llama-3.3-70b-versatile")))

    if os.getenv("GOOGLE_API_KEY"):
        from langchain_google_genai import ChatGoogleGenerativeAI
        providers.append(("Gemini", ChatGoogleGenerativeAI(model="gemini-1.5-flash")))

    return providers


def main():
    providers = build_providers()
    if not providers:
        print("No provider API keys found in .env — add at least one to run this.")
        return

    for name, model in providers:
        chain = PROMPT | model | PARSER
        result = chain.invoke({"topic": TOPIC})
        print(f"\n[{name}]\n{result}")


if __name__ == "__main__":
    main()
