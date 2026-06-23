# AGENTS.md — Respira / Ventila

Este arquivo orienta agentes, assistentes, Codex e colaboradores automatizados que venham a trabalhar neste repositório.

O projeto tem tese pedagógica, identidade visual, arquitetura didática e critérios de qualidade próprios. Não trate os arquivos como HTML solto e não aplique reflexos genéricos de engenharia quando eles contradisserem a finalidade do material.

## 1. Missão do projeto

O repositório hospeda duas séries integradas:

- **Respira** — Parte A: fisiologia respiratória, oxigenação, relação V/Q, gasometria, síndromes, terapêutica, suporte não invasivo e fundamentos de ventilação mecânica.
- **Ventila** — Parte B: ventilação mecânica aprofundada, visual, interativa, socrática e clinicamente aplicada.

Tese editorial do Ventila:

> O ventilador não é tratamento em si. É uma intervenção mecânica que compra tempo, transfere trabalho, impõe energia e cria riscos.

Essa tese deve orientar perguntas, casos, pegadinhas, laboratórios, animações e feedbacks.

## 2. Decisão arquitetural atual — single-file como fonte canônica

A decisão atual do projeto é explícita:

> **Cada módulo publicado deve ser um HTML autocontido, capaz de abrir diretamente no navegador e funcionar sem build, sem servidor, sem fetch, sem backend e sem toolchain.**

Isso não é improviso. É uma escolha de robustez.

O projeto é um conjunto de instrumentos didáticos portáteis, não um SaaS. A propriedade central é:

```txt
abrir o .html → funcionar
```

Portanto:

- não introduza build obrigatório;
- não exija bundler;
- não transforme o deploy em pipeline;
- não separe CSS/JS se isso fizer o módulo publicado depender de etapa externa;
- não substitua HTML autocontido por arquitetura “limpa” que quebre autonomia;
- não faça DRY prematuro se a duplicação ainda não é dor real;
- aceite duplicação quando ela compra antifragilidade;
- mantenha navegação relativa e compatibilidade offline.

A regra de decisão é:

```txt
runtime robusto + módulo fechado + baixa frequência de edição compartilhada → não refatorar
```

Build, extração de JSON, loader, núcleo compartilhado ou pipeline só são aceitáveis se forem auxiliares, lossless e não substituírem o HTML publicado como artefato canônico.

## 3. Regra absoluta de alteração: nunca reduzir

Regra operacional:

> **Nunca reduzir. Só corrigir, ampliar, restaurar ou refinar sem perda.**

Não compacte módulo robusto. Não remova caso clínico. Não apague feedback longo. Não substitua fisiologia específica por abstração genérica. Não corte nuances para “limpar” o arquivo. Não transforme uma ferramenta didática rica em apostila minimalista.

Quando precisar corrigir:

1. preserve o conteúdo existente;
2. identifique a falha real;
3. corrija localmente;
4. acrescente se necessário;
5. teste;
6. não reescreva por vaidade arquitetural.

## 4. Estado atual do Respira

Respira possui 10 módulos principais:

1. `mvp1-interativo.html` — Como o ar entra e sai: via aérea, gradiente, diafragma, resistência, complacência, congestão, constante de tempo e auto-PEEP.
2. `mvp2-interativo.html` — Saturar não é respirar bem: oxigenação, ventilação, curva O₂-Hb, monóxido, anemia e entrega.
3. `mvp3-interativo.html` — Onde o ar e o sangue se encontram: V/Q, shunt, espaço morto, resposta ao oxigênio, PEEP e recrutamento.
4. `mvp4-interativo.html` — Gasometria como narrativa: pH, pCO₂, HCO₃⁻, compensação, Winter, ânion-gap e bancada guiada.
5. `mvp5-interativo.html` — Arquitetura que respira: Laplace, surfactante, colapso, recrutamento, PEEP.
6. `mvp6-interativo.html` — Grandes síndromes respiratórias.
7. `mvp7-interativo.html` — Terapêutica como forças sobre eixos fisiológicos.
8. `mvp8-interativo.html` — Oxigênio e suporte não invasivo.
9. `mvp9-interativo.html` — Ventilação mecânica: equação do movimento, VCV/PCV, ondas, pausa, auto-PEEP.
10. `mvp10-interativo.html` — Ventilação protetora e desmame.

