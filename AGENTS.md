# AGENTS.md — Respira / Ventila

Este arquivo orienta agentes, assistentes, Codex e colaboradores automatizados que venham a trabalhar neste repositório. O projeto tem uma tese pedagógica, uma identidade visual, uma arquitetura didática e critérios psicométricos definidos. Não trate os arquivos como HTML solto.

## 1. Missão do projeto

O repositório hospeda a série **Respira** e deverá hospedar a continuação **Ventila**.

**Respira** é a Parte A: fisiologia respiratória, oxigenação, relação V/Q, gasometria, síndromes, terapêutica, suporte não invasivo e fundamentos de ventilação mecânica.

**Ventila** será a Parte B: ventilação mecânica aprofundada, em progressão socrática, visual, interativa e clinicamente aplicada.

Tese editorial do Ventila:

> O ventilador não é tratamento em si. É uma intervenção mecânica que compra tempo, transfere trabalho, impõe energia e cria riscos.

Essa tese deve orientar perguntas, casos, pegadinhas, laboratórios, animações e feedbacks.

## 2. Estado atual do Respira

A série Respira está publicada com 10 módulos:

1. `mvp1-interativo.html` — Como o ar entra e sai.
2. `mvp2-interativo.html` — Saturar não é respirar bem.
3. `mvp3-interativo.html` — Onde o ar e o sangue se encontram.
4. `mvp4-interativo.html` — A gasometria como narrativa.
5. `mvp5-interativo.html` — A arquitetura que respira.
6. `mvp6-interativo.html` — As grandes síndromes.
7. `mvp7-interativo.html` — A terapêutica: as forças.
8. `mvp8-interativo.html` — Oxigênio e suporte não invasivo.
9. `mvp9-interativo.html` — Ventilação mecânica: fundamentos.
10. `mvp10-interativo.html` — Ventilação protetora e desmame.

O índice principal é `index.html`.

Há uma camada de refinamento psicométrico em `respira-quiz-refiner.js`. Ela surgiu para corrigir um viés identificado nos módulos posteriores: a resposta correta tendia a ser reconhecível por ser morfologicamente maior. A decisão pedagógica foi transferir a robustez para o feedback, não para a alternativa.

## 3. Regra editorial central: nada genérico

Evite soluções genéricas. Em especial:

- Não aumente alternativas com frases neutras apenas para nivelar tamanho.
- Não use distratores absurdos ou obviamente inferiores.
- Não escreva feedback reaproveitável entre módulos.
- Não publique versões compactas quando a solicitação for robustez.
- Não separe laboratório e caso clínico como peças independentes quando o caso deve alimentar o laboratório.

O padrão correto:

- Alternativas curtas, específicas e plausíveis.
- Gabarito longo, causal, memorável e específico.
- Laboratório visual que demonstra o mecanismo.
- Caso clínico que força decisão.

## 4. Contrato psicométrico das questões

Cada questão deve ter quatro alternativas curtas e plausíveis. A resposta correta não deve ser identificável por tamanho, posição, complexidade gramatical ou quantidade de detalhes.

A distribuição da resposta correta deve ser balanceada entre A/B/C/D ao longo do módulo.

Distrator bom é hipótese errada por confusão de mecanismo. Distrator ruim é alternativa obviamente falsa.

### Feedback obrigatório em Ventila

Novas questões do Ventila devem usar feedback estruturado:

```js
{
  block: "Pico alto",
  stem: "Em VCV, o pico subiu e o platô ficou normal. Qual termo da equação mudou?",
  opts: ["resistência", "complacência", "PEEP", "volume alveolar"],
  answer: 0,
  feedback: {
    mechanism: "A pausa zera fluxo; se o platô não sobe, o componente elástico não mudou.",
    whyRight: "A diferença pico-platô representa o componente resistivo.",
    trap: "Complacência ruim também aumenta pressão, mas elevaria o platô.",
    bedside: "Procure problema de via aérea, tubo, circuito ou resistência antes de tratar como pulmão rígido.",
    bridge: [
      { label: "Laboratório interno", href: "ventila5.html#lab-pausa" },
      { label: "Mecânica do Respira", href: "mvp1-interativo.html#r=20&c=0.08&rr=24&m=sim" }
    ]
  }
}
```

Campos obrigatórios:

1. `mechanism` — mecanismo fisiológico ou mecânico.
2. `whyRight` — por que a correta resolve o mecanismo.
3. `trap` — por que a alternativa sedutora engana.
4. `bedside` — implicação prática à beira-leito.
5. `bridge` — ponte para laboratório interno e/ou módulo Respira.

O `bridge` deve apontar tanto para dentro do Ventila quanto para fora, quando o fundamento já existir no Respira.

## 5. Cinco blocos obrigatórios por módulo Ventila

Cada módulo Ventila deve conter cinco blocos obrigatórios:

1. **Trilha socrática conceitual** — perguntas graduais que constroem o mecanismo.
2. **Ilustração dinâmica em movimento** — animação-mãe específica do módulo.
3. **Laboratório interativo** — controles e readouts manipuláveis.
4. **Caso clínico evolutivo** — caso obrigatório, integrado ao laboratório.
5. **Quiz socrático** — alternativas enxutas e feedback robusto.

O caso clínico não é vinheta decorativa. Ele deve alimentar o estado inicial do laboratório e reaparecer na decisão final.

O caso deve seguir cinco atos:

1. Entrada — por que o paciente chegou ao ventilador?
2. Leitura — dados clínicos, parâmetros, gasometria, curvas e exame.
3. Decisão — qual ajuste ou conduta parece lógica?
4. Pegadinha — qual decisão intuitiva pioraria o cenário?
5. Reavaliação — o que mudou depois da intervenção?

## 6. Schema consolidado de módulo Ventila

Use este contrato de dados como referência:

```js
const MODULE = {
  id: "ventila3",
  title: "Curvas I: pressão, fluxo e volume",
  thesis: "Curvas são semiologia: pressão mostra custo, fluxo mostra tempo, volume mostra entrega e retorno.",

  patient: {
    entrada: {
      summary: "Paciente obstrutivo intubado por exaustão, agora piora após aumento de frequência.",
      whyVentilated: "bomba + obstrução + fadiga",
      phenotype: "bomba"
    },
    vent: { mode: "VCV", VT: 450, RR: 28, flow: 50, PEEP: 5, FiO2: 40 },
    gaso: { pH: 7.25, PaCO2: 68, HCO3: 30, PaO2: 78 },
    curvas: {
      pressure: "pico alto progressivo",
      flow: "fluxo expiratório não zera",
      volume: "aprisionamento progressivo"
    },
    exame: {
      ausculta: "sibilos difusos",
      hemodinamica: "hipotensão após hiperinsuflação dinâmica"
    }
  },

  trail: [],

  visual: {
    engine: "waves",
    params: { animated: true, playhead: true, showPressure: true, showFlow: true, showVolume: true }
  },

  lab: {
    tier: 2,
    coupledTo: "patient",
    controls: ["RR", "flow", "R", "C", "PEEP", "VT"],
    readouts: ["Ppeak", "Pplat", "autoPEEP", "Te", "flowEndExp", "VE"],
    presets: ["normal", "obstrutivo", "restritivo", "tubo dobrado", "vazamento"]
  },

  quiz: [],

  reassess: {
    afterCorrectAction: "Reduzir frequência e alongar tempo expiratório reduz aprisionamento.",
    afterTrapAction: "Aumentar frequência piora aprisionamento e hemodinâmica."
  }
};
```

O objeto `patient` deve ser o preset inicial do laboratório. Não duplique estado clínico em estruturas independentes.

## 7. Arquitetura Ventila em 12 módulos

Ventila terá 12 módulos. Não force 10 por simetria com Respira.

### Ventila 1 — Por que este paciente está no ventilador?

Pergunta-mãe: qual falha levou ao tubo?

Eixos: comando, via aérea, bomba muscular, pulmão, troca gasosa, proteção e procedimento.

Ilustração: mapa animado de falhas do sistema respiratório.

Caso: paciente intubado por rebaixamento/proteção, com pulmão inicialmente preservado. Pegadinha: tratar como se fosse falência pulmonar primária.

### Ventila 2 — Máquina, circuito, tubo e paciente

Pergunta-mãe: onde está o defeito — máquina, circuito, tubo, via aérea ou pulmão?

Ilustração: fluxo no circuito com sensores, tubo, cuff, pulmão e válvula expiratória.

Caso: alarme de pressão alta com platô normal. Pegadinha: confundir problema resistivo/circuito com pulmão rígido.

### Ventila 3 — Curvas I: pressão, fluxo e volume

Golden module inicial. Deve ser o primeiro módulo Ventila construído.

Pergunta-mãe: que pergunta cada curva responde?

- Pressão: quanto custou empurrar o ar?
- Fluxo: o ar entrou e saiu no tempo certo?
- Volume: o que entrou voltou?

Ilustração: ondas P/F/V em tempo real, com playhead.

Caso: paciente obstrutivo com fluxo expiratório que não zera, aprisionamento e piora hemodinâmica após aumento de frequência. Pegadinha: aumentar frequência para “lavar CO2”.

### Ventila 4 — Curvas II: loops P-V e F-V

Pergunta-mãe: o que a relação entre variáveis revela que o valor isolado esconde?

Ilustração: loops P-V e F-V desenhados ciclo a ciclo.

Caso: melhora de saturação após aumento de PEEP, mas loop sugere hiperdistensão e a hemodinâmica piora. Pegadinha: achar que saturação melhor sempre significa ventilação melhor.

### Ventila 5 — VCV profundamente

Pergunta-mãe: se o volume é promessa, o que a pressão denuncia?

Ilustração: volume-alvo sendo entregue e pressão surgindo como consequência.

Caso: pico alto, platô seguro e sinais de resistência aumentada. Pegadinha: reduzir volume por medo de pressão de pico sem olhar platô.

### Ventila 6 — PCV profundamente

Pergunta-mãe: se a pressão é promessa, o que o volume denuncia?

Ilustração: pressão fixa insuflando pulmão; volume varia conforme resistência, complacência e tempo.

Caso: pressão igual, volume corrente cai e CO2 sobe após piora de complacência. Pegadinha: achar que está tudo seguro porque pressão não aumentou.

### Ventila 7 — Modos híbridos, adaptativos e PRVC

Pergunta-mãe: o modo adaptativo entendeu a doença ou só reagiu ao que mediu?

Ilustração: controlador ajustando pressão para perseguir volume-alvo.

Caso: esforço do paciente interfere na leitura do algoritmo. Pegadinha: confiar que o modo “inteligente” substitui raciocínio.

### Ventila 8 — PSV, CPAP, SIMV e trabalho respiratório

Pergunta-mãe: quanto do trabalho é do paciente e quanto é da máquina?

Ilustração: diafragma e ventilador dividindo trabalho.

Caso: paciente parece confortável em suporte alto, mas falha quando o suporte é reduzido. Pegadinha: interpretar conforto sob assistência alta como recuperação muscular.

### Ventila 9 — Assincronias paciente-ventilador

Pergunta-mãe: quem queria respirar, quando queria começar e quando queria parar?

Ilustração: drive neural, esforço muscular e entrega mecânica sobrepostos.

Caso: drive alto, duplo disparo e empilhamento de volume. Pegadinha: apenas aumentar sedação sem corrigir causa mecânica/metabólica da assincronia.

### Ventila 10 — Sedação, analgesia e bloqueio neuromuscular

Pergunta-mãe: estou tratando sofrimento, drive, sincronia ou mascarando erro mecânico?

Ilustração: fármacos movendo drive, consciência, dor, hemodinâmica e sincronia.

Caso: necessidade de controle profundo para estratégia ventilatória específica. Pegadinha: confundir bloqueio motor com sedação/analgesia.

Observação obrigatória: bloqueio motor não seda nem analgesia. O módulo deve tratar esse ponto com rigor ético e técnico.

### Ventila 11 — Fenótipos de intubação e plano ventilatório

Pergunta-mãe: “intubado” é diagnóstico ou consequência de diagnósticos diferentes?

Ilustração: árvore de plano ventilatório por motivo do tubo.

Caso: três pacientes com tubo e oximetria parecida, mas motivos diferentes para ventilação. Pegadinha: tratar todos como categoria homogênea.

### Ventila 12 — Desmame, extubação e falha pós-extubação

Pergunta-mãe: o paciente consegue respirar e proteger a via aérea sem a máquina?

Ilustração: balança carga × capacidade, com via aérea/proteção como trava separada.

Caso: paciente passa teste respiratório, mas falha por proteção de via aérea. Pegadinha: “passou no teste, pode extubar”.

## 8. Gramática visual obrigatória

Cada módulo deve ter uma animação-mãe:

- Ventila 1: mapa de falhas.
- Ventila 2: fluxo no circuito e tubo.
- Ventila 3: ondas pressão/fluxo/volume em tempo real.
- Ventila 4: loops P-V e F-V.
- Ventila 5: volume garantido e pressão consequente.
- Ventila 6: pressão garantida e volume consequente.
- Ventila 7: algoritmo adaptativo perseguindo alvo.
- Ventila 8: divisão de trabalho paciente × máquina.
- Ventila 9: drive neural versus entrega mecânica.
- Ventila 10: fármacos movendo drive, consciência e hemodinâmica.
- Ventila 11: plano por fenótipo de intubação.
- Ventila 12: balança carga × capacidade.

## 9. Exigência de engenharia: motor visual em tempo real

Ventila não deve virar 12 animações artesanais independentes. Crie um toolkit compartilhado:

- `ventila-core.css` — tema, cards, botões, feedback, layout.
- `ventila-core.js` — boot do módulo, trilha, feedback estruturado, navegação, deep-links.
- `ventila-visuals.js` — motor de cena em tempo real.
- `ventila-labs.js` — modelos, integradores, presets e readouts.

Requisitos mínimos do `ventila-visuals.js`:

- `requestAnimationFrame` para playhead e animações contínuas.
- SVG ou Canvas com API estável.
- Capacidade de desenhar ondas P/F/V sincronizadas.
- Capacidade de desenhar loops ciclo a ciclo.
- Separação entre estado fisiológico e camada visual.
- Play/pause/reset.
- Readouts derivados do mesmo estado usado para desenhar.

Para módulos com esforço do paciente, planeje suporte a integrador numérico, incluindo RK4 quando necessário. Não implemente modelos complexos antes da hora, mas mantenha a arquitetura pronta para `Pmus(t)`, drive neural e interação paciente-máquina.

## 10. Ordem de construção

Não comece pelo índice. Não comece por todos os módulos.

Construa primeiro o **Ventila 3** como golden module.

Ordem recomendada:

1. `ventila-core.css`
2. `ventila-core.js`
3. `ventila-visuals.js`
4. `ventila-labs.js`
5. `ventila3.html` completo nos cinco blocos obrigatórios
6. Revisão do golden module
7. Ventila 5 — VCV
8. Ventila 6 — PCV
9. Ventila 9 — Assincronias
10. Demais módulos
11. `ventila.html` ou integração no `index.html`

## 11. Critérios de qualidade

Antes de publicar ou atualizar um módulo, verifique:

