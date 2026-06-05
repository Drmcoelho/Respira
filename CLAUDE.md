# CLAUDE.md — Projeto **VENTILA**

> **Instruções operacionais para qualquer instância de Claude (ou humano) que trabalhe neste projeto.**
> Leia este arquivo inteiro antes de escrever uma linha. Ele é a memória e a constituição do projeto.
> Ventila é a **Parte B** de uma obra cuja Parte A (**Respira**) já está no ar e validada. Ventila ensina a *não violentar a respiração quando a máquina entra na história*.

-----

## 0. TL;DR operacional — o que fazer ao abrir o projeto

1. **Não comece pelo índice.** Comece pela gramática visual: **Ventila 3 (Curvas I)** é o golden module.
1. Levante primeiro o **núcleo compartilhado** (`ventila-core`, `ventila-visuals`, `ventila-labs`, `ventila-quiz`). Ventila **não** pode ser artesanal módulo a módulo como o Respira foi — 12 módulos × 5 blocos = ~60 componentes; sem núcleo, o projeto afunda no peso.
1. Cada módulo é majoritariamente **dados** (um objeto `MODULE`), não código.
1. **Todo motor fisiológico é validado numericamente em Node antes de virar UI.** Número errado = erro clínico. Sem exceção.
1. Reuse os motores **já validados** do Respira (§3.3). Não os redescubra.
1. Mantenha: single-file por módulo, offline, navegação relativa, sem `localStorage`, identidade visual do Respira com acento próprio.
1. Idioma de saída: **PT-BR**; raciocínio técnico/código em inglês quando útil. Prosa com setas e encadeamento, listas só quando a forma do conteúdo é lista.

-----

## 1. Identidade e proveniência

- **Autor:** Dr. Matheus M. Coelho · CRM-SP 151.318 · Limeira/SP.
- **Dedicatória recorrente:** “Para a Dani” (presente em todo módulo, discreta, no rodapé/fecho).
- **Licença/intenção:** *Livre para usar, compartilhar e ensinar.* Material didático, não substitui julgamento clínico.
- **Respira (Parte A, no ar):** `https://drmcoelho.github.io/Respira/` — 10 módulos interativos + `ideia.html` (manifesto).
- **Ventila (Parte B, a construir):** 12 módulos. Modos ventilatórios merecem espaço próprio — por isso 12, não 10.

-----

## 2. A TESE (o critério editorial que decide cada pegadinha)

> **Ventilar é governar uma interação entre paciente, máquina, tubo, pulmão, drive neural, fármacos e tempo. O ventilador não é tratamento; é uma intervenção mecânica que compra tempo, transfere trabalho, impõe energia e cria riscos.**

Os quatro verbos viram eixos mensuráveis — e já temos motor para cada:

- **compra tempo** → reverter a falha que levou ao tubo (Ventila 1, 11).
- **transfere trabalho** → divisão diafragma × máquina; carga × capacidade (Ventila 8, 12).
- **impõe energia** → *mechanical power*, driving pressure, VILI (Ventila 4, 5, 6, 10-proteção).
- **cria riscos** → assincronia, hiperdistensão, auto-PEEP, falha de extubação (Ventila 9, 12).

**Não pode virar apostila de modos.** O eixo é sempre: *por que está na máquina → o que a máquina controla → o que varia como consequência → está sincronizado ou lutando → a sedação trata sofrimento/drive ou mascara erro mecânico → o pulmão está protegido ou ferido → já dá para devolver o trabalho?*

Regra de ouro de questão (herdada do Respira, reforçada): **mecanismo sobre protocolo**, alternativas curtas/plausíveis/equilibradas, **nunca “correta por morfologia”** (a certa não é a mais longa), gabarito longo e estruturado.

-----

## 3. HERANÇA DO RESPIRA — ativos validados a reusar (não redescobrir)

### 3.1 Os 10 módulos do Respira e o que cada um contém

