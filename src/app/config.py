"""Configuração do backend, carregada a partir de variáveis de ambiente."""
from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuração local. Não há envio de dados para serviços externos."""

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # Ollama
    ollama_host: str = "http://ollama:11434"
    ollama_model: str = "llama3.1:8b"
    ollama_embed_model: str = "nomic-embed-text"

    # Backend
    app_host: str = "0.0.0.0"
    app_port: int = 8000

    # Banco local
    db_path: str = "/data/freud-lacan-local.sqlite"

    # Idioma
    default_locale: str = "pt-BR"

    # Segurança / misc
    local_secret: str = "troque-isto"
    telemetry_enabled: bool = False

    # Caminho do prompt-base (relativo à raiz do container)
    system_prompt_path: Path = Path("/app/prompts/system.pt-BR.md")


@lru_cache
def get_settings() -> Settings:
    return Settings()
