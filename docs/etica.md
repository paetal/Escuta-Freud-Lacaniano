# Ética e delimitação

Este documento descreve o que o `freud-lacan-local` **é**, o que **não é**, e quais as responsabilidades do projeto, dos mantenedores e dos usuários. Ele é parte constitutiva do projeto, não um aviso legal acessório.

---

## O que este projeto é

O `freud-lacan-local` é um **interlocutor textual** para:

- estudo conceitual da tradição freudiana e lacaniana;
- auto-reflexão e elaboração escrita;
- associação livre e experimentação com a própria fala;
- leitura mais fina das próprias formulações;
- exploração de noções teóricas e de material clínico em contexto de estudo.

---

## O que este projeto **não** é

O `freud-lacan-local` **não**:

- substitui análise pessoal ou psicoterapia;
- realiza diagnóstico psiquiátrico, psicológico ou médico;
- atua como profissional de saúde mental;
- oferece tratamento de qualquer natureza;
- promete cura, alívio de sintomas ou resolução de conflitos;
- é recurso apropriado em situações de crise, sofrimento grave ou risco;
- é canal de aconselhamento jurídico, financeiro, médico ou farmacológico.

---

## Situações que exigem ajuda humana

O sistema **não é adequado** e **não deve ser usado como único recurso** nestas situações:

- ideação suicida, planejamento ou atos autolesivos;
- ameaça ou risco a terceiros;
- violência doméstica, abuso, exploração;
- sintomas agudos de desorganização psíquica, surto, mania, psicose;
- episódios de dissociação significativa;
- uso problemático de substâncias em fase aguda;
- sofrimento que interfere de forma significativa no trabalho, nos vínculos, no sono, na alimentação ou na saúde física;
- qualquer situação em que a segurança física ou psíquica esteja em risco.

Nessas situações, procure **profissionais humanos de saúde mental** e **serviços de emergência locais**.

O prompt-base do sistema é instruído a **abandonar o estilo habitual** diante de sinais de risco agudo e orientar a busca por ajuda humana. Isso não torna o sistema um recurso de crise — apenas garante que ele não atrapalhe.

---

## Recursos de apoio (Brasil)

- **CVV — Centro de Valorização da Vida:** ligação gratuita **188**, disponível 24h. Chat e e-mail em [cvv.org.br](https://www.cvv.org.br).
- **CAPS — Centros de Atenção Psicossocial:** rede pública de saúde mental. Busque a unidade mais próxima pelo SUS.
- **SAMU:** **192** para emergências médicas.
- **Polícia Militar:** **190** em situações de risco imediato.

Fora do Brasil, busque os serviços de saúde mental e emergência do seu país.

---

## Privacidade

O projeto é desenhado para que toda a conversa, memória e corpus permaneçam na máquina do usuário. Em particular:

- **nenhuma** chamada a serviços externos de inferência é feita por padrão;
- o modelo de linguagem roda localmente via Ollama;
- as conversas são gravadas em SQLite local, em arquivo sob controle do usuário;
- não há telemetria embarcada;
- exportação e apagamento do histórico devem ser operações de primeira classe.

Qualquer integração futura que envolva envio de dados para fora da máquina precisa ser **opcional**, **explícita** e **documentada** — e jamais ativada por padrão. Integrações que violem esse princípio serão recusadas no projeto.

---

## Responsabilidade dos mantenedores

Os mantenedores se comprometem a:

- manter o código aberto e auditável;
- documentar o prompt-base, a curadoria do corpus e as dependências;
- recusar contribuições que transformem o sistema em ferramenta clínica, diagnóstica ou de aconselhamento profissional;
- revisar com atenção qualquer proposta que amplie a superfície de risco;
- manter este documento atualizado.

---

## Responsabilidade do usuário

Ao utilizar o `freud-lacan-local`, o usuário reconhece que:

- leu este documento e o [`manifesto.md`](manifesto.md);
- compreende que o sistema é ferramenta de estudo e auto-reflexão;
- entende que **não** se trata de tratamento, análise ou psicoterapia;
- se compromete a procurar ajuda humana em situações que a demandem;
- assume a responsabilidade pelo uso que faz da ferramenta e pelo manejo de seus próprios dados.

---

## Sobre o uso da psicanálise no projeto

O projeto se inspira em Freud e Lacan sem se apresentar como representante oficial de nenhuma escola, instituição ou associação psicanalítica. A orientação é **conceitual e textual**, com fins de estudo.

O projeto **não** concorre com a prática clínica, **não** se apresenta como alternativa à análise e **não** sugere que a experiência com o sistema equivalha, em qualquer grau, a um processo analítico.

---

## Alterações futuras

Qualquer alteração significativa neste documento ou no escopo ético do projeto será registrada no changelog, discutida em issue pública e comunicada de forma visível no README.