|Arquivo                |Conteúdo                                                                                                       |Motor reusável em Ventila                |
|-----------------------|---------------------------------------------------------------------------------------------------------------|-----------------------------------------|
|`mvp1-interativo.html` |Mecânica: R, C, τ=R·C, auto-PEEP, frequência como manobra                                                      |aprisionamento/auto-PEEP (V3)            |
|`mvp2-interativo.html` |Curva da Hb (Severinghaus+P50), conteúdo×saturação×entrega, CO                                                 |oxigenação/entrega                       |
|`mvp3-interativo.html` |V/Q, shunt × espaço morto, A–a, P:F                                                                            |troca; espaço morto                      |
|`mvp4-interativo.html` |Gasometria (Henderson-Hasselbalch, Winter, AG corrigido, Δ-Δ)                                                  |ácido-base; hipercapnia permissiva       |
|`mvp5-interativo.html` |Laplace P=2T/r, surfactante, PEEP-recrutamento                                                                 |recrutamento; driving                    |
|`mvp6-interativo.html` |As grandes síndromes (curadoria de estados via deep-link)                                                      |padrão de “Sala”                         |
|`mvp7-interativo.html` |Terapêutica como força sobre um eixo (6 famílias)                                                              |padrão de famílias                       |
|`mvp8-interativo.html` |O₂ e suporte não invasivo (FiO₂ entregue × demanda; Venturi/HFNC/CPAP/BiPAP)                                   |**semente de Ventila 8**                 |
|`mvp9-interativo.html` |VM fundamentos: equação do movimento, VCV/PCV, ondas P/F/V, pausa inspiratória, auto-PEEP, veredito pico↔platô |**MOTOR TIER-1 — semente de V3,4,5,6**   |
|`mvp10-interativo.html`|Protetora & desmame: mechanical power, VC/kg(PBW), hipercapnia permissiva, RSBI/TTI, falha bomba/pulmão/coração|**semente de V12 e dos alvos protetores**|

### 3.2 Parâmetros de hash (deep-link) de cada lab — **verificados no arquivo vivo**

Use exatamente estes nomes; um link com parâmetro errado nasce morto.

```
mvp1  #r= c= rr=                       &m=sim       (R cmH2O/(L/s); C em L/cmH2O, múltiplos de 0.005; RR 8–35)
mvp2  #pao2= p50= hb= co=              &m=curve     (p50 e hb passo 0.5)
mvp3  #s= d= f= c=                     &m=lab       (s shunt 0–50; d 30–70; f 21–100; c 0/1)
mvp4  #ph= co2= hco3= na= cl= alb=     &m=bench
mvp5  #ra= rb= peep= surf=             &m=lab       (ra/rb passo 5; surf 0/1)
mvp9  #lab
mvp10 #lab | #proteger | #desmamar
```

### 3.3 MOTORES FISIOLÓGICOS VALIDADOS — fórmulas e constantes (copiar verbatim)

> Todos abaixo foram conferidos numericamente contra forma fechada em Node. **Unidades internas SI:** C em **L/cmH₂O**, fluxo em **L/s**, VT em **L**, pressões em **cmH₂O**, tempos em **s**, RR em **/min**.

**(a) Equação do movimento** — base de tudo:

```
P_via_aérea(t) = R·fluxo(t) + V(t)/C + PEEP
```

**(b) VCV (fluxo quadrado), forma fechada:**

```
Ti      = VT / fluxo
τ       = R·C
Te      = 60/RR − Ti
Ppico   = R·fluxo + VT/C + PEEP
Pplatô  = VT/C + PEEP
ΔP(driving) = VT/C
resistivo   = Ppico − Pplatô = R·fluxo
Vtrap   = VT · e^(−Te/τ)          → auto-PEEP = Vtrap / C
Pmédia  = [ (PEEP+R·fluxo)·Ti + fluxo/(2C)·Ti² + PEEP·Te + (VT/C)·τ·(1−e^(−Te/τ)) ] / (60/RR)
```

**(c) PCV (pressão quadrada, fluxo desacelerante):**

```
VT     = Pinsp · C · (1 − e^(−Ti/τ))     ← volume é DEPENDENTE (perigo silencioso: cai com C)
Ppico  = PEEP + Pinsp
Pplatô = PEEP + VT/C
fluxo(t) = (Pinsp/R)·e^(−t/τ)
```

**(d) Mechanical power (Gattinoni simplificado, VCV) — J/min:**

```
MP = 0.098 · RR · VT · (Ppico − ½·ΔP_elástico)        // VT em L
   = 0.098 · RR · VT · (PEEP + ½·ΔP_el + resistivo)
Alvo lesivo ≈ > 17 J/min (associação populacional, não corte individual).
```

