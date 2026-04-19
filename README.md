# freud-lacan-local

> Interlocutor de escuta para estudo e auto-reflexão, com orientação freudiana e lacaniana, rodando 100% local e offline.

> *English:* Local-first conversational tool for self-reflection and study, inspired by Freudian and Lacanian psychoanalysis. Private, offline, and ethically delimited.

---

## Aviso importante

O **freud-lacan-local** é uma ferramenta de **interlocução textual** para **estudo** e **auto-reflexão**.

Ele **não** substitui análise, psicoterapia, diagnóstico ou atendimento em saúde mental. Ele **não** atua como terapeuta, psicanalista, médico ou recurso de crise. Em situações de sofrimento grave, ideação suicida, risco a si ou a terceiros, procure ajuda humana profissional e serviços de emergência locais. Veja [`docs/etica.md`](docs/etica.md).

---

## O que é

O `freud-lacan-local` é um projeto open source que oferece um espaço textual privado para **elaboração**, **associação livre**, **leitura mais fina da própria fala** e **estudo conceitual** orientado pela tradição freudiana e lacaniana.

Ele roda inteiramente na máquina do usuário, com modelos de peso aberto servidos localmente via [Ollama](https://ollama.com), sem envio de dados a serviços externos. Conversas, notas e memória ficam em SQLite local, em arquivos que o usuário pode auditar, apagar ou migrar livremente.

A proposta não é simular um analista nem automatizar uma clínica. É oferecer um **dispositivo de linguagem** que sustente uma experiência de fala menos banal do que a dos assistentes conversacionais genéricos.

Leia o [`docs/manifesto.md`](docs/manifesto.md) para o fundamento teórico e o posicionamento conceitual completo.

---

## Princípios

- execução 100% local — nenhum dado sai da máquina
- privacidade radical — o usuário controla armazenamento, exportação e apagamento
- arquitetura auditável — código aberto, dependências rastreáveis, sem telemetria
- orientação freudiana e lacaniana explícita — documentada no prompt e no corpus
- delimitação ética clara — o projeto declara o que é e o que não é

---

## Stack

- [Ollama](https://ollama.com) — runtime local para modelos de peso aberto
- Modelo local recomendado: Llama 3.1 8B, Mistral 7B, Qwen 2.5 ou equivalente
- [FastAPI](https://fastapi.tiangolo.com) — backend HTTP
- SQLite — persistência local das conversas
- RAG local sobre corpus freudiano e lacaniano (ver [`docs/rag.md`](docs/rag.md))
- Docker Compose para subir tudo em um único comando

---

## Rodando localmente

Pré-requisitos: [Docker](https://docs.docker.com/get-docker/) e [Docker Compose](https://docs.docker.com/compose/install/).

```bash
git clone https://github.com/SEU-USUARIO/freud-lacan-local.git
cd freud-lacan-local
cp .env.example .env
docker compose up --build
```

Acesse a interface em:

```
http://localhost:3000
```

A API sobe em `http://localhost:8000`. A documentação interativa do FastAPI fica em `http://localhost:8000/docs`.

Na primeira execução, o Ollama faz o download do modelo configurado em `.env` (`OLLAMA_MODEL`). Isso pode levar alguns minutos e consumir alguns GB de disco.

---

## Estrutura do repositório

```
freud-lacan-local/
├── README.md                 — este arquivo
├── LICENSE                   — AGPL-3.0
├── CONTRIBUTING.md           — como contribuir
├── CODE_OF_CONDUCT.md        — código de conduta
├── .env.example              — variáveis de ambiente exemplares
├── .gitignore
├── docker-compose.yml        — orquestração local
├── docs/
│   ├── manifesto.md          — fundamento teórico e posicionamento
│   ├── etica.md              — delimitação ética do projeto
│   ├── roadmap.md            — plano de desenvolvimento
│   ├── prompt.md             — o prompt-base comentado
│   └── rag.md                — organização da base de conhecimento
├── src/
│   ├── app/                  — backend FastAPI
│   ├── rag/                  — indexação e recuperação do corpus
│   └── prompts/              — prompts versionados
├── scripts/                  — utilitários de setup, ingestão, export
└── examples/                 — exemplos de uso e de corpus autoral
```

---

## Documentação

- [Manifesto e fundamento teórico](docs/manifesto.md)
- [Ética e delimitação](docs/etica.md)
- [Roadmap](docs/roadmap.md)
- [Prompt-base](docs/prompt.md)
- [Organização da base RAG](docs/rag.md)

---

## Como contribuir

Contribuições são bem-vindas. Antes de abrir uma issue ou pull request, leia [`CONTRIBUTING.md`](CONTRIBUTING.md) e [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

O projeto tem um compromisso explícito com a sua delimitação ética (ver [`docs/etica.md`](docs/etica.md)). Contribuições que tentem transformar o sistema em produto de aconselhamento clínico, diagnóstico automatizado ou substituição de atendimento profissional serão recusadas.

---

## Licença

Distribuído sob a licença **GNU AGPL-3.0**. Veja [`LICENSE`](LICENSE).

A escolha da AGPL é deliberada. Ela garante que qualquer derivado — inclusive versões servidas pela rede — permaneça aberto e auditável, em coerência com os princípios do projeto.

---

## Repetindo o aviso, porque importa

Este projeto **não** substitui análise, psicoterapia, diagnóstico ou atendimento em saúde mental. É uma ferramenta de estudo e auto-reflexão.
