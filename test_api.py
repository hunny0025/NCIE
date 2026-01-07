import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if api_key and api_key.startswith("sk-proj-"):
    print("✅ API Key loaded successfully!")
    print(f"First 10 chars: {api_key[:10]}...")
else:
    print("❌ API Key not found or invalid")
    print("Make sure .env file exists with OPENAI_API_KEY=your_key")