**(e) Peso predito (PBW) e VC/kg:**

```
PBW(M) = 50   + 0.91·(altura_cm − 152.4)
PBW(F) = 45.5 + 0.91·(altura_cm − 152.4)
VTkg   = VT_mL / PBW            // o VC se ajusta pela ALTURA, não pelo peso real
```

**(f) Ventilação alveolar / hipercapnia permissiva:**

```
Vd    = 2.2 · PBW            (mL, espaço morto anatômico)
VA    = (VT_mL − Vd) · RR / 1000   (L/min)
PaCO2 = clamp(172.6 / VA, 20, 140)      // 172.6 ≈ 0.863·VCO2(200) ; calibra PaCO2≈40 em VA normal
pH    = 7.40 − 0.008·(PaCO2 − 40)        // acidose respiratória AGUDA, antes da compensação renal
```

**(g) FiO₂ entregue × demanda (Módulo 8 / suporte de O₂):**

```
Demanda D∈[0,100]:  RR = 14 + 0.26·D ;  VT = 430 + 2.2·D
VE = RR·VT/1000 ;  MIF (fluxo insp. médio) = VE / 0.33
Baixo fluxo:  FiO2 = 0.21 + 0.79·clamp(Vcap/MIF, 0, fmax)
              Vcap = fluxo_O2 + bônus_máscara + (reservatório_mL·RR/1000)
              fmax: cânula 0.44 · máscara simples 0.60 · não-reinalante 0.90
Venturi:      FiO2 = ajuste (fixo, por desenho — fluxo total alto desacopla da demanda)
Alto fluxo:   FiO2 = ajuste·cov + 0.21·(1−cov) ;  cov = clamp(fluxo/(MIF·0.85), 0, 1)
```

**(h) Desmame — balanço carga × capacidade, RSBI, TTI:**

```
duty = 0.4 ;  meanflow = (VE_dem/duty)/60 ;  Pres = R·meanflow
VTcomf = 450 mL
esforço(VT) = (VT/C + Pres) / Pimax
VT = esforço(450) ≤ 0.4 ? 450 : clamp( C·(0.4·Pimax − Pres), 150, 450 )
RR  = clamp( VE_dem / (VT/1000), 8, 45 )
RSBI = RR / (VT/1000)          // > 105 prevê falha
TTI  = ((VT/C + Pres)/Pimax)·duty   // ≥ 0.15 → fadiga (pega o que o RSBI deixa passar)
Modos de falha: BOMBA (Pimax baixo) · CARGA (C baixo / R alto) · CORAÇÃO (reserva limítrofe → edema de desmame mesmo com RSBI bom).
```

### 3.4 Tokens de design (CSS) — herdar; Ventila ganha um acento próprio

```
--paper:#F4EFE4 --paper-deep:#EBE3D3 --ink:#16383B --ink-soft:#4A6164
--accent:#C0603A --accent-deep:#A24B2C --air:#3C7F86 --tissue:#C97F66
--correct:#4E7C5A --correct-bg:#E4ECE0 --wrong:#B0503E --wrong-bg:#F0E1DB
--warn:#B8862F --warn-bg:#F2E9D2 --line:#D7CCB8 --shadow:rgba(22,56,59,.13)
Fontes: Fraunces (display serif) · Hanken Grotesk (corpo) · JetBrains Mono (números/código)
Textura: overlay de ruído SVG opacity .04 (já usado no Respira)
```

**Acento Ventila (proposto, a confirmar):** introduzir `--signal` (um aço/ciano frio, ex. `#2E6E8E`) para diferenciar “máquina” de “fisiologia”, lendo como curso-irmão. *Default: aplicar.*

### 3.5 Lições do Respira (o que amadureceu — não repetir os erros)

- **Verifique o HTML cru, não o cache.** Já houve falso alarme por `web_fetch` desatualizado e por âncora que envolve o card inteiro. Use `curl` + parsing do markup real.
- **A âncora `<a>` pode envolver o card todo** → o texto de um card aparece antes do `href` do próximo. Cuidado ao inferir mapeamento.
- **jsdom não implementa `scrollIntoView`/`scrollTo`** → stubar em `beforeParse`.
- **`const` no topo do script NÃO vira propriedade de `window`** no jsdom; **`function` vira.** Para validar dados, exponha via funções ou dirija pelo DOM.
- **Sliders com `step`** “snapam” o valor → use valores na grade (ex. C múltiplo de 0.005).
- **Disclaimers de honestidade não são opcionais** — são parte da confiança.
- **O índice pode ser reconstruído e perder costuras** (ex.: link para `ideia.html` sumiu num rebuild). Releia o índice após mudanças.

-----

## 4. ARQUITETURA DO VENTILA (mais madura que o Respira)

### 4.1 Decisões de arquitetura

- **Distribuição:** 12 single-files (`ventila1.html`…`ventila12.html`) com o núcleo **inlined por um build Node mínimo** → preserva offline/compartilhável (propriedade inegociável herdada do Respira). *Não* SPA.
- **Núcleo compartilhado** mantido em fontes separadas e injetado no build (não copiar-colar como no Respira).
- **Landing:** `ventila.html` (índice da Parte B, padrão visual do Respira) + deep-links de volta aos labs do Respira para a fisiologia que fundamenta.

### 4.2 Arquivos do núcleo

```
ventila-core.css      tokens, layout, segbar, medidor, cards, verdicts, honestidade
ventila-core.js       motor da Trilha socrática + MÁQUINA DE ATOS do caso + deep-link por hash + modo
ventila-visuals.js    MOTOR DE CENA em tempo real (requestAnimationFrame) — ver §4.7
ventila-labs.js       Tier 1 (forma fechada) + Tier 2 (RK4 com P_músculo) + renderizador de ondas/loops — ver §4.8
ventila-quiz.js       render do quiz + schema de feedback de 5 campos — ver §4.6
build.mjs             injeta núcleo nos 12 single-files; roda a suíte de validação
validate/             scripts node+jsdom por módulo (ver §7)
modules/ventilaN.js   apenas o objeto MODULE (dados) de cada módulo
```

### 4.3 O contrato de dados `MODULE` (schema canônico — todo módulo implementa)

```js
const MODULE = {
  id: "ventila5",
  title: "VCV profundamente",
  thesis: "No VCV, volume é promessa; pressão é consequência.",

  // ATO 1 — o paciente abre o módulo; também é o ESTADO INICIAL do lab (acoplamento obrigatório)
  patient: {
    entrada: "Séptico, pneumonia. Intubado por insuficiência hipoxêmica + exaustão.",
    vent:   { mode:"vcv", VT:450, RR:22, flow:60, PEEP:8, FiO2:0.5 },
    gaso:   { pH:7.30, PaCO2:48, PaO2:78, HCO3:23 },
    exame:  "Roncos difusos, secreção espessa.",
    initialLabState: { R:18, C:38 }   // o lab CARREGA isto como condição inicial
  },

  trail: [ /* trilha socrática: {block, stem, opts, answer, feedback{...}} */ ],

  visual: { engine: "waves", params:{} },   // ver §4.7 — uma "animação-mãe" por módulo

  lab: {
    tier: 1,                                  // 1 = forma fechada · 2 = RK4 (esforço)
    coupledTo: "patient",                     // carrega patient.initialLabState
    controls: [ "VT","fluxo","Ti","pausa","PEEP","R","C","alarmePressao" ],
    readouts: [ "Ppico","Pplatô","ΔP","auto-PEEP","VT_exp","MP" ]
  },

  quiz: [ /* {block, stem, opts[4], answer, feedback{ mechanism, whyRight, trap, bedside, bridge }} */ ],

  // ATO 5 — fechamento: o que mudou após a intervenção
  reassess: { intervention:"Aspiração + broncodilatador", delta:"Pico 42→30; platô inalterado (24)." }
};
```

### 4.4 Os CINCO blocos obrigatórios (decisão travada: **5, não 4**)

1. **Trilha socrática conceitual** — do senso comum ao mecanismo; a resposta nunca vem antes da dúvida.
1. **Ilustração dinâmica em movimento** — a animação-mãe (§4.7), rodando, não SVG estático.
1. **Laboratório interativo** — sliders/presets; o mecanismo responde. **É o Ato 2/3 do caso.**
1. **Caso clínico evolutivo** — em 5 atos (§4.5); o “campo de prova”.
1. **Quiz socrático** — alternativas curtas; gabarito longo de 5 campos (§4.6).

### 4.5 O caso clínico em 5 ATOS, em 3 MOMENTOS