O índice principal é `index.html`.

Wrappers canônicos em `/modules/` podem existir para navegação e nomenclatura, mas os arquivos legados continuam válidos.

## 5. Estado atual do Ventila

Ventila está organizado por `ventila.html` e módulos de raiz `ventila0.html` a `ventila26.html`.

A matriz atual é:

| Nº | Arquivo | Tese / função |
|---:|---|---|
| 00 | `ventila0.html` | Gramática da máquina: modos, variável controlada, variável livre, tempo, fluxo, contrato causal |
| 01 | `ventila1.html` | Por que este paciente está no ventilador? A causa do tubo vem antes do modo |
| 02 | `ventila2.html` | Máquina, circuito, tubo e paciente: onde está o defeito? |
| 03 | `ventila3.html` | Curvas I: pressão, fluxo e volume como semiologia em tempo real |
| 04 | `ventila4.html` | Curvas II: loops P-V e F-V, valor isolado versus relação entre variáveis |
| 05 | `ventila5.html` | VCV: volume é promessa, pressão é consequência |
| 06 | `ventila6.html` | PCV: pressão por tempo, volume como consequência |
| 07 | `ventila7.html` | Híbridos/adaptativos/PRVC: controlador não é médico |
| 08 | `ventila8.html` | PSV, CPAP, SIMV e trabalho respiratório |
| 09 | `ventila9.html` | Assincronias: drive neural versus entrega mecânica |
| 10 | `ventila10.html` | Sedação e BNM: esforço entre P-SILI e atrofia diafragmática |
| 11 | `ventila11.html` | Fenótipos → plano: “intubado” não é diagnóstico |
| 12 | `ventila12.html` | Desmame/extubação/falha: respirar e proteger são portões diferentes |
| 13 | `ventila13.html` | Traqueostomia como plataforma de desmame + Mega Revisão Parte 1 |
| 14 | `ventila14.html` | Aplicação integrada: pulmão na tela + Mega Revisão Parte 2 |
| 15 | `ventila15.html` | Tutor visual PSV · VCV · PCV: consolidação dos modos e inversão causal |
| 16 | `ventila16.html` | Tutor adaptativo de sessão: BKT, grafo de pré-requisitos e remediação dirigida |
| 17 | `ventila17.html` | SDRA — recrutabilidade antes da PEEP: PEEP só compra pulmão quando recrutamento supera hiperdistensão e custo hemodinâmico. |
| 18 | `ventila18.html` | Obstrutivo grave — dar tempo para sair: Resistência, constante de tempo, auto-PEEP e hipercapnia permissiva sem perseguir números com FR lesiva. |
| 19 | `ventila19.html` | Coração-pulmão — o VD no ventilador: Retorno venoso, resistência vascular pulmonar e septo: a pressão positiva vista pelo ventrículo direito. |
| 20 | `ventila20.html` | Neuroventilação — CO₂ também é hemodinâmica: PaCO₂, fluxo cerebral, PIC e o preço isquêmico da hiperventilação mantida. |
| 21 | `ventila21.html` | Prona e resgate — redistribuir antes de escalar: Posição como terapia da heterogeneidade: V/Q, estresse regional e resposta que vai além da SpO₂. |
| 22 | `ventila22.html` | APRV — abrir sem aprisionar: Phigh/Plow não bastam: T-high, T-low e terminação do fluxo governam recrutamento e ventilação. |
| 23 | `ventila23.html` | ECMO e ECCO₂R — quando a máquina compra proteção: Fluxo, sweep, referência precoce e ultraprotação: suporte extracorpóreo como ponte, não cura. |
| 24 | `ventila24.html` | Obesidade, gestação e abdome — a parede pesa: Complacência do sistema não é complacência pulmonar: parede e abdome mudam a leitura das pressões. |
| 25 | `ventila25.html` | Pediatria e neonatologia — pulmão pequeno, tempo curto: Tubo estreito, vazamento, volume garantido e a física específica do recém-nascido e da criança. |
| 26 | `ventila26.html` | Fora da UTI — transporte e contingência: Oxigênio, bateria, circuito, fixação e plano B: robustez operacional faz parte da ventilação. |

