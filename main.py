from fastapi import FastAPI
from app.api.routes import router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(title="AI SQL Backend")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",   # Vite / React
        "http://127.0.0.1:5173",
        "https://aiforsql.netlify.app"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(router)