**Atos:** 1 Entrada (por que chegou ao tubo) · 2 Leitura (gaso, curvas, parâmetros, exame) · 3 Decisão (o que parece lógico) · 4 **Pegadinha** (a decisão intuitiva que pioraria) · 5 Reavaliação (o que mudou).
**Momentos (o caso NÃO fica depois do conteúdo):**

- **Abertura:** “este é o paciente” (`patient`).
- **Meio:** “mexa nas variáveis dele” — o **lab carrega `patient.initialLabState`**.
- **Fim:** “o que você faria agora?” — a pegadinha entra no quiz; `reassess` fecha.

> Isso transforma o módulo em **simulação de raciocínio**, não aula + perguntinhas. Caso e lab **partilham o mesmo objeto de estado**.

### 4.6 Schema de questão — feedback de 5 campos (o maior salto sobre o Respira)

```js
{
  block: "Pico alto",
  stem:  "Em VCV, o pico subiu e o platô ficou normal. Qual termo da equação mudou?",
  opts:  ["Resistência","Complacência","PEEP total","Volume alveolar"],  // curtas, plausíveis, equilibradas
  answer: 0,
  feedback: {
    mechanism: "A pausa zera o fluxo; sem fluxo não há R·fluxo, sobra só a pressão elástica (platô).",
    whyRight:  "Pico − platô = R·fluxo; platô normal ⇒ o custo extra está no cano, não no alvéolo.",
    trap:      "Complacência baixa também eleva pressão — mas elevaria o PLATÔ, não só o pico.",
    bedside:   "Procure secreção, broncoespasmo, tubo dobrado/mordido, água no circuito. Não assuma SDRA.",
    bridge:    "Acione a pausa no lab e aumente R: veja pico−platô crescer. (Fisiologia: Respira mvp1 #r=…)"
  }
}
```

**Regra:** a correta é curta; as erradas seduzem; a robustez vai TODA para o `feedback`. `bridge` aponta para dentro (lab/curva do módulo) **e/ou** de volta ao Respira (a fisiologia que fundamenta).

### 4.7 Motor visual — **cena em tempo real** (a diferença técnica nº1 vs Respira)

O Respira redesenhava SVG estático ao mover o slider. Ventila exige **animação-mãe rodando** (playhead, loops desenhados ciclo a ciclo, linhas de drive×máquina). Portanto `ventila-visuals.js` é um **motor de cena**, não uma coleção de funções de desenho:

- laço único `requestAnimationFrame`; pausável; respeita `prefers-reduced-motion`.
- “engines” parametrizáveis selecionados por `MODULE.visual.engine`:
  `failmap` (V1) · `circuit` (V2) · `waves` (V3) · `loops` (V4) · `vcv` (V5) · `pcv` (V6) · `adaptive` (V7) · `work` (V8) · `async` (V9) · `pharmaco` (V10) · `phenotree` (V11) · `balance` (V12).
- a cena **lê o mesmo estado do lab** (um tick atualiza física → ondas → leituras juntos).
- **`async` (V9) é a mais difícil**: três traços sobrepostos (drive neural, P_músculo, entrega) + tipos de assincronia. Prototipar cedo.

### 4.8 Motor de lab — DOIS TIERS

**Tier 1 — forma fechada (estende o mvp9 validado).** Paciente **passivo**, modos controlados. Cobre **V1, V2, V3, V4, V5, V6, V7, V11**. Já temos todas as fórmulas (§3.3 b–f).

**Tier 2 — integração numérica RK4 com `P_músculo(t)`.** Esforço espontâneo, PSV/CPAP/SIMV, modos adaptativos, assincronias, efeito de sedação/drive. Cobre **V8, V9, V10**. **Não tem forma fechada.** ODE a integrar (RK4, passo ~1–2 ms):

```
V'(t) = [ P_vent(t) + P_mus(t) − V(t)/C − PEEP ] / R
P_mus(t): meia-onda (seno) sobre o Ti NEURAL, amplitude = drive·força_muscular (negativa = puxa)
P_vent(t): 0 em CPAP/disparo; = Psup durante suporte (PSV); rampa (rise time); etc.
Disparo: por fluxo/pressão quando o esforço cruza o limiar (− trigger).
Ciclagem (PSV): quando fluxo cai a % do pico. Auto-PEEP realimenta P_alveolar de fim de expiração.
Assincronias EMERGEM do descompasso entre Ti neural e Ti mecânico, fluxo insuficiente, etc.
```

> O integrador RK4 é pré-requisito de V8–V10. **Confirmar o estado do integrador antes de detalhar o Tier-2.**
> Ambos os tiers partilham o mesmo **renderizador de ondas/loops** e o mesmo **motor de caso**.

### 4.9 Deep-links

- **Internos** (entre labs/curvas do próprio Ventila) via hash, padrão Respira.
- **De volta ao Respira** para a fisiologia base (ex.: recrutamento → `mvp5`, ácido-base → `mvp4`, auto-PEEP → `mvp1`). Mantém a escada Respira→Ventila viva sem duplicar fisiologia. Use os parâmetros de §3.2.

### 4.10 Doutrina de honestidade (caixa obrigatória em todo lab)

Declarar em voz alta as simplificações: compartimento único (pulmão real é heterogêneo, “baby lung”); platô pressupõe paciente passivo; mechanical power = equação simplificada e limiar populacional; PaCO₂ de modelo de VA com espaço morto fixo; RSBI/TTI são preditores imperfeitos — o TRE com o paciente decide; números são **estimativas didáticas, não prescrição**.

-----

## 5. A MATRIZ DOS 12 MÓDULOS (especificação)

Legenda: **T** = tier do lab · **Eng** = engine visual · **Pegadinha** = o Ato 4 (ativo clínico mais alto — preservar intacto).

|# |Módulo                           |T    |Eng      |Caso (1 linha)                                                           |Pegadinha                                       |Gabarito (núcleo)                                                                |
|--|---------------------------------|-----|---------|-------------------------------------------------------------------------|------------------------------------------------|---------------------------------------------------------------------------------|
|1 |Por que está no ventilador       |1*   |failmap  |Intox. BZD/opioide, Glasgow 6, pulmão limpo                              |tratar como SDRA (PEEP/pressões agressivas)     |“intubado” não é diagnóstico; o plano nasce da CAUSA do tubo                     |
|2 |Máquina, circuito, tubo, paciente|1    |circuit  |Pós-op, pulmão normal, pico alto súbito; platô normal; tubo mordido      |sedar/reduzir VC achando pulmão duro            |pico↑ + platô normal = pré-alveolar (resistência/circuito/tubo)                  |
|3 |**Curvas I (P/F/V)** ★golden     |1    |waves    |DPOC exausto, FR 28, fluxo exp. não zera, pico progressivo, hipotensão   |subir FR p/ “lavar CO₂”                         |falta tempo expiratório → auto-PEEP; reduzir FR, ↑fluxo, ↑Te, broncodilatar      |
|4 |Curvas II (loops P-V, F-V)       |1    |loops    |Aspirativa em VCV; ↑PEEP melhora SatO₂ mas driving sobe e PA cai         |SatO₂↑ = sempre mais protetor                   |PEEP recruta OU hiperdistende; proteção = driving/platô/complacência/hemodinâmica|
|5 |VCV profundamente                |1    |vcv      |Séptico, VCV 450; pico 28→42; platô 24; secreção                         |reduzir VC por medo de barotrauma (platô seguro)|em VCV pico alto pode ser só resistência; o alvéolo “vê” o platô/driving         |
|6 |PCV profundamente                |1    |pcv      |SDRA mod. PCV; piora radiológica; VT 420→260; PaCO₂↑                     |“pressão estável = seguro”                      |PCV fixa pressão; VOLUME é dependente e cai sem alarme de pressão                |
|7 |Híbridos/adaptativos (PRVC)      |1    |adaptive |Alvo 420 mL; esforço por acidose; máquina reduz pressão; mais taquipneico|confiar que o modo “entendeu”                   |controlador, não médico; vazamento/drive/ΔC enganam o algoritmo                  |
|8 |PSV/CPAP/SIMV e trabalho         |**2**|work     |PSV 14 confortável; PS 7 → FR 34, VT 260, RSBI piora                     |FR normal sob PSV alto = músculo bom            |PSV alto MASCARA fraqueza; desmame testa carga-capacidade com suporte baixo      |
|9 |Assincronias                     |**2**|async    |SDRA, sedação leve, drive alto, duplo disparo, breath stacking, driving↑ |só sedar sem corrigir causa/ajuste              |desencontro temporal drive×entrega; sedar pode apagar o sinal e manter o dano    |
|10|Sedação/analgesia/BNM            |**2**|pharmaco |SDRA grave pronado; curarizam com sedação superficial                    |BNM “seda”                                      |bloqueador paralisa, não seda/analgesia; sem sedação = violência ética           |
|11|Fenótipos → plano                |1*   |phenotree|3 tubos, mesma SatO₂: TCE / queimadura de via aérea / SDRA viral         |“intubado” como categoria única                 |o ventilador responde ao MOTIVO do tubo (planos diferentes)                      |
|12|Desmame/extubação/falha          |mvp10|balance  |TRE RSBI 72, mas tosse fraca + secreção + delirium → broncoaspira        |“passou no TRE → extubar”                       |desmame = respirar; extubação = respirar E proteger via aérea (4º eixo)          |

