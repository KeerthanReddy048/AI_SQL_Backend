AI-Powered Natural Language to SQL Query System

Overview

This project is a web-based AI system that allows users to connect their own cloud or on-prem PostgreSQL databases and query them using natural language.
The system automatically understands the database schema, generates safe SQL queries, executes them, and returns results — while enforcing strict safety, observability, and error-handling mechanisms.

Key Features

🔌 Dynamic Database Connection

Connect to cloud (Supabase / remote PostgreSQL) or on-prem PostgreSQL

Credentials stored only in memory (never persisted)

🧠 Schema-Aware AI SQL Generation

Automatic schema introspection using information_schema

LLM generates SQL strictly based on available tables and columns

🔒 SQL Safety Guardrails

-> SELECT-only enforcement

-> Blocks destructive queries (DROP, DELETE, UPDATE, etc.)

-> Prevents multi-statement execution

-> Automatic row limiting

🛠 Robust Error Handling with AI Regeneration

-> Gracefully handles SQL errors (invalid columns, tables, syntax)

-> Automatically regenerates SQL using error feedback (single retry)

-> Prevents infinite retries or unsafe execution

📊 Query Observability & Logging

-> Logs user question, generated SQL, execution time, row count, and status

-> Enables auditing and performance analysis

🌐 Web Interface

-> Database connect / disconnect UI

-> Natural language query input

-> Displays generated SQL and query results

-> Prevents querying when DB is not connected

System Architecture

  User (Web UI)
      ↓
  FastAPI Backend
      ↓
  Intent Validation
      ↓
  Schema Introspection
      ↓
  LLM → SQL Generation
      ↓
  SQL Safety Validation
      ↓
  PostgreSQL Execution
      ↓
  Results + Logs

Tech Stack

-> Backend: FastAPI, Python

-> Database: PostgreSQL (Supabase / On-Prem)

AI: Large Language Model (LLM) for SQL generation

Frontend: Web UI (React / HTML + JS)

DB Driver: psycopg2

API Endpoints

-> POST /connect-db – Test and establish database connection

-> POST /ask – Natural language query → SQL → result

-> GET /schema – Fetch database schema

-> POST /disconnect-db – Disconnect active database

Security Considerations

-> Database credentials are never stored

-> Queries are restricted to read-only

-> Unsafe SQL is blocked before execution

-> All queries are logged for auditability

Example Use Cases

-> Business users querying databases without SQL knowledge

-> Analytics teams exploring data quickly