- A tese do módulo está explícita?
- O caso clínico existe e alimenta o laboratório?
- A animação-mãe é específica do módulo?
- O laboratório manipula o mecanismo central?
- As alternativas são curtas e plausíveis?
- A correta não é previsível por tamanho ou posição?
- O feedback tem `mechanism`, `whyRight`, `trap`, `bedside` e `bridge`?
- O bridge aponta para Ventila e, quando útil, para Respira?
- Existe pegadinha clínica real?
- Há disclaimer quando o modelo é simplificado?
- O módulo preserva a identidade visual do projeto?
- O módulo funciona sem backend obrigatório?

## 12. Estilo

Use português brasileiro.

O tom deve ser socrático, direto, sofisticado e clínico. Evite tom catedrático. O aluno deve sentir que está sendo conduzido por perguntas e contradições produtivas.

Prefira perguntas como:

- “Qual falha levou ao tubo?”
- “O alvéolo sentiu essa pressão ou ela morreu no cano?”
- “Quem iniciou o ciclo: paciente ou máquina?”
- “A sedação tratou sofrimento, drive ou só calou a curva?”
- “O paciente falhou a bomba, o pulmão, a via aérea ou o coração?”

Evite:

- “Decore estes parâmetros.”
- “O modo X é sempre melhor.”
- “Sempre faça...” sem contexto.
- “Nunca faça...” sem mecanismo.

## 13. Segurança e honestidade

Este projeto é material didático. Não deve se apresentar como prescrição individual, protocolo institucional ou substituto de julgamento clínico.

Quando abordar fármacos, mantenha foco em mecanismo, indicação, risco e monitorização. Evite transformar o conteúdo em tabela prescritiva isolada.

Quando usar limiares como driving pressure, mechanical power, RSBI ou TTI, deixe claro quando são heurísticas, associações populacionais ou preditores imperfeitos.

Quando usar modelos de compartimento único, declare a limitação: pulmão real é heterogêneo.

## 14. Convenções de arquivo

Respira existente:

- `index.html`
- `mvp1-interativo.html` a `mvp10-interativo.html`
- `mvpX.html` quando houver arquivo base
- `respira-quiz-refiner.js`

Ventila novo:

- `ventila.html` — índice da Parte B, se criado.
- `ventila1.html` a `ventila12.html`
- `ventila-core.css`
- `ventila-core.js`
- `ventila-visuals.js`
- `ventila-labs.js`

Evite repetir CSS/JS em todos os módulos do Ventila. Respira nasceu artesanal; Ventila deve nascer modular.

## 15. Regras de alteração

- Não compacte módulo robusto sem pedido explícito.
- Não substitua conteúdo clínico específico por abstração genérica.
- Não remova deep-links para Respira sem motivo.
- Não altere o índice sem confirmar que os arquivos apontados existem.
- Não quebre rotas públicas antigas.
- Se usar alias/loader, documente a razão.

## 16. Definição de sucesso do Ventila 3

Ventila 3 estará pronto quando entregar:

1. Caso clínico inicial acoplado ao laboratório.
2. Ondas P/F/V animadas com playhead em tempo real.
3. Manipulação de R, C, RR, VT, fluxo, PEEP e vazamento/aprisionamento.
4. Readouts de pico, platô, auto-PEEP, tempo expiratório, fluxo no fim da expiração e ventilação minuto.
5. Pelo menos 10 questões com alternativas curtas e feedback de cinco campos.
6. Pelo menos três pegadinhas: aumentar frequência para reduzir CO2, confundir pico com platô, ignorar fluxo expiratório que não zera.
7. Bridges para Respira 1, Respira 4 e Respira 9 quando pertinente.
8. Disclaimer do modelo simplificado.

Se Ventila 3 ficar de pé nesse padrão, os outros módulos devem seguir o mesmo contrato.

## 17. Frase-guia

Respira ensinou a respirar pensando.

Ventila deve ensinar a usar a máquina sem apagar o mecanismo que ela está substituindo.
