from groq import Groq
from app.core.config import GROQ_API_KEY
from app.utils.text_utils import extract_sql

SYSTEM_PROMPT = """
You are an expert PostgreSQL query generator.

Rules:
- Output ONLY valid PostgreSQL SQL
- SELECT or WITH only
- No explanations, no comments
- PostgreSQL syntax only
- Use correct joins and aggregations
- Convert natural language questions into optimized SQL queries.
- Use ONLY SELECT statements.
- NEVER use INSERT, UPDATE, DELETE, DROP, ALTER, or TRUNCATE.
- Use correct JOINs based on foreign key relationships.
- Use aggregation functions when required.
- Use table and column names exactly as provided.
- Assume PostgreSQL syntax.
- Return ONLY the SQL query.
- Do not explain the query.
- Do not add comments or formatting.
- Use case-insensitive comparisons for string filters
- Prefer LOWER(column) = LOWER(value) or ILIKE
- Please give ONLY the SQL query as output, no explanation.
"""


client = Groq(api_key=GROQ_API_KEY)

def generate_sql(prompt: str) -> str:
    response = client.chat.completions.create(
        model="qwen/qwen3-32b",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.0
    )
    return extract_sql(response.choices[0].message.content)
