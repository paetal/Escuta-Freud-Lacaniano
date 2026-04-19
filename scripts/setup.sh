#!/usr/bin/env bash
# setup.sh — primeiro boot do freud-lacan-local
#
# Baixa o modelo configurado em .env para o Ollama local.
# Use depois de `docker compose up -d`.

set -euo pipefail

if [ ! -f .env ]; then
  echo "arquivo .env não encontrado. copie .env.example para .env antes de continuar."
  exit 1
fi

# shellcheck disable=SC1091
source <(grep -E '^(OLLAMA_MODEL|OLLAMA_EMBED_MODEL)=' .env)

: "${OLLAMA_MODEL:=llama3.1:8b}"
: "${OLLAMA_EMBED_MODEL:=nomic-embed-text}"

echo "baixando modelo de conversa: ${OLLAMA_MODEL}"
docker exec flc-ollama ollama pull "${OLLAMA_MODEL}"

echo "baixando modelo de embeddings: ${OLLAMA_EMBED_MODEL}"
docker exec flc-ollama ollama pull "${OLLAMA_EMBED_MODEL}"

echo "pronto. api em http://localhost:8000/docs"
