from fastapi import FastAPI
from app.cards.presentation.router import router as cards_router

app = FastAPI(
    title="Word Hunt API",
    version="0.1.0"
)


app.include_router(cards_router)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}