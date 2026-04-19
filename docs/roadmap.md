# Roadmap

Este documento descreve as fases de desenvolvimento previstas. Ele é indicativo e será atualizado conforme o projeto evolui. Cada fase prioriza **funcionalidade mínima viável**, **qualidade de escuta** e **privacidade**, nessa ordem.

---

## Fase 0 — Fundações (em curso)

Objetivo: tornar o projeto publicável e legível para contribuidores.

- [x] Nomeação do projeto: `freud-lacan-local`
- [x] Manifesto, ética e licença AGPL-3.0
- [x] Prompt-base inicial documentado
- [x] Estrutura de repositório e scaffolding inicial
- [ ] CI básico (lint, testes)
- [ ] Template de issue e pull request

---

## Fase 1 — MVP local funcional

Objetivo: o usuário consegue clonar o repositório, rodar um `docker compose up` e conversar com o sistema em uma interface web simples.

- [ ] Backend FastAPI com endpoints `/chat`, `/history`, `/export`, `/delete`
- [ ] Integração com Ollama local
- [ ] Persistência em SQLite com esquema versionado
- [ ] Frontend web mínimo (SSR ou SPA simples) em `localhost:3000`
- [ ] Configuração por `.env` com valores sensatos por padrão
- [ ] Script de ingestão para o prompt-base
- [ ] Script de export e apagamento do histórico
- [ ] Testes de fumaça do pipeline ponta a ponta

Critério de saída da Fase 1: um novo usuário, seguindo o README, consegue instalar e conversar em menos de 15 minutos, sem qualquer tráfego de rede fora de downloads de modelo e imagens Docker.

---

## Fase 2 — RAG sobre corpus freudiano e lacaniano

Objetivo: o sistema consegue consultar e citar textos curados das tradições freudiana e lacaniana, respeitando domínio público e permissões de uso.

- [ ] Estrutura `src/rag/` com indexador e recuperador
- [ ] Embeddings locais (sem API externa)
- [ ] Pipeline de ingestão a partir de `docs/corpus/` e `examples/corpus/`
- [ ] Curadoria inicial do **eixo freudiano** em domínio público (ver [`rag.md`](rag.md))
- [ ] Curadoria inicial do **eixo lacaniano** a partir de material autoral ou autorizado
- [ ] Possibilidade de eixo **autoral** do usuário (notas, mapas conceituais)
- [ ] Citações rastreáveis no output

Critério de saída da Fase 2: usuário consegue pedir uma explicação conceitual e receber resposta ancorada em fontes curadas, com referências verificáveis.

---

## Fase 3 — Refinamento da escuta

Objetivo: o sistema responde de forma menos genérica, mais atenta à singularidade da fala.

- [ ] Memória de conversa com resumo periódico
- [ ] Detecção simples de repetições, deslocamentos e temas recorrentes na própria fala do usuário ao longo de múltiplas sessões
- [ ] Configurações de estilo de escuta (mais discreto, mais interrogativo, mais conceitual)
- [ ] Avaliação qualitativa com diário de uso
- [ ] Ajustes no prompt-base com base em uso real
- [ ] Biblioteca de "movimentos" de resposta (pontuação, corte, devolução, escansão)

Critério de saída da Fase 3: diminuição perceptível de respostas genéricas de autoajuda em um conjunto de casos de teste qualitativos.

---

## Fase 4 — Segurança e proteção

Objetivo: reduzir ao mínimo o risco de uso inadequado.

- [ ] Classificador local de sinais de risco agudo com resposta segura
- [ ] Mensagem de redirecionamento para recursos humanos e de emergência
- [ ] Rate limiting local e proteção contra loops
- [ ] Auditoria do prompt com testes adversariais documentados
- [ ] Revisão externa do escopo ético por pessoa com formação em saúde mental
- [ ] Relato público dos limites conhecidos do sistema

Critério de saída da Fase 4: relatório público com o que o sistema faz e o que ele reconhecidamente **não** faz, incluindo falhas conhecidas.

---

## Fase 5 — Experiência e distribuição

Objetivo: tornar o projeto utilizável por pessoas que não são desenvolvedoras.

- [ ] Instalador para macOS, Windows e Linux
- [ ] Interface com modo noturno, ajuste de fonte, acessibilidade básica
- [ ] Export para Markdown, PDF e arquivo de texto simples
- [ ] Tradução da interface e da documentação para inglês
- [ ] Tutoriais de uso para estudo e auto-reflexão

Critério de saída da Fase 5: uma pessoa sem formação técnica consegue instalar, usar e exportar seu histórico sem precisar de linha de comando.

---

## Fora do escopo — decisões explícitas

Estas direções **não** serão perseguidas:

- versão hospedada na nuvem como serviço comercial;
- integração com plataformas que envolvam envio de fala para serviços externos sem consentimento explícito, opt-in e documentação;
- qualquer apresentação do sistema como terapia, tratamento ou atendimento clínico;
- funcionalidades de "diagnóstico automático", triagem clínica ou protocolos terapêuticos;
- gamificação, engajamento por métricas de uso, notificações de retenção.

---

## Como propor alterações ao roadmap

Abra uma issue com o rótulo `roadmap`. Descreva o problema, a proposta, alternativas consideradas e as implicações éticas. Discussões sobre o escopo do projeto acontecem no repositório, publicamente.