Não rebaixar a série para 12 módulos. Ventila agora tem 0–26.

## 6. Cinco blocos obrigatórios por módulo Ventila

Cada módulo Ventila deve preservar, quando aplicável, cinco blocos estruturais:

1. **Caso clínico evolutivo** — em cinco atos, com pegadinha real.
2. **Trilha socrática conceitual** — perguntas graduais que constroem o mecanismo.
3. **Ilustração dinâmica em movimento** — animação-mãe específica do módulo.
4. **Laboratório / instrumento interativo** — controles, presets e readouts manipuláveis.
5. **Quiz socrático** — alternativas enxutas, plausíveis e feedback robusto.

A ordem visual pode variar conforme o módulo, mas a função didática deve estar presente. Alguns módulos especiais, como Ventila 15, podem expandir o padrão com múltiplos tutores, desde que não removam a progressão socrática nem a camada visual/interativa.

## 7. Caso clínico em cinco atos

O caso não é vinheta decorativa. Ele é o campo de prova do mecanismo.

Estrutura preferencial:

1. **Entrada** — por que o paciente chegou ao ventilador?
2. **Leitura** — dados clínicos, parâmetros, gasometria, curvas, exame e contexto.
3. **Decisão** — qual ajuste ou conduta parece lógica?
4. **Pegadinha** — qual decisão intuitiva pioraria o cenário?
5. **Reavaliação** — o que muda ao aplicar a leitura correta?

O caso deve alimentar o laboratório ou, no mínimo, dialogar explicitamente com ele. Evite caso solto seguido de ferramenta genérica.

## 8. Contrato psicométrico das questões

Cada questão deve ter quatro alternativas curtas e plausíveis. A resposta correta não deve ser identificável por tamanho, posição, complexidade gramatical ou quantidade de detalhes.

Distrator bom é hipótese errada por confusão de mecanismo. Distrator ruim é alternativa obviamente falsa.

A robustez deve ir para o feedback, não para uma alternativa correta longa demais.

Feedback robusto deve, quando possível, cobrir cinco campos:

1. **Mecanismo** — fisiologia ou mecânica causal.
2. **Por que a correta** — qual variável resolve o problema.
3. **A armadilha** — por que a opção sedutora engana.
4. **À beira do leito** — implicação prática.
5. **Ponte** — link para outro módulo Ventila ou fundamento Respira.

O bridge deve apontar para dentro do Ventila e/ou para Respira quando o fundamento já existir.

## 9. Gramática visual obrigatória

Ventila não deve virar apostila de modos. O aluno precisa ver o mecanismo mexer.

Gramática por módulo:

- Ventila 0: contrato dos modos, variável controlada/livre, tempo de ciclo e área do fluxo.
- Ventila 1: mapa de falhas que levam ao tubo.
- Ventila 2: circuito, sensores, tubo, cuff, paciente e defeitos pré-alveolares.
- Ventila 3: ondas pressão/fluxo/volume com playhead.
- Ventila 4: loops P-V e F-V.
- Ventila 5: volume garantido e pressão consequente.
- Ventila 6: pressão por tempo e volume consequente.
- Ventila 7: algoritmo adaptativo perseguindo alvo.
- Ventila 8: divisão de trabalho paciente × máquina.
- Ventila 9: drive neural, esforço muscular e entrega mecânica.
- Ventila 10: drive, esforço, sedação, BNM, P-SILI e atrofia.
- Ventila 11: classificador fenotípico e plano ventilatório.
- Ventila 12: SBT, RSBI, proteção de via aérea e falha cardíaca do desmame.
- Ventila 13: trabalho resistivo do tubo, traqueostomia e decanulação.
- Ventila 14: campo alveolar recrutável/não recrutável, shunt, hiperdistensão, auto-PEEP.
- Ventila 15: tutor visual comparativo PSV/VCV/PCV, curvas, pulmão esquemático e tutores de leitura.

## 10. Motores e validação

Mantenha fórmulas em funções puras, com unidades claras.

Motores já usados no projeto incluem:

