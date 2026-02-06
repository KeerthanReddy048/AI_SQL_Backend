import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY missing")

LOG_FILE = "query_logs.jsonl"
MAX_RETRIES = 2

BLOCKED_KEYWORDS = [
    "DROP", "DELETE", "UPDATE", "INSERT",
    "ALTER", "TRUNCATE", "CREATE", "REPLACE"
]

EXPLANATION_KEYWORDS = [
    "explain", "why", "how", "which join",
    "describe", "what does"
]
