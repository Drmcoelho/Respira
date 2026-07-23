# HEXÁPODE — GERAÇÃO 001: ESPECIFICAÇÃO VISUAL EXECUTÁVEL

> Plano operacional da IA 1 — Direção Visual.
>
> Escopo deste ciclo: **10 ativos canônicos de identidade visual**, reutilizáveis por Respira, Ventila e todos os demais braços do Projeto Hexápode.

---

## 0. Contrato global da geração

### 0.1 Função

A Geração 001 não ilustra uma especialidade. Ela estabelece o **sistema visual compartilhado** que permitirá produzir os demais 590 ativos sem deriva estética, sem reinvenção de símbolos e sem inconsistência entre atlas.

### 0.2 Formato canônico

- proporção principal: `4:3`;
- resolução-base: `1600 × 1200 px` ou superior;
- orientação: horizontal;
- fundo predominante: marfim quente;
- acabamento: editorial científico, vetorial, limpo e funcional;
- contornos: finos, regulares e predominantemente grafite;
- sombras: discretas ou ausentes;
- texturas: mínimas;
- texto incorporado pelo gerador: somente quando indispensável;
- rótulos exatos, números, códigos e tabelas: preferencialmente adicionados em SVG/HTML pelo Codex;
- sem logotipos comerciais;
- sem marcas-d’água;
- sem pacientes identificáveis;
- sem visual infantilizado, futurista genérico ou estética de banco de imagens.

### 0.3 Paleta semântica-base

| Papel | Cor | Hex |
|---|---|---|
| papel / marfim | fundo principal | `#F7F4EC` |
| papel profundo / bege | planos secundários | `#E8E1D1` |
| grafite / estrutura | texto, contornos e arquitetura | `#2B2E34` |
| petróleo / secundário | legendas e informações auxiliares | `#6A727A` |
| azul / máquina | dispositivos, comandos e tecnologia | `#1D4E7A` |
| teal / fluxo gasoso | ar, ventilação, fluxo e oxigenação | `#1696A3` |
| terracota / tecido-esforço | músculo, tecido e esforço fisiológico | `#C45A3C` |
| verde / resposta segura | estabilidade, proteção e recuperação | `#2E7D69` |
| vermelho / lesão | dano, sangramento e inflamação | `#B2473F` |
| âmbar / alerta | risco, atenção e mudança crítica | `#D39A2E` |
| areia / divisória | grades, separadores e linhas de apoio | `#DCD2BE` |

### 0.4 Pacote mínimo de cada ativo

Cada ativo deve produzir ou registrar:

```text
<asset-id>/
├── base-art.png
├── overlay.svg
├── prompt.md
├── metadata.yml
├── alt.txt
└── thumbnail.webp
```

O `base-art.png` deve conter a composição visual. O `overlay.svg` deve concentrar texto exato, rótulos, medidas, tabelas e elementos que não podem depender da ortografia do modelo gerador.

### 0.5 Critérios transversais de aceite

- reconhecível como parte do Hexápode mesmo sem título;
- utilizável em desktop e recortável para mobile;
- legível em miniatura;
- sem elementos puramente decorativos;
- sem ambiguidades de direção, hierarquia ou semântica cromática;
- componentes reutilizáveis isoladamente;
- coerente com `Docs/CODEX-VISION.md`;
- revisado visualmente sobre o arquivo renderizado, não apenas pelo prompt.

---

# 1. HEX-G001-001 — Paleta oficial

## Missão

Fixar a paleta semântica do ecossistema e demonstrar o papel funcional de cada cor.

## Composição

Prancha editorial em quatro zonas:

1. faixa de 11 amostras cromáticas;
2. tabela de função semântica;
3. pequenos exemplos aplicados em órgão, máquina, fluxo, alerta, lesão e resposta segura;
4. regras resumidas de contraste e combinação.

## Prompt canônico

```text
Create a canonical medical editorial design-system board for the Hexápode atlas ecosystem. Warm ivory paper background, refined scientific vector style, precise thin graphite linework, calm hierarchy and generous whitespace. Present eleven semantic color swatches for paper, deep paper, graphite structure, petroleum secondary text, machine-command blue, gas-flow teal, tissue-effort terracotta, safe-response green, injury red, alert amber and divider sand. Add small applied specimens showing the colors on a ventilator, airflow arrows, tissue, safety badge, lesion marker and warning badge. Functional, reusable, minimal, not decorative, no logos, no watermark, 4:3 landscape.
```