- equação do movimento: `Paw = R·fluxo + V/C + PEEP`;
- VCV com fluxo constante e pausa;
- PCV/PSV com fluxo decelerante;
- constante de tempo `τ = R·C`;
- auto-PEEP por expiração incompleta;
- estimativas de driving, mechanical power, RSBI, shunt, recrutamento, hiperdistensão e trabalho resistivo;
- Tier-2 com RK4 quando há esforço do paciente e `Pmus(t)`.

Antes de publicar ou alterar um motor:

1. validar sintaxe;
2. conferir unidades;
3. testar presets extremos;
4. comparar com forma fechada quando houver;
5. checar invariantes;
6. declarar limitações na caixa de honestidade.

## 11. Regras de arquivo

Respira:

- `index.html`
- `mvp1-interativo.html` a `mvp10-interativo.html`
- aliases/wrappers em `/modules/` quando existirem
- arquivos auxiliares em `assets/` e `data/` quando já estiverem presentes

Ventila:

- `ventila.html` — índice da Parte B
- `ventila0.html` a `ventila26.html` — módulos publicados canônicos

Não mover Ventila para `/modules/` se isso criar dependência ou confusão. Aliases estáticos podem ser aceitos futuramente, mas não substituem os arquivos de raiz.

## 12. Regras de alteração

Proibido:

- reduzir conteúdo sem pedido explícito e sem justificativa;
- apagar blocos didáticos ricos;
- transformar módulo interativo em texto estático;
- substituir mecanismo por protocolo;
- remover deep-links Respira↔Ventila;
- quebrar rotas públicas antigas;
- introduzir build obrigatório;
- criar dependência externa além das fontes Google já usadas;
- usar `localStorage`/`sessionStorage` sem decisão explícita;
- omitir disclaimer de modelo simplificado;
- prometer que estimativa didática é dado de paciente real.

Obrigatório:

- manter PT-BR;
- manter identidade visual;
- manter rodapé autoral e dedicatória quando presentes;
- testar clique básico de abas/trilhas/quizzes;
- preservar `prefers-reduced-motion` quando houver animação contínua;
- manter `aria-label`/semântica razoável em controles novos;
- checar links relativos.

## 13. Estilo

Use português brasileiro.

Tom: socrático, direto, sofisticado e clínico. Evite tom catedrático.

Prefira perguntas como:

- “Qual falha levou ao tubo?”
- “O alvéolo sentiu essa pressão ou ela morreu no cano?”
- “Quem iniciou o ciclo: paciente ou máquina?”
- “A sedação tratou sofrimento, drive ou só calou a curva?”
- “O paciente falhou a bomba, o pulmão, a via aérea ou o coração?”
- “Neste modo, fluxo é causa ou consequência?”

Evite:

- “Decore estes parâmetros.”
- “O modo X é sempre melhor.”
- “Sempre faça...” sem contexto.
- “Nunca faça...” sem mecanismo.

## 14. Segurança e honestidade

Este projeto é material didático. Não deve se apresentar como prescrição individual, protocolo institucional ou substituto de julgamento clínico.

Quando usar limiares como driving pressure, mechanical power, RSBI, TTI, P/F, PEEP, auto-PEEP ou trabalho resistivo, deixe claro quando são heurísticas, aproximações didáticas, associações populacionais ou preditores imperfeitos.

Quando usar modelos de compartimento único, declare que o pulmão real é heterogêneo.

Quando abordar fármacos, mantenha foco em mecanismo, indicação, risco e monitorização. Não transformar em tabela prescritiva isolada.

## 15. Definição de sucesso

Um módulo está pronto quando:

1. abre diretamente como HTML;
2. roda sem build;
3. preserva sua tese;
4. tem caso/visual/lab/trilha/quiz ou expansão equivalente;
5. possui pegadinha clínica real;
6. usa mecanismo, não protocolo decorado;
7. tem feedback robusto;
8. possui caixa de honestidade;
9. mantém links internos;
10. não reduz conteúdo preexistente.

Definição do projeto:

> Respira ensinou a respirar pensando. Ventila deve ensinar a usar a máquina sem apagar o mecanismo que ela está substituindo.
