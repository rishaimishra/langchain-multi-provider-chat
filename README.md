# LangChain Multi-Provider Chat

Part of my **Founder's AI Learning Path** — learning AI engineering in public while running [SRV Technology](https://srvtechnology.com).

A few weeks into learning LangChain, the thing that actually clicked wasn't any single API call — it was realizing the chat-model interface is the same shape across providers. Swap the class, keep everything else (`invoke`, `stream`, prompt templates, chains) identical.

This repo is a minimal, side-by-side demo of calling **OpenAI, Mistral AI, Groq, and Google Gemini** through LangChain's unified `BaseChatModel` interface — same prompt, four models, no per-provider branching logic.

## What's here

- `openai_chat.py` — `ChatOpenAI`
- `mistral_chat.py` — `ChatMistralAI`
- `groq_chat.py` — `ChatGroq`
- `gemini_chat.py` — `ChatGoogleGenerativeAI`
- `compare_providers.py` — runs the same prompt through all four and prints each response side by side

## Why this matters

Once you're on LangChain's interface, switching providers (cost, latency, rate limits, or just "this model is better at this task") is a one-line change, not a rewrite. That's the actual lesson — not "here's how to call an API."

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env   # fill in whichever provider keys you want to test
python compare_providers.py
```

You don't need all four keys — each script only needs its own provider's key, and `compare_providers.py` will skip any provider whose key is missing.

## Learning path

This is one entry in an ongoing series — see the write-ups on [LinkedIn](https://www.linkedin.com/in/rishav-kumar-4441b3112/) where I break down what I'm learning as I build each piece.