## Overlay exato

- título: `Hexápode — Paleta Oficial`;
- nomes e códigos hexadecimais da tabela 0.3;
- rótulos: `estrutura`, `máquina`, `fluxo`, `tecido`, `segurança`, `lesão`, `alerta`, `apoio`.

## Alt text

> Prancha do sistema Hexápode com onze cores semânticas e exemplos de aplicação em estrutura editorial, equipamentos, fluxo gasoso, tecidos, segurança, lesão e alerta.

## Reutilização

Todos os projetos, componentes, pranchas, interfaces e documentos.

## Aceite específico

- todos os códigos hexadecimais corretos;
- contraste suficiente entre texto e fundo;
- vermelho e verde nunca usados como única distinção informacional.

---

# 2. HEX-G001-002 — Tipografia

## Missão

Definir a hierarquia tipográfica editorial e técnica do ecossistema.

## Composição

Prancha com seis famílias de uso:

1. título editorial serifado;
2. título de seção;
3. subtítulo;
4. corpo sans-serif;
5. legenda e anotação;
6. dados e rótulos monoespaçados.

Mostrar escalas desktop, tablet e mobile, além de um exemplo de módulo médico completo.

## Prompt canônico

```text
Create a canonical typography specimen board for the Hexápode medical atlas ecosystem. Match a warm ivory scientific editorial system with thin graphite rules, deep blue and teal accents. Show a restrained hierarchy: large editorial serif titles, strong section headings, clean sans-serif body copy, compact captions, annotation text and monospaced labels for clinical data. Include responsive scale examples for desktop, tablet and mobile, plus a miniature medical module specimen. Functional typographic system, precise spacing, excellent readability, no commercial logos, no watermark, 4:3 landscape.
```

## Overlay exato

- `Título editorial`;
- `Título de seção`;
- `Subtítulo`;
- `Texto corpo`;
- `Legenda e anotação`;
- `Dados mono`;
- exemplo de título: `Mecânica Respiratória`;
- exemplo de subtítulo: `Pressão, fluxo e volume como cadeia causal`;
- exemplo mono: `Pplat 24 cmH₂O · PEEP 8 cmH₂O`.

## Alt text

> Prancha tipográfica do Hexápode com hierarquia para títulos, seções, corpo de texto, legendas, anotações e dados clínicos monoespaçados em diferentes tamanhos de tela.

## Reutilização

Toda interface, página didática, legenda, tabela, módulo e material exportado.

## Aceite específico

- nenhuma amostra abaixo do tamanho mínimo definido para leitura móvel;
- alinhamentos e entrelinhas consistentes;
- dados técnicos claramente distintos do texto narrativo.

---

# 3. HEX-G001-003 — Biblioteca de ícones

## Missão

Estabelecer o vocabulário icônico mínimo comum a todo o ecossistema.

## Composição

Grade com 30 ícones-base divididos em cinco grupos:

- órgãos e anatomia;
- fisiologia e sinais;
- dispositivos e procedimentos;
- risco e estado;
- navegação e aprendizagem.

Ícones essenciais: pulmões, alvéolo, coração, cérebro, rim, fígado, estômago, vaso, célula, ECG, pressão, temperatura, gota, seringa, bolsa IV, comprimido, ventilador, tubo, máscara, ultrassom, microscópio, bisturi, escudo, alerta, estabilidade, lesão, pergunta, comparação, sequência e conclusão.

## Prompt canônico

```text
Create a canonical library sheet of thirty reusable medical line icons for the Hexápode atlas ecosystem. Warm ivory background, uniform thin graphite strokes, restrained semantic accents from the Hexápode palette, consistent optical size and corner language. Organize into anatomy, physiology, devices, risk-state and learning-navigation groups. Include lungs, alveolus, heart, brain, kidney, liver, stomach, vessel, cell, ECG, pressure, temperature, blood drop, syringe, IV bag, pill, ventilator, airway tube, mask, ultrasound probe, microscope, scalpel, shield, warning, stable status, injury, question, comparison, sequence and conclusion. Vector-like, precise, simple, no logos, no watermark, 4:3 landscape.
```

