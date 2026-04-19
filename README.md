# freud-lacan-local

Interlocutor de escuta para estudo e auto-reflexão, com orientação freudiana e lacaniana, rodando 100% local e offline.

## O que é

O freud-lacan-local é uma ferramenta open source de interlocução textual inspirada pela tradição freudiana e lacaniana da psicanálise. Ele foi desenhado para rodar offline, em máquina local, sem enviar dados íntimos para serviços externos.

Seu objetivo é oferecer um espaço de escuta, elaboração textual e estudo.

## O que ele não é

Este projeto não substitui análise, psicoterapia, diagnóstico ou atendimento em saúde mental.  
Não atua como terapeuta, psicanalista, médico ou recurso de crise.

## Princípios

- execução 100% local
- privacidade radical
- arquitetura auditável
- orientação freudiana e lacaniana explícita
- delimitação ética clara

## Stack

- Ollama
- modelo local open weights
- FastAPI
- SQLite
- RAG local
- Docker Compose

## Rodando localmente

```bash
git clone https://github.com/seuusuario/freud-lacan-local.git
cd freud-lacan-local
cp .env.example .env
docker compose up --build
