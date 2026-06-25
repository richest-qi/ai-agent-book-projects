#!/usr/bin/env python3
"""FastAPI entrypoint for the web search chat app."""

import logging
import uuid
from pathlib import Path

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from agent import WebSearchAgent
from config import Config

logging.basicConfig(
    level=getattr(logging, Config.LOG_LEVEL),
    format="%(asctime)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Web Search Chat", version="1.0.0")

STATIC_DIR = Path(__file__).resolve().parent / "static"
sessions: dict[str, WebSearchAgent] = {}


class ChatRequest(BaseModel):
    message: str = Field(..., min_length=1, max_length=4000)
    session_id: str | None = None


class ChatResponse(BaseModel):
    session_id: str
    answer: str


class ResetRequest(BaseModel):
    session_id: str


def _create_agent() -> WebSearchAgent:
    return WebSearchAgent(
        api_key=Config.MOONSHOT_API_KEY,
        base_url=Config.KIMI_BASE_URL,
    )


def _get_or_create_session(session_id: str | None) -> tuple[str, WebSearchAgent]:
    if session_id and session_id in sessions:
        return session_id, sessions[session_id]

    new_id = str(uuid.uuid4())
    agent = _create_agent()
    sessions[new_id] = agent
    return new_id, agent


@app.on_event("startup")
def on_startup() -> None:
    if not Config.validate():
        raise RuntimeError("Invalid configuration. Set MOONSHOT_API_KEY in .env")


@app.get("/")
async def index() -> FileResponse:
    return FileResponse(STATIC_DIR / "index.html")


@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    message = request.message.strip()
    if not message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    session_id, agent = _get_or_create_session(request.session_id)
    logger.info("Session %s: user message (%d chars)", session_id, len(message))

    answer = agent.chat(message)
    return ChatResponse(session_id=session_id, answer=answer)


@app.post("/api/reset")
async def reset_chat(request: ResetRequest) -> dict[str, bool]:
    sessions.pop(request.session_id, None)
    logger.info("Session %s cleared", request.session_id)
    return {"ok": True}


app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


if __name__ == "__main__":
    uvicorn.run("main:app", host=Config.HOST, port=Config.PORT, reload=True)