## Overlay exato

Rótulos dos cinco grupos e nomes dos ícones.

## Alt text

> Biblioteca do Hexápode com trinta ícones lineares consistentes para anatomia, fisiologia, dispositivos, riscos, estados clínicos e navegação didática.

## Reutilização

Menus, cards, diagramas, perguntas, fluxos, rodapés, tabelas e status.

## Aceite específico

- todos os ícones reconhecíveis em 24 px;
- espessura visual equivalente;
- nenhum ícone depende de cor para ser compreendido.

---

# 4. HEX-G001-004 — Corpo humano masculino

## Missão

Criar uma base anatômica masculina neutra para sobreposições futuras.

## Composição

- vista anterior;
- vista posterior;
- vista lateral simplificada;
- proporção em oito cabeças;
- planos sagital, frontal e transversal;
- marcos anatômicos principais;
- zonas de encaixe para órgãos e dispositivos.

## Prompt canônico

```text
Create a canonical anonymous adult male body reference board for the Hexápode medical atlas ecosystem. Neutral standing posture, front, back and simplified side views, eight-head proportional guide, subtle anatomical landmarks and body-plane guides. Thin precise graphite linework on warm ivory paper, minimal terracotta tissue accents, non-photorealistic, educational, non-erotic, no facial identity, no genital detail, reusable as a base for organ, pathology, device and procedure overlays. Scientific editorial vector style, 4:3 landscape, no logo, no watermark.
```

## Overlay exato

- `Anterior`;
- `Posterior`;
- `Lateral`;
- `Plano sagital`;
- `Plano frontal`;
- `Plano transversal`;
- marcos: cabeça, pescoço, tórax, abdome, pelve, membros superiores e inferiores.

## Alt text

> Referência anatômica masculina neutra em vistas anterior, posterior e lateral, com guias proporcionais, planos corporais e principais regiões anatômicas.

## Reutilização

Trauma, procedimentos, cardiologia, neurologia, ventilação, nefrologia, farmacologia e anatomia.

## Aceite específico

- anatomia proporcional e simétrica;
- postura compatível entre as vistas;
- espaço suficiente para overlays posteriores;
- ausência de feições identificáveis.

---

# 5. HEX-G001-005 — Corpo humano feminino

## Missão

Criar uma base anatômica feminina neutra, equivalente à base masculina e compatível com os mesmos overlays.

## Composição

Mesma arquitetura do ativo masculino, preservando diferenças proporcionais relevantes sem caricatura ou sexualização.

## Prompt canônico

```text
Create a canonical anonymous adult female body reference board for the Hexápode medical atlas ecosystem. Neutral standing posture, front, back and simplified side views, proportional guide, subtle anatomical landmarks and body-plane guides. Thin precise graphite linework on warm ivory paper, minimal terracotta tissue accents, non-photorealistic, educational, non-erotic, no facial identity, no explicit genital or breast detail, reusable as a base for organ, pathology, device and procedure overlays. Scientific editorial vector style, 4:3 landscape, no logo, no watermark.
```

## Overlay exato

Mesmo conjunto do ativo masculino.

## Alt text

> Referência anatômica feminina neutra em vistas anterior, posterior e lateral, com guias proporcionais, planos corporais e principais regiões anatômicas.

## Reutilização

Todos os braços clínicos, especialmente anatomia, obstetrícia futura, cardiologia, trauma, procedimentos e farmacologia.

## Aceite específico

- correspondência posicional com o corpo masculino;
- sem estilização sexualizada;
- proporções adultas plausíveis;
- pronta para sobreposição anatômica.

---

# 6. HEX-G001-006 — Corpo infantil

## Missão

Criar base pediátrica neutra com proporções próprias, sem reduzir a criança a um adulto em miniatura.

## Composição

- vista anterior e posterior;
- referência etária visual de criança escolar;
- proporções corporais pediátricas;
- cabeça relativamente maior;
- tórax, abdome e membros com relações próprias;
- zonas para dispositivos e cálculo por peso.

## Prompt canônico

