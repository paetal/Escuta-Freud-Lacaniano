"""
freud-lacan-local — API local.

Interlocutor textual de escuta para estudo e auto-reflexão, com orientação
freudiana e lacaniana, rodando 100% local. NÃO substitui análise,
psicoterapia, diagnóstico ou atendimento em saúde mental.

Este arquivo contém o scaffold inicial do backend. Endpoints funcionais
serão entregues ao longo da Fase 1 do roadmap.
"""
from __future__ import annotations

from pathlib import Path

import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from .config import get_settings

app = FastAPI(
    title="freud-lacan-local",
    description=(
        "Interlocutor textual de escuta para estudo e auto-reflexão. "
        "Não substitui análise, psicoterapia ou atendimento em saúde mental."
    ),
    version="0.1.0",
)


# ------------------------------------------------------------------
# modelos de request / response
# ------------------------------------------------------------------


class ChatMessage(BaseModel):
    role: str  # "user" | "assistant" | "system"
    content: str


class ChatRequest(BaseModel):
    messages: list[ChatMessage]


class ChatResponse(BaseModel):
    reply: str


# ------------------------------------------------------------------
# utilidades
# ------------------------------------------------------------------


def _load_system_prompt() -> str:
    settings = get_settings()
    path = Path(settings.system_prompt_path)
    if not path.exists():
        # fallback local para desenvolvimento fora do container
        fallback = Path(__file__).parent.parent / "prompts" / "system.pt-BR.md"
        path = fallback
    return path.read_text(encoding="utf-8")


# ------------------------------------------------------------------
# endpoints
# ------------------------------------------------------------------


@app.get("/healthz")
def healthz() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/")
def root() -> dict[str, str]:
    return {
        "name": "freud-lacan-local",
        "tagline": (
            "Interlocutor de escuta para estudo e auto-reflexão, "
            "com orientação freudiana e lacaniana, rodando 100% local e offline."
        ),
        "disclaimer": (
            "Este projeto NÃO substitui análise, psicoterapia, diagnóstico "
            "ou atendimento em saúde mental. Em situações de sofrimento grave, "
            "ideação suicida ou risco, procure ajuda humana profissional."
        ),
    }


@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    """
    Endpoint de conversa. Envia mensagens ao modelo local via Ollama,
    com o prompt-base injetado como mensagem de sistema.
    """
    settings = get_settings()
    system_prompt = _load_system_prompt()

    payload = {
        "model": settings.ollama_model,
        "stream": False,
        "messages": [
            {"role": "system", "content": system_prompt},
            *[m.model_dump() for m in request.messages],
        ],
    }

    async with httpx.AsyncClient(timeout=120.0) as client:
        try:
            r = await client.post(
                f"{settings.ollama_host}/api/chat",
                json=payload,
            )
            r.raise_for_status()
        except httpx.HTTPError as exc:
            raise HTTPException(
                status_code=502,
                detail=f"Falha ao conversar com o modelo local: {exc}",
            ) from exc

    data = r.json()
    reply = data.get("message", {}).get("content", "")
    return ChatResponse(reply=reply)