* V1 e V11 são **bookends**: V11 é a síntese aplicada de V1; construir como par. V1/V11 usam um seletor de fenótipo (lógica leve), não o motor de física pesado.

> **Concentração de risco:** V8, V9, V10 (Tier-2 RK4 + animação de assincronia). **Reuso máximo:** V3/V5/V6 são o mesmo motor Tier-1 visto de ângulos diferentes — construir o motor uma vez paga seis módulos (3,4,5,6,7,11).

Para a ficha completa de cada módulo (todas as pegadinhas e gabaritos detalhados), ver os documentos de planejamento fonte; este CLAUDE.md carrega o essencial executável.

-----

## 6. Padrões de código e estilo

- **Single-file** por módulo após build; durante dev, núcleo separado. Sem dependências externas além das **fontes Google** (degrada para fonte de sistema offline).
- **Proibido `localStorage`/`sessionStorage`** (e qualquer browser storage).
- **Sem frameworks.** JS vanilla. Funções top-level (para testabilidade jsdom), dados em `const MODULE`.
- **Acessibilidade:** `aria-label` em controles e modos; `aria-live` em leituras que mudam; `prefers-reduced-motion` respeitado pelo motor de cena.
- **Determinismo:** mesma entrada → mesma saída; nada de aleatoriedade não-semeada.
- **Números:** toda fórmula clínica vive em UMA função pura, testável, documentada com unidades. Nunca embutir número mágico sem comentário de unidade/fonte.
- **Idioma:** UI e conteúdo em PT-BR; identificadores/código em inglês.
- **Prosa de feedback:** mecanismo > protocolo; setas e encadeamento; sem “morfologia da resposta certa”.

-----

## 7. WORKFLOW DE VALIDAÇÃO (obrigatório antes de entregar qualquer módulo)

Padrão herdado e comprovado no Respira (`node` + `jsdom`). Para cada módulo:

```js
// 1) SINTAXE: new Function(<script>)  → compila?
// 2) RUNTIME jsdom:
const dom = new JSDOM(html, { runScripts:"dangerously", url,
  beforeParse(w){ w.Element.prototype.scrollIntoView=()=>{}; w.scrollTo=()=>{}; }});
// 3) TRILHA: start() → percorre N questões → chega ao fechamento.
// 4) MOTOR: recomputar a forma fechada INDEPENDENTEMENTE e exigir |Δ| < 0.1 nos presets-chave.
//    (Tier-2: validar invariantes — conservação de volume no ciclo, auto-PEEP↑ com Te↓, etc.)
// 5) CASO↔LAB: o lab carrega patient.initialLabState? as leituras batem com o caso?
// 6) QUIZ: todo feedback tem os 5 campos não-vazios.
// 7) DEEP-LINKS: regex de arquivo + parâmetros obrigatórios presentes + m=… (e mvp9/#lab).
// 8) Portão: imprimir "TUDO VERDE ✓" só se tudo passar.
```

- **Antes de construir um motor novo**, escrever um `modelN.js` de sanidade (como `model9.js`/`model10.js` do Respira) e conferir os números à mão contra a literatura.
- **Spot-check vivo:** após publicar, `curl` do HTML cru + checagem de HTTP 200 dos arquivos e dos deep-links.

-----

## 8. ORDEM DE CONSTRUÇÃO (de-risking)