```text
Create a canonical anonymous pediatric body reference board for the Hexápode medical atlas ecosystem. School-age child proportions, front and back views, neutral posture, proportion guide, larger head-to-body ratio, pediatric thorax, abdomen and limb relationships, subtle anatomical landmarks and overlay zones for devices and clinical diagrams. Thin precise graphite linework on warm ivory paper, non-photorealistic, child-safe, educational, no facial identity, no genital detail, no decorative cartoon style, 4:3 landscape, no logo, no watermark.
```

## Overlay exato

- `Anterior`;
- `Posterior`;
- `Proporção pediátrica`;
- `Cabeça`;
- `Tórax`;
- `Abdome`;
- `Pelve`;
- `Membros`.

## Alt text

> Referência corporal pediátrica neutra em vistas anterior e posterior, com proporções infantis e regiões anatômicas para uso em diagramas clínicos.

## Reutilização

Pediatria, toxicologia, ventilação pediátrica, trauma, farmacologia e procedimentos.

## Aceite específico

- criança não representada como adulto reduzido;
- postura e escala consistentes;
- nenhum elemento de aparência lúdica inadequada ao atlas.

---

# 7. HEX-G001-007 — Grid editorial

## Missão

Definir a arquitetura espacial das pranchas e páginas do Hexápode.

## Composição

Mostrar:

- proporção 4:3;
- margens seguras;
- grade-base de 12 colunas;
- layouts de 2, 3 e 4 colunas;
- storyboard de 5 painéis;
- painel dominante + satélites;
- comparação lado a lado;
- exercício e gabarito;
- comportamento de recorte mobile.

## Prompt canônico

```text
Create a canonical editorial grid-system specification sheet for the Hexápode medical atlas ecosystem. Warm ivory background, thin graphite rules, sand dividers and subtle pale blue column guides. Show a 4:3 page frame, safe margins, twelve-column base grid, two-column, three-column, four-column, five-panel storyboard, dominant-panel layout, comparison layout, quiz layout and mobile crop behavior. Highly functional, exact, spacious, scientific editorial design, no decorative imagery, no logos, no watermark, 4:3 landscape.
```

## Overlay exato

- `Formato canônico 4:3`;
- `Margem segura`;
- `12 colunas`;
- `Calha`;
- `Título`;
- `Conteúdo`;
- `Rodapé`;
- `Painel dominante`;
- `Comparação`;
- `Exercício`;
- `Recorte mobile`.

## Alt text

> Sistema de grid do Hexápode com formato 4:3, margens, doze colunas e modelos para comparação, storyboard, painel dominante, exercício e adaptação móvel.

## Reutilização

Todas as pranchas, páginas, apresentações e exportações.

## Aceite específico

- cada layout deriva da mesma grade-base;
- nenhum painel fica ilegível após redução para celular;
- margens e calhas constantes.

---

# 8. HEX-G001-008 — Sistema de setas

## Missão

Padronizar causalidade, direção, tempo, força, comparação e retroalimentação.

## Composição

Biblioteca dividida em:

- fluxo físico;
- causalidade;
- sequência temporal;
- aumento e redução;
- ação bidirecional;
- feedback;
- transferência entre compartimentos;
- bloqueio e interrupção;
- trajetória anatômica;
- correção e resposta.

## Prompt canônico

```text
Create a canonical arrow and connector system sheet for the Hexápode medical atlas ecosystem. Warm ivory scientific editorial background, thin graphite geometry and restrained semantic accents. Organize straight, curved, dashed, dotted, bidirectional, loop, increase, decrease, transfer, blockade, timeline and feedback arrows by functional meaning. Include tiny medical examples over an alveolus, vessel, ventilator waveform and causal chain. Precise vector-like language, no decorative arrows, no logos, no watermark, 4:3 landscape.
```

## Overlay exato

- `Fluxo`;
- `Causalidade`;
- `Tempo`;
- `Aumento`;
- `Redução`;
- `Troca`;
- `Bloqueio`;
- `Feedback`;
- `Correção`.

## Alt text

> Biblioteca de setas e conectores do Hexápode para representar fluxo, causalidade, tempo, mudança, bloqueio, transferência e retroalimentação.

## Reutilização

Todos os diagramas causais, fisiológicos, farmacológicos e procedimentais.

## Aceite específico

- direção inequívoca;
- mesma semântica em todos os projetos;
- pontilhado e tracejado nunca usados de forma intercambiável sem legenda.

---

