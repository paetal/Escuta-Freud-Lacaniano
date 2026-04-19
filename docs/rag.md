# Organização da base RAG

O `freud-lacan-local` pode (opcionalmente) consultar um corpus textual curado para oferecer explicações conceituais mais consistentes e rastreáveis. Este documento descreve como esse corpus é organizado.

A indexação e a recuperação são feitas **localmente**, com embeddings locais, sem chamadas a serviços externos.

---

## Três eixos

O corpus é dividido em três eixos distintos. Essa separação facilita a curadoria, a auditoria e a substituição de partes sem afetar as demais.

### Eixo freudiano

Textos de Freud, preferencialmente em **domínio público**. Ênfase em:

- *A interpretação dos sonhos* (1900)
- *Psicopatologia da vida cotidiana* (1901)
- *Três ensaios sobre a teoria da sexualidade* (1905)
- Ensaios sobre **sintoma**, **recalque**, **repetição** e **transferência**
- Ensaios sobre **elaboração** (*Durcharbeiten*) e **conflito psíquico**

Nota: o status de domínio público varia entre edições e traduções. Antes de incluir um texto na base distribuída publicamente, verifique a situação jurídica na jurisdição relevante. Quando em dúvida, mantenha o texto fora da distribuição pública e oriente o usuário a incluir localmente sua própria cópia.

### Eixo lacaniano

O eixo lacaniano é mais delicado por razões de direito autoral. A recomendação padrão é:

- **não distribuir** cópias dos Seminários ou dos *Écrits* no repositório;
- manter no repositório **notas conceituais, glossários e mapas** produzidos pelos mantenedores ou contribuidores, com atribuição clara;
- permitir que o usuário **ingesta localmente**, na sua própria instalação, material a que tenha acesso legítimo.

Temas de interesse:

- linguagem, significante e cadeia
- sujeito dividido e enunciação
- desejo, falta e fantasia
- gozo e repetição
- posição enunciativa
- o Outro, a demanda, o objeto *a*

### Eixo autoral

Material do próprio usuário: notas de leitura, mapas conceituais, glossários, textos pessoais sobre escuta e elaboração, metodologia própria de estudo.

Este eixo é estritamente local. Não é versionado no repositório. É carregado pelo usuário na sua própria instalação e permanece em sua máquina.

---

## Estrutura de diretórios

```
corpus/
├── freud/            — textos de Freud em domínio público
│   ├── pt-br/
│   └── de/
├── lacan/            — notas conceituais, glossários, mapas
│   └── notes/
└── autoral/          — ignorado pelo git; material do usuário
    └── .gitkeep
```

O diretório `corpus/autoral/` deve estar listado no `.gitignore`.

---

## Pipeline de ingestão

O script `scripts/ingest.py` (a ser implementado na Fase 2 do roadmap) faz:

1. leitura dos arquivos `.md`, `.txt` ou `.pdf` no diretório de corpus
2. extração e segmentação em trechos com metadados (autor, obra, ano, seção)
3. geração de embeddings locais
4. persistência em índice vetorial local (por exemplo, SQLite + FAISS ou equivalente)
5. relatório de ingestão com contagens por eixo

Nenhum dado sai da máquina durante esse processo.

---

## Citações

Respostas do sistema que utilizam o corpus devem **citar a fonte** com dados mínimos: autor, obra, seção ou página quando possível. O objetivo é permitir ao usuário ir ao texto original e conferir.

O sistema não deve inventar citações. Se não houver fonte no corpus, prefira formulação conceitual sem atribuição falsa.

---

## Revisão da curadoria

A curadoria do corpus é decisão editorial do projeto. Propostas de inclusão, exclusão ou reorganização devem ser abertas em issue com o rótulo `corpus`, descrevendo:

- o material proposto
- a relevância conceitual
- a situação de direito autoral
- uma amostra representativa

A decisão final fica com os mantenedores.
