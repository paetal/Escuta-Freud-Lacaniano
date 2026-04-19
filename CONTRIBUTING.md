# Como contribuir

Obrigado pelo interesse em contribuir com o `freud-lacan-local`.

Antes de qualquer coisa, leia:

- [`README.md`](README.md)
- [`docs/manifesto.md`](docs/manifesto.md)
- [`docs/etica.md`](docs/etica.md)
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md)

Esses documentos definem o escopo e os limites do projeto. Contribuições que entrem em conflito com eles serão recusadas.

---

## Tipos de contribuição bem-vindos

- correções de bugs
- melhorias de documentação
- refatoração e melhorias de arquitetura
- casos de teste adversariais (tentativas de "quebrar" o prompt)
- curadoria do corpus (eixo freudiano em domínio público, notas conceituais)
- traduções
- relatos de uso, incluindo falhas e limitações observadas

## Tipos de contribuição que **não** serão aceitos

- integrações que enviem conversa do usuário para serviços externos por padrão
- funcionalidades que apresentem o sistema como terapia, tratamento, diagnóstico ou atendimento clínico
- mudanças no prompt-base que removam ou atenuem as instruções sobre limites e risco
- gamificação, notificações de retenção, métricas de engajamento que incentivem uso problemático
- inclusão de corpus sem atenção à situação de direito autoral

Em caso de dúvida, abra uma issue antes de gastar tempo em um PR.

---

## Fluxo de contribuição

1. Abra uma issue descrevendo o problema ou a proposta. Para alterações de escopo ético, conceitual ou no prompt-base, a discussão em issue é obrigatória antes do PR.
2. Faça um fork do repositório.
3. Crie uma branch com nome descritivo: `fix/historico-vazio`, `feat/export-markdown`, `docs/corpus-freud-pt`.
4. Faça commits pequenos e legíveis. Mensagens em português ou inglês.
5. Abra um pull request referenciando a issue.
6. Aguarde revisão. Mantenedores podem pedir ajustes.

---

## Alterações no prompt-base

O prompt em [`src/prompts/system.pt-BR.md`](src/prompts/system.pt-BR.md) é parte central do projeto. Alterações nele devem:

- vir acompanhadas de justificativa explícita na issue;
- preservar as instruções sobre limites, papéis clínicos recusados e redirecionamento em risco;
- ser testadas contra os casos adversariais em `examples/adversarial/`;
- quando aprovadas, ser registradas no changelog.

---

## Estilo de código

Serão adicionadas configurações de lint e format ao longo da Fase 1 do roadmap. Até lá, siga:

- Python: PEP 8, type hints, docstrings curtas;
- Markdown: uma frase por linha quando possível, para facilitar diff;
- commits: imperativo curto em português ou inglês (`corrige x`, `adiciona y`, `fix x`, `add y`).

---

## Revisão por pares

Revisões são feitas publicamente. Pull requests que afetem escopo ético, prompt-base ou curadoria de corpus podem exigir múltiplos revisores.

---

## Dúvidas

Abra uma issue com o rótulo `question`. Perguntas de primeira vez são bem-vindas.