# 9. HEX-G001-009 — Sistema de cores aplicado

## Missão

Demonstrar como a paleta deve operar em diagramas reais, e não apenas como amostras isoladas.

## Composição

Oito miniaplicações:

1. máquina e monitor;
2. gás e ventilação;
3. tecido e esforço;
4. sangue e perfusão;
5. lesão;
6. alerta;
7. resposta segura;
8. estrutura neutra.

Incluir combinações permitidas, combinações proibidas e solução para daltonismo.

## Prompt canônico

```text
Create a canonical applied-color semantics board for the Hexápode medical atlas ecosystem. Use the official warm ivory, graphite, petroleum, machine blue, gas-flow teal, tissue terracotta, safe green, injury red, alert amber and sand palette. Demonstrate the colors in eight miniature medical diagrams: machine-monitoring, airflow, tissue effort, perfusion, injury, warning, safe response and neutral structure. Add examples of correct combinations, prohibited combinations and color-blind-safe pattern reinforcement. Scientific, functional, minimal, no logos, no watermark, 4:3 landscape.
```

## Overlay exato

- `Máquina`;
- `Fluxo gasoso`;
- `Tecido e esforço`;
- `Perfusão`;
- `Lesão`;
- `Alerta`;
- `Resposta segura`;
- `Estrutura`;
- `Nunca depender apenas da cor`.

## Alt text

> Prancha do Hexápode demonstrando o uso aplicado das cores semânticas em máquinas, fluxo gasoso, tecidos, perfusão, lesão, alerta e resposta segura.

## Reutilização

Validação de todas as futuras pranchas e interfaces.

## Aceite específico

- exemplos coerentes com a paleta oficial;
- redundância por forma, padrão ou rótulo nos estados críticos;
- nenhuma cor usada apenas por preferência estética.

---

# 10. HEX-G001-010 — Templates

## Missão

Criar os modelos estruturais que receberão conteúdo clínico sem exigir nova composição do zero.

## Composição

Seis templates-base:

1. capa de módulo;
2. storyboard causal de cinco painéis;
3. comparação A × B;
4. mecanismo em camadas;
5. exercício socrático;
6. síntese clínica com decisão.

Adicionar componentes menores: caixa de conceito, alerta, armadilha, referência, conclusão e gabarito.

## Prompt canônico

```text
Create a canonical template library sheet for the Hexápode medical atlas ecosystem. Warm ivory scientific editorial style, thin graphite structure, sand dividers and restrained semantic color accents. Show six reusable miniature page templates: module cover, five-panel causal storyboard, A-versus-B comparison, layered mechanism, Socratic exercise and clinical decision summary. Add compact component templates for concept, warning, cognitive trap, reference, conclusion and answer key. Precise wireframe-plus-style specimens, functional and reusable, no logos, no watermark, 4:3 landscape.
```

## Overlay exato

- `Capa de módulo`;
- `Storyboard causal`;
- `Comparação`;
- `Mecanismo em camadas`;
- `Exercício socrático`;
- `Síntese e decisão`;
- `Conceito`;
- `Alerta`;
- `Armadilha`;
- `Referência`;
- `Conclusão`;
- `Gabarito`.

## Alt text

> Biblioteca de templates do Hexápode para capas, storyboards causais, comparações, mecanismos em camadas, exercícios socráticos e sínteses clínicas.

## Reutilização

Todos os módulos e braços do ecossistema.

## Aceite específico

- cada template possui pergunta, mecanismo e conclusão identificáveis;
- componentes menores encaixam sem alterar a grade;
- templates funcionam com conteúdo curto ou denso.

---

# 11. Ordem de produção e revisão

A ordem de geração deve ser exatamente:

```text
001 Paleta oficial
002 Tipografia
003 Biblioteca de ícones
004 Corpo humano masculino
005 Corpo humano feminino
006 Corpo infantil
007 Grid editorial
008 Sistema de setas
009 Sistema de cores aplicado
010 Templates
```

Após cada ativo:

1. revisar o render integral;
2. registrar erros anatômicos, tipográficos e composicionais;
3. corrigir o prompt;
4. produzir o overlay exato;
5. atualizar metadados;
6. somente então marcar como concluído.

A Geração 002 não deve começar antes de os dez ativos desta geração estarem aprovados como uma família visual coerente.