1. **`ventila-core` + `ventila-quiz`** (tokens, trilha, máquina de atos, schema de feedback, deep-link, honestidade, harness). Barato — herda do Respira.
1. **Motor Tier-1 + renderizador de ondas + `ventila-visuals` (motor de cena)** — estender o mvp9, revalidar números.
1. **Ventila 3 (Curvas I) — GOLDEN MODULE completo nos 5 blocos.** Cria a gramática visual e prova o acoplamento caso↔lab. Trava o padrão e a régua de qualidade.
1. **Ventila 5 e 6** (VCV/PCV) — reusam motor+ondas; contraste direto; majoritariamente dados.
1. **Ventila 4** (loops) — adiciona traçado de loop ao motor de cena.
1. **Ventila 1 + 11** (bookends; seletor de fenótipo).
1. **Ventila 2 e 7** (circuito; adaptativo).
1. **Motor Tier-2 (RK4 + P_músculo)** + **Ventila 8, 9, 10** — risco concentrado; 9 (assincronias) é o pico de dificuldade visual.
1. **Ventila 12** (reusa mvp10) + **`ventila.html`** (índice) com deep-links de volta ao Respira.

> Ordem de **design do motor** começa pelas curvas (3); ordem de **publicação** pode ser 1→12.

-----

## 9. Decisões em aberto / riscos

- [ ] **Acento visual `--signal`** para Ventila (default: aplicar). — *confirmar*
- [ ] **Estado do integrador RK4** existente (pré-requisito de V8–V10). — *confirmar antes de detalhar Tier-2*
- [ ] **Build:** Node script de inline vs. manter núcleo via `<script src>` relativo (perde “1 arquivo”, mantém offline). Default: **build inline**. — *confirmar*
- [ ] Profundidade de V10 (farmacologia como vetores) sem virar bula — manter “fármaco move eixos (drive/consciência/hemodinâmica/sincronia)”, nunca doses.
- ⚠ **Risco nº1:** animação em tempo real + RK4 são genuinamente novos; não subestimar. Prototipar `async` (V9) cedo.
- ⚠ **Risco nº2:** peso do projeto — sem núcleo compartilhado, inviável.

-----

## 10. Definition of Done

**Por módulo:** 5 blocos presentes · motor validado numericamente (|Δ|<0.1 ou invariantes Tier-2) · trilha completa até o fechamento · caso acoplado ao lab (carrega `initialLabState`) · todo `feedback` com 5 campos · deep-links 200/válidos · caixa de honestidade · offline (só fontes externas) · `aria` · jsdom “TUDO VERDE ✓”.

**Do projeto:** 12 módulos + `ventila.html` no padrão Respira · deep-links de volta ao Respira vivos · índice religado e reauditado por `curl` · rodapé “Para a Dani · livre para usar, compartilhar e ensinar”.

-----

## Apêndice A — Gramática visual por módulo (a “animação-mãe”)

1 mapa de falhas do sistema · 2 fluxo no circuito/tubo · 3 ondas P/F/V em tempo real · 4 loops P-V e F-V desenhados ciclo a ciclo · 5 volume garantido → pressão consequente · 6 pressão garantida → volume consequente · 7 algoritmo perseguindo alvo · 8 divisão de trabalho paciente×máquina · 9 drive neural × entrega mecânica (3 traços) · 10 fármacos movendo drive/consciência/hemodinâmica · 11 árvore de plano por fenótipo · 12 balança carga×capacidade + trava de via aérea.

## Apêndice B — Glossário operacional

**VILI:** lesão induzida pelo ventilador (volu/baro/atelectrauma/biotrauma). **Driving pressure (ΔP):** Pplatô−PEEP = VT/C; alvo <15. **Mechanical power:** energia/min ao pulmão; alvo <17 J/min. **Auto-PEEP:** pressão de ar aprisionado por Te insuficiente. **RSBI:** FR/VC(L); >105 prevê falha. **TTI:** índice tensão-tempo; ≥0.15 → fadiga. **PBW:** peso predito pela altura (define VC/kg). **TRE:** teste de respiração espontânea. **P-SILI:** lesão autoinfligida pelo esforço. **Três falhas do desmame:** bomba (músculo), carga (pulmão/parede), coração (edema de desmame).

-----

*Fim do CLAUDE.md. Mantenha-o atualizado: ao decidir um item de §9, mova-o para a seção correspondente. Este arquivo deve sempre refletir o estado real do projeto.*
