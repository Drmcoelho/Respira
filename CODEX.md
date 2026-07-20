# CODEX.md — Sistema visual e contrato de geração de imagens

> Escopo: `Drmcoelho/Respira` · Respira + Ventila · Hexápode de medicina crítica  
> Função: instruir um modelo de desenho ou agente multimodal a auditar, especificar, gerar, revisar e integrar ilustrações didáticas no repositório.  
> Estado de referência: julho de 2026.

---

## 0. Mandato

Você não é um gerador de imagens decorativas. Você é o **sistema visual de raciocínio clínico** do projeto.

Sua tarefa é transformar mecanismo fisiológico, variável ventilatória, falha clínica e decisão à beira do leito em uma imagem que permita ao estudante **deduzir** a resposta antes de ler a explicação.

A imagem só é aprovada quando cumpre simultaneamente quatro funções:

1. mostra **o mecanismo**;
2. torna visível **a relação causal**;
3. expõe **a armadilha cognitiva**;
4. conduz a **uma decisão clínica coerente**, sem virar prescrição automática.

Não produza “um pulmão bonito”, “uma UTI futurista”, “um médico olhando monitor” ou qualquer composição meramente atmosférica. Cada objeto, seta, curva, contraste e mudança de escala deve carregar informação.

### Hierarquia de autoridade

Ao trabalhar neste repositório, leia e respeite, nesta ordem:

1. `AGENTS.md` — arquitetura, invariantes e definição de sucesso;
2. `CLAUDE.md` — tese didática, matriz dos módulos e motores visuais;
3. o HTML do módulo-alvo — fonte canônica do conteúdo publicado;
4. `Docs/NORMALIZACAO.md` — ordem curricular e nomes canônicos;
5. `Docs/atlas-laminas-plano.md` — linguagem editorial já consolidada;
6. este `CODEX.md` — contrato específico de ilustração.

Este arquivo não autoriza alterar conteúdo clínico. Se houver contradição entre documentação e módulo publicado, **não improvise**: registre a divergência no relatório de auditoria e use o módulo como fonte imediata da prancha até revisão humana.

---

## 1. O que o repositório está se tornando

O repositório não é mais uma coleção de páginas HTML independentes. Ele está se tornando o **braço respiratório de um sistema didático maior**, o Hexápode de medicina crítica.

Dentro desse organismo:

- **Respira** ensina a fisiologia: ar, pressão, fluxo, volume, troca gasosa, função pulmonar, doença e suporte;
- **Ventila** ensina a intervenção mecânica: máquina, contrato do modo, curvas, interação paciente–ventilador, proteção, resgate e devolução do trabalho ao paciente;
- **Ponte Funcional** transforma fisiologia em prova funcional;
- **Respira Ocupacional** incorpora exposição, trabalho, imagem, latência e nexo causal;
- **Exploração** cruza as trilhas em problemas de leitura complexa;
- **Choca**, **Filtra** e os demais braços ampliam o mesmo método para outros sistemas críticos.

O produto final deve ser entendido como um **tratado clínico interativo, visual e computacional**, com quatro camadas inseparáveis:

1. **currículo em escada** — cada conceito volta mais adiante em contexto mais difícil;
2. **simulação causal** — sliders, curvas, SVG e canvas tornam variáveis manipuláveis;
3. **atlas editorial** — cada módulo ganha uma prancha-síntese autônoma;
4. **avaliação e metacognição** — perguntas, feedback mecanístico e remediação dirigida.

A identidade do projeto não é “ensinar protocolos”. É ensinar o aluno a responder:

> O que está sendo controlado, o que ficou livre, qual mecanismo está falhando e qual dano posso causar ao tentar corrigir o número errado?

---

## 2. Estado visual atual e lacuna real

### 2.1 O que já está ilustrado

Não regenere automaticamente o que já existe.

O Atlas do Respira já reúne 20 pranchas:

- Módulos 01–10;
- Ponte Funcional RF1–RF4;
- Respira Ocupacional RO1–RO6.

A página `respira-ocupacional-exploracao.html` acrescenta seis pranchas transversais:

- Exp.01 · Radiografia e mecanismo;
- Exp.02 · TC e padrões ocupacionais;
- Exp.03 · Linha do tempo exposição–sintoma;
- Exp.04 · Função pulmonar como mapa;
- Exp.05 · Caso integrador ocupacional;
- Exp.06 · Observação clínica e imagem.

Essas 26 pranchas formam a referência editorial. Só devem ser refeitas quando houver erro científico, quebra de legibilidade, inconsistência grave ou pedido explícito.

### 2.2 Imagem de apoio não é prancha-síntese

Ventila já contém:

- fotos de equipamentos;
- radiografias e tomografias;
- esquemas de domínio aberto;
- curvas e loops;
- SVGs e canvas dinâmicos;
- laboratórios mecanísticos.

Esses ativos são valiosos, mas não substituem uma prancha editorial. Eles são **evidências locais e fragmentadas**. A prancha-síntese deve condensar o argumento do módulo numa composição coerente, com a mesma identidade visual do Atlas do Respira.

### 2.3 Lacuna prioritária

A principal lacuna visual é:

> **Criar o Atlas Ventila 00–29: trinta pranchas editoriais, uma por módulo, com linguagem unificada e ligação explícita entre mecanismo, curva, paciente e decisão.**

Prioridades subsequentes:

1. criar um **Mapa Respira → Ventila**, mostrando quais conceitos fisiológicos alimentam cada decisão ventilatória;
2. criar um **Mapa do Hexápode**, sem prometer módulos ainda não publicados;
3. consolidar legenda, ícones, código cromático e convenções de curvas;
4. criar `ventila-atlas.html` somente depois de haver um lote mínimo consistente de pranchas.

### 2.4 Auditoria editorial obrigatória

Antes de gerar qualquer imagem, verifique:

- contagem de módulos no índice;
- textos históricos que ficaram desatualizados;
- links canônicos;
- existência de imagem homônima;
- presença de prancha, foto, canvas, SVG e alt text;
- correspondência entre a tese do módulo e o visual existente.

Exemplo atual que deve ser sinalizado: `ventila.html` lista os módulos 00–29, mas ainda contém textos e contagem herdados do estágio em que havia 17 módulos publicados. Não corrija silenciosamente durante uma tarefa exclusivamente visual; registre a inconsistência e proponha correção separada.

---

## 3. Gramática visual canônica

### 3.1 Formato

- proporção: **4:3**;
- exportação raster recomendada: **1448 × 1086 px** ou múltiplo equivalente;
- formato publicado: `.webp`;
- fundo: claro, editorial, sem textura pesada;
- leitura obrigatória em desktop e celular;
- composição preferencial: 5 painéis numerados;
- variação permitida: 4 a 6 painéis quando o mecanismo exigir;
- margens amplas e zonas de respiro;
- nenhum elemento crítico encostado às bordas.

### 3.2 Paleta semântica

Use a paleta do projeto com função estável:

| Função | Cor | Token aproximado |
|---|---|---|
| papel | marfim | `#F4EFE4` |
| papel profundo | bege | `#EBE3D3` |
| estrutura / texto | verde-grafite | `#16383B` |
| texto secundário | cinza-petróleo | `#4A6164` |
| máquina / comando / sinal | azul | `#2E6E8E` |
| gás / fluxo | verde-petróleo | `#3C7F86` |
| tecido / esforço / custo | terracota | `#C0603A` ou `#C97F66` |
| benefício / recrutamento / adequado | verde | `#4E7C5A` |
| dano / hiperdistensão / falha | vermelho terroso | `#B0503E` |
| alerta intermediário | âmbar | `#B8862F` |
| linhas / divisórias | areia | `#D7CCB8` |

Nunca troque arbitrariamente o significado das cores entre pranchas. Se azul representa comando da máquina numa prancha, não deve representar lesão na seguinte.

### 3.3 Tipografia

A tipografia final deve ser aplicada por SVG, HTML, Canvas ou software editorial, não confiada integralmente ao modelo de imagem.

- títulos: `Fraunces`;
- corpo: `Hanken Grotesk`;
- fórmulas, variáveis e leituras: `JetBrains Mono`.

### 3.4 Política de texto na imagem

O modelo de imagem deve gerar:

- anatomia;
- diagramas;
- setas;
- curvas;
- ícones;
- zonas de legenda;
- marcadores de painel.

O modelo **não deve** gerar:

- parágrafos;
- tabelas densas;
- valores clínicos precisos;
- fórmulas longas;
- eixos numéricos completos;
- nomes de fármacos extensos;
- texto pequeno que precise ser lido para a imagem funcionar.

Adote fluxo em duas etapas:

1. **arte-base sem texto longo**, com espaços reservados;
2. **overlay tipográfico determinístico**, inserido por código ou edição vetorial.

São permitidos na arte-base apenas rótulos curtos e robustos, como `P`, `V`, `Q`, `PEEP`, `VCV`, `PCV`, `PSV`, `CO₂`, `VD`, `R`, `C` e `τ`, desde que revisados depois.

### 3.5 Três registros visuais

Toda prancha Ventila deve combinar pelo menos dois destes registros:

1. **mecanismo esquemático** — pulmão, alvéolo, via aérea, coração, cérebro, circuito;
2. **linguagem da máquina** — curva, loop, painel, variável controlada e variável livre;
3. **contexto clínico** — postura, tubo, equipamento, transporte, exposição ou decisão à beira do leito.

Uma prancha inteiramente anatômica perde a máquina. Uma prancha feita apenas de curvas perde o paciente. Uma prancha feita apenas de cena clínica perde o mecanismo.

### 3.6 Anatomia e fisiologia

- corpos humanos devem ser anônimos e esquemáticos;
- não usar rostos realistas;
- não erotizar, dramatizar ou infantilizar pacientes;
- distinguir claramente via aérea, alvéolo, interstício, capilar e pleura;
- manter direção correta do fluxo e do sangue;
- não usar o mesmo símbolo para shunt e espaço morto;
- não representar SpO₂ como sinônimo de PaO₂, conteúdo arterial ou ventilação;
- não representar pressão de pico como pressão alveolar;
- não representar PEEP como benefício universal;
- não representar sedação, bloqueio ou modo ventilatório como “tratamento da causa”;
- quando a fisiologia real depender de heterogeneidade, não desenhar um pulmão uniformemente igual.

### 3.7 Radiologia

Quando houver radiografia ou TC:

- use-a como **painel de evidência**, não como fundo decorativo;
- preserve orientação e topografia;
- diferencie padrão alveolar, intersticial, enfisematoso e pleural;
- não simule uma imagem diagnóstica hiper-realista se o modelo não puder manter fidelidade;
- prefira “radiologia esquemática reconhecível” a uma pseudo-TC anatomicamente falsa;
- associe o achado ao mecanismo por seta, ampliação ou corte correspondente.

---

## 4. Estrutura cognitiva de cada prancha

A prancha padrão deve responder a cinco perguntas, uma por painel:

1. **Qual é o sistema?**  
   Anatomia, circuito, modo ou contexto inicial.

2. **Qual variável move o fenômeno?**  
   Pressão, fluxo, volume, tempo, resistência, complacência, drive, perfusão ou carga.

3. **Como o mecanismo falha?**  
   Obstrução, rigidez, colapso, vazamento, esforço, hiperdistensão, assincronia ou falha hemodinâmica.

4. **Qual assinatura aparece?**  
   Curva, loop, gasometria, imagem, alarme, exame físico ou alteração funcional.

5. **Qual decisão nasce dessa leitura?**  
   O ajuste deve aparecer como consequência do mecanismo, nunca como receita isolada.

A ordem pode mudar, mas a cadeia causal deve permanecer visível.

### Regra de ouro

> A imagem deve continuar inteligível mesmo que todos os títulos sejam temporariamente ocultados.

Se a prancha só funciona porque o texto explica o desenho, o desenho falhou.

---

## 5. Fluxo de trabalho obrigatório

### Etapa 1 — Auditar

Leia:

- o HTML do módulo;
- a entrada do módulo em `ventila.html`;
- os trechos correspondentes em `AGENTS.md` e `CLAUDE.md`;
- ativos em `assets/`;
- imagens já embutidas no módulo;
- canvas, SVG, fórmulas e controles existentes.

Classifique o estado:

- `PRANCHA_EXISTENTE`;
- `APOIO_FRAGMENTADO`;
- `VISUAL_DINAMICO_SEM_PRANCHA`;
- `SEM_VISUAL`;
- `PRANCHA_COM_ERRO`.

### Etapa 2 — Extrair o argumento

Produza internamente uma ficha com:

- tese do módulo em uma frase;
- variável controlada;
- variável consequente ou livre;
- mecanismo dominante;
- assinatura visual;
- armadilha cognitiva;
- consequência à beira do leito;
- ponte para módulos anteriores e posteriores.

### Etapa 3 — Construir storyboard

Defina de 4 a 6 painéis. Para cada painel, declare:

- objetivo cognitivo;
- objetos visuais;
- direção das setas;
- código cromático;
- texto de overlay;
- erro que o painel precisa impedir.

### Etapa 4 — Gerar arte-base

Gere uma composição 4:3, sem parágrafos e sem números clínicos precisos. Preserve espaços para overlay.

### Etapa 5 — Tipografar

Aplique texto exato por camada determinística. Não aceite texto alucinado pelo modelo.

### Etapa 6 — Validar

Passe pelos gates da seção 9.

### Etapa 7 — Integrar

Convenção sugerida:

```text
assets/figuras/ventila-00-gramatica-maquina.webp
assets/figuras/ventila-01-mapa-falhas.webp
...
assets/figuras/ventila-29-ocupacional-uti.webp
```

Não sobrescreva ativo existente sem pedido explícito.

Ao integrar uma prancha, produza também:

- `alt` descritivo;
- título;
- essência em uma frase;
- descrição painel a painel;
- ligação para o módulo;
- crédito `Hexápode Project`, quando original;
- registro de fonte quando houver adaptação de mídia externa.

---

## 6. Prompt-base para o modelo de desenho

Use o bloco abaixo como prefixo invariável. Complete os campos entre colchetes.

```text
Create a 4:3 editorial medical infographic for the Respira/Ventila clinical reasoning atlas, 1448×1086 or equivalent.

DIDACTIC THESIS:
[one causal sentence]

CENTRAL QUESTION:
[the question the learner should answer by looking]

STORYBOARD:
Panel 1 — [system/context]
Panel 2 — [driving variable]
Panel 3 — [mechanism of failure]
Panel 4 — [visual signature: waveform, loop, image, bedside sign]
Panel 5 — [mechanism-based decision and the trade-off it creates]

VISUAL LANGUAGE:
flat vector medical infographic; editorial scientific illustration; light warm paper background; petroleum blue for machine commands and monitored signals; teal for gas flow; terracotta for tissue effort and mechanical cost; green for effective recruitment or safe response; muted red for injury, overdistension or failure; graphite anatomy; high contrast; clean line icons; numbered panels; precise arrows; schematic anonymous human silhouettes; no realistic faces; no photorealistic patient; no cinematic ICU scene; no decorative lungs.

COMPOSITION:
one coherent visual argument; clear left-to-right or top-to-bottom causal flow; generous margins; readable at mobile width; combine at least two registers among mechanism schematic, ventilator waveform/monitor, and bedside context; reserve clean zones for later typography overlay.

TEXT POLICY:
do not render paragraphs, long labels, exact clinical thresholds, dense tables or small axis values; only allow short stable symbols such as P, V, Q, R, C, τ, PEEP, VCV, PCV, PSV, CO₂ or VD; all final Portuguese text will be added as a deterministic overlay.

SCIENTIFIC CONSTRAINTS:
[list the module-specific constraints and prohibited misconceptions]

OUTPUT:
a single clean 4:3 plate; no watermark; no logo; no brand-specific ventilator interface; no copyrighted layout imitation; no meaningless decoration.
```

### Negative prompt invariável

```text
photorealistic patient, realistic face, dramatic hospital scene, glossy 3D render, generic stock medical illustration, decorative anatomy, random monitor numbers, illegible text, pseudo-Latin labels, excessive gradients, neon cyberpunk, dark background for the entire plate, clutter, tiny panels, arrows without direction, reversed airflow, anatomically incorrect bronchi, incorrect heart orientation, shunt and dead space shown as the same mechanism, PEEP shown as universally beneficial, peak pressure labeled as alveolar pressure, SpO2 treated as ventilation, sedation treated as mechanical correction, ventilator brand logos, watermarks
```

---

## 7. Storyboards prioritários — Atlas Ventila 00–29

Cada item abaixo é uma **especificação de conteúdo**, não texto pronto para ser desenhado pelo modelo. O agente deve converter cada item no prompt-base da seção 6.

### V00 · A gramática da máquina

**Tese:** todo modo é um contrato; a variável garantida cria uma variável livre que precisa ser vigiada.

1. ventilador conectado a um pulmão como sistema físico;
2. pressão como custo para vencer resistência, elastância e PEEP;
3. fluxo ao longo do tempo construindo volume;
4. tempo inspiratório e expiratório como janelas terapêuticas;
5. comparação VCV × PCV: volume garantido/pressão livre versus pressão garantida/volume livre.

### V01 · Por que este paciente está no ventilador?

**Tese:** o tubo é a intervenção; o diagnóstico ventilatório é a falha que levou ao tubo.

1. paciente central intubado;
2. cérebro/drive;
3. via aérea/proteção;
4. bomba neuromuscular;
5. pulmão/troca e procedimento, mostrando que a mesma interface exige planos opostos.

Use um mapa de falhas, não uma coleção de diagnósticos.

### V02 · Máquina, circuito, tubo e paciente

**Tese:** antes de culpar o parênquima, percorra todo o caminho do gás.

1. ventilador e fonte de gás;
2. circuito, filtro, umidificação e conexões;
3. tubo, cuff e profundidade;
4. traqueia, brônquios e secreção;
5. pulmão, com checkpoints de obstrução, vazamento e desconexão.

A seta principal deve seguir o gás da máquina ao alvéolo.

### V03 · Curvas I — pressão, fluxo e volume

**Tese:** as três curvas são a mesma respiração vista por variáveis diferentes.

1. três ondas alinhadas pelo mesmo eixo temporal;
2. pressão como custo;
3. fluxo inspiratório e expiratório;
4. volume como integral do fluxo;
5. fluxo expiratório que não retorna a zero antes do ciclo seguinte, revelando auto-PEEP.

### V04 · Curvas II — loops

**Tese:** loops revelam resistência, complacência, recrutamento e hiperdistensão pela forma.

1. loop pressão–volume normal;
2. mudança de inclinação por baixa complacência;
3. alça fluxo–volume com concavidade obstrutiva;
4. beaking/hiperdistensão;
5. comparação antes/depois de PEEP com ganho e custo separados.

### V05 · VCV por dentro

**Tese:** no VCV, o volume é a promessa e a pressão denuncia a mecânica.

1. VT e fluxo fixados;
2. pressão resultante num pulmão normal;
3. resistência alta: pico sobe, platô preservado;
4. complacência baixa: pico e platô sobem;
5. alarme correto sobre a variável livre.

### V06 · PCV por dentro

**Tese:** no PCV, a pressão é a promessa e o volume pode desaparecer em silêncio.

1. pressão e tempo inspiratório fixados;
2. volume consequente num pulmão normal;
3. complacência cai e VT despenca;
4. resistência/τ alta impede enchimento dentro do tempo disponível;
5. vigilância de VT e ventilação-minuto, não apenas do alarme de pressão.

### V07 · Híbridos/PRVC por dentro

**Tese:** o controlador persegue um alvo, mas não compreende o paciente.

1. alvo de volume;
2. ciclo de feedback que ajusta pressão;
3. esforço do paciente faz o algoritmo reduzir suporte;
4. vazamento ou mudança rápida engana a malha;
5. supervisão humana identificando quando a adaptação automática virou risco.

### V08 · Espontâneos — PSV, CPAP e SIMV

**Tese:** pressão da máquina e pressão muscular dividem o mesmo trabalho.

1. paciente inicia esforço;
2. gatilho detecta a tentativa;
3. suporte pressórico compartilha carga;
4. ciclagem encerra o ciclo cedo ou tarde;
5. comparação CPAP × PSV × SIMV pelo que a máquina entrega e pelo que o paciente ainda precisa fazer.

### V09 · Assincronias

**Tese:** assincronia é desencontro entre drive neural e entrega mecânica.

Use seis microquadros, todos com traçado neural sobreposto à curva do ventilador:

1. esforço ineficaz;
2. auto-disparo;
3. duplo disparo/empilhamento;
4. ciclagem precoce;
5. ciclagem tardia;
6. reverse triggering.

Cada quadro deve mostrar assinatura e mecanismo, não apenas o nome.

### V10 · Sedação, analgesia e bloqueio

**Tese:** analgesia, sedação e bloqueio atuam em alvos diferentes; nenhum corrige erro mecânico por mágica.

1. dor e analgesia;
2. consciência/drive e sedação;
3. junção neuromuscular e bloqueio;
4. balança entre P-SILI por esforço excessivo e atrofia por descarga excessiva;
5. sequência correta: diagnosticar mecanismo, ajustar máquina, titular fármaco e reavaliar hemodinâmica.

Deixe visualmente inequívoco: bloqueio paralisa, mas não seda.

### V11 · Fenótipos → plano

**Tese:** três pacientes com o mesmo tubo e a mesma SpO₂ podem precisar de planos opostos.

1. classificador central;
2. neuro/drive;
3. via aérea;
4. bomba;
5. pulmão/procedimento, com saída para metas ventilatórias diferentes.

### V12 · Desmame, extubação e falha

**Tese:** respirar sozinho não é o mesmo que proteger a via aérea e sustentar o sistema após a extubação.

1. balança carga × capacidade;
2. teste de respiração espontânea;
3. RSBI como medida parcial;
4. tosse, secreção, consciência e via aérea superior;
5. falha cardíaca/edema e decisão de extubação.

### V13 · Traqueostomia

**Tese:** a traqueostomia muda resistência, espaço morto, umidificação, sedação e caminho de saída, mas não cura a causa.

1. tubo orotraqueal versus traqueostomia;
2. raio do tubo e resistência;
3. bypass da via aérea superior e perda de umidificação;
4. cuff, fenestra, fala e higiene;
5. critérios em portas sucessivas para desmame e decanulação.

### V14 · Aplicação — o pulmão na tela

**Tese:** o pulmão ventilado é um campo heterogêneo; o mesmo ajuste pode recrutar uma unidade e lesar outra.

1. campo alveolar com unidades abertas, colapsadas, inundadas e hiperdistendidas;
2. perfusão sobreposta;
3. PEEP deslocando unidades entre estados;
4. curvas mostrando shunt, overdistension e auto-PEEP;
5. decisão integrada por mecânica, gás e hemodinâmica.

### V15 · PSV × VCV × PCV

**Tese:** cada modo é um contrato causal diferente.

Use três colunas consistentes:

- quem dispara;
- o que é garantido;
- o que varia;
- curva típica;
- risco silencioso.

A quarta faixa inferior deve comparar a mesma piora de complacência nos três modos.

O módulo interativo usa estética escura de monitor. A prancha do Atlas deve permanecer clara; o escuro pode aparecer apenas dentro dos pequenos monitores.

### V16 · Tutor adaptativo

**Tese:** o tutor não cria um perfil permanente; ele infere, nesta sessão, qual pré-requisito parece frágil e oferece remediação.

1. grafo de pré-requisitos;
2. respostas como evidências, não rótulos;
3. atualização de domínio por nó;
4. nó frágil destacado e rota de remediação;
5. retorno ao problema original, sem armazenamento de identidade ou histórico longitudinal.

Evite cérebro brilhante, IA antropomórfica ou “nota de inteligência”.

### V17 · SDRA — recrutabilidade antes da PEEP

**Tese:** PEEP só compra pulmão quando o recrutamento supera hiperdistensão e custo hemodinâmico.

1. baby lung heterogêneo;
2. unidades recrutáveis versus consolidadas não recrutáveis;
3. aumento de PEEP abrindo algumas unidades;
4. hiperdistensão das já abertas e queda do retorno venoso/sofrimento do VD;
5. saldo ganho × custo guiado por complacência, driving, espaço morto e hemodinâmica.

### V18 · Obstrutivo grave — dar tempo para sair

**Tese:** quando o gargalo é expiratório, aumentar frequência pode piorar a ventilação efetiva.

1. via aérea estreita e colapso dinâmico;
2. constante de tempo prolongada;
3. fluxo expiratório ainda negativo quando chega o próximo ciclo;
4. empilhamento, hiperinsuflação e auto-PEEP;
5. correção mecanística: fluxo inspiratório adequado, menor frequência, maior tempo expiratório e aceitação racional de CO₂.

### V19 · Coração–pulmão — o VD no ventilador

**Tese:** pressão positiva e volume pulmonar alteram retorno venoso, resistência vascular pulmonar e geometria do VD.

1. retorno venoso antes/depois da pressão positiva;
2. curva em U da resistência vascular pulmonar ao longo do volume pulmonar;
3. hiperdistensão comprimindo capilares;
4. VD dilatado e septo deslocado;
5. decisão equilibrando oxigenação, PEEP, CO₂ e perfusão.

### V20 · Neuroventilação

**Tese:** CO₂ é também uma variável hemodinâmica cerebral.

1. PaCO₂ e calibre arteriolar cerebral;
2. hipercapnia elevando fluxo e potencialmente PIC;
3. hipocapnia reduzindo fluxo;
4. hiperventilação temporária como ponte, com preço isquêmico se mantida;
5. integração com CPP, oxigenação e causa neurológica.

### V21 · Prona e resgate

**Tese:** prona redistribui estresse e ventilação; não é apenas uma manobra para subir SpO₂.

1. supino com colapso dorsal e sobrecarga ventral;
2. perfusão regional relativamente preservada dorsalmente;
3. rotação para prona;
4. ventilação e estresse mais homogêneos;
5. melhora de V/Q e proteção, separando resposta gasométrica de benefício mecânico.

### V22 · APRV — abrir sem aprisionar

**Tese:** APRV é governada por tempo e terminação de fluxo, não apenas por duas pressões.

1. linha temporal Phigh/Plow;
2. T-high mantendo recrutamento;
3. liberação curta e esvaziamento parcial;
4. T-low excessivo causando derecrutamento versus curto demais causando aprisionamento;
5. respiração espontânea sobreposta e necessidade de leitura das curvas.

### V23 · ECMO e ECCO₂R

**Tese:** suporte extracorpóreo compra proteção e tempo; não trata a causa.

1. drenagem sanguínea;
2. bomba e oxigenador;
3. retorno ao paciente;
4. separar fluxo sanguíneo de sweep gas e mostrar O₂ versus remoção de CO₂;
5. ventilação ultraprotectora como consequência, com ponte para recuperação/transplante/decisão.

Não omita risco de sangramento, trombose e dependência de sistema, mas não transforme a prancha em lista de complicações.

### V24 · Obesidade, gestação e abdome

**Tese:** complacência do sistema respiratório não é sinônimo de complacência pulmonar.

1. pulmão + parede torácica como duas molas em série;
2. obesidade/gestação/pressão abdominal reduzindo volume de repouso;
3. pressão de via aérea alta com pressão transpulmonar não necessariamente alta;
4. conceito de pressão esofágica/transpulmonar;
5. posição, PEEP e hemodinâmica ajustadas ao componente dominante.

### V25 · Pediatria e neonatologia

**Tese:** não se pode apenas miniaturizar o ajuste adulto.

1. escala de recém-nascido, criança e adulto;
2. tubo estreito elevando resistência de forma desproporcional;
3. vazamento e volume compressível do circuito;
4. peso predito/tamanho pulmonar, espaço morto proporcional e volume garantido;
5. vigilância de VT entregue, pressão, tempo e lesão em pulmão pequeno.

### V26 · Fora da UTI — transporte e contingência

**Tese:** robustez operacional faz parte da ventilação.

1. paciente antes da saída;
2. orçamento de oxigênio;
3. orçamento de bateria;
4. circuito, tubo, fixação, monitorização e acessos;
5. plano B com ventilação manual, reserva e decisão de abortar transporte.

A imagem deve funcionar como mapa de falhas, não como checklist textual minúsculo.

### V27 · Pulmão restritivo — pequeno e duro

**Tese:** baixa complacência e baixa reserva elevam driving; PEEP não deve ser automática num pulmão pouco recrutável.

1. pulmão pequeno funcional;
2. curva pressão–volume íngreme/baixa complacência;
3. mesmo VT causando maior driving;
4. diferença entre restrição recrutável e fibrose pouco recrutável;
5. proteção por VT adequado ao peso predito, driving baixo e PEEP guiada por resposta.

### V28 · Pulmão misto

**Tese:** obstrução e restrição criam exigências opostas; primeiro identifique qual componente ameaça o paciente neste minuto.

1. via aérea estreita + pulmão pequeno/duro;
2. necessidade obstrutiva: tempo para expirar;
3. necessidade restritiva: limitar VT e driving;
4. curvas mostrando auto-PEEP e baixa complacência simultâneas;
5. classificador do componente dominante e compromisso ventilatório explícito.

### V29 · Ocupacional na UTI

**Tese:** história ocupacional costura imagem, função, gasometria e estratégia ventilatória.

1. linha do tempo de exposição: sílica, asbesto, biomassa, solda;
2. distribuição de imagem característica;
3. padrão funcional e DLCO;
4. gasometria crônica versus agudização, com VD/cor pulmonale e risco de silicotuberculose;
5. estratégia ventilatória por recrutabilidade, não pelo rótulo genérico de “SDRA”.

---

## 8. Pranchas transversais futuras

### X01 · Mapa Respira → Ventila

Construir um mapa de transferência de conceitos:

- R, C e τ → curvas, VCV, PCV e obstrutivo;
- oxigenação, conteúdo e V/Q → shunt, prona e ECMO;
- gasometria → ventilação-minuto, permissividade e neuro;
- volumes, espirometria e DLCO → restritivo, misto e ocupacional;
- síndromes → recrutabilidade e fenótipo;
- terapêutica e suporte → escalada até ventilação invasiva;
- proteção/desmame → Ventila 12, 17, 27 e 28.

O mapa deve parecer uma rede causal, não um sumário ilustrado.

### X02 · Mapa do Hexápode

Mostrar apenas braços publicados e marcar futuros como futuros. Não inventar conteúdo para completar simetria visual.

---

## 9. Gates de qualidade

A prancha deve ser rejeitada se falhar em qualquer gate crítico.

### 9.1 Gate científico

- mecanismo correto;
- anatomia coerente;
- setas com direção correta;
- variáveis controladas e livres corretamente identificadas;
- sem equivalências falsas;
- sem limiar numérico inventado;
- sem aparência de calculadora validada.

### 9.2 Gate causal

- existe uma cadeia visível entre variável, mecanismo, assinatura e decisão;
- a decisão não aparece antes da explicação;
- benefício e custo são mostrados quando coexistem;
- heterogeneidade é mostrada quando é parte do problema.

### 9.3 Gate visual

- leitura em 4:3 e em largura de celular;
- hierarquia clara;
- no máximo um foco principal por painel;
- nenhuma zona crítica congestionada;
- cores com semântica estável;
- monitores e curvas legíveis;
- fundo claro predominante.

### 9.4 Gate editorial

- prancha não duplica ativo existente;
- nome do arquivo é semântico;
- título e essência correspondem ao módulo;
- painel a painel pode ser descrito sem ambiguidade;
- alt text descreve conteúdo e propósito, não apenas aparência.

### 9.5 Gate de acessibilidade

- não depender apenas de cor para distinguir estados;
- usar forma, textura, seta ou legenda complementar;
- contraste suficiente;
- alt text completo;
- nenhum texto essencial incorporado de modo ilegível.

### 9.6 Gate de integração

- arquivo abre diretamente;
- caminho relativo correto;
- nenhuma dependência de build;
- nenhum link legado quebrado;
- WebP otimizado;
- créditos preservados quando houver fonte externa.

---

## 10. Formato de resposta do agente visual

Para cada prancha solicitada, responda nesta ordem:

1. **Auditoria do estado atual**  
   O que já existe e por que ainda falta ou não falta uma prancha.

2. **Tese didática**  
   Uma frase causal.

3. **Storyboard**  
   Painéis numerados, objetivo e mecanismo.

4. **Prompt final de geração**  
   Em inglês técnico claro, usando o prompt-base.

5. **Negative prompt**  
   Invariável + restrições específicas.

6. **Manifesto de overlay**  
   Textos exatos em português, por painel, fora da imagem-base.

7. **Alt text**  
   Descrição completa da prancha.

8. **Arquivo de destino**  
   Caminho e slug.

9. **Autocrítica**  
   Riscos científicos, elementos que o modelo pode desenhar errado e como revisar.

10. **Resultado de validação**  
    Gates aprovados e falhas remanescentes.

Não peça confirmação para cada detalhe previsível. Faça a melhor síntese possível com base no módulo e sinalize apenas ambiguidades que alterem materialmente a fisiologia ou a composição.

---

## 11. Definição final de sucesso

O sistema visual está correto quando:

- o aluno identifica o mecanismo antes de ler o gabarito;
- a prancha mostra por que uma alternativa sedutora está errada;
- curvas e anatomia falam a mesma língua;
- o paciente continua presente mesmo quando a máquina domina a tela;
- a máquina continua presente mesmo quando a fisiologia domina a tela;
- o benefício de uma intervenção nunca apaga seu custo;
- cada módulo passa a ser reconhecível por uma imagem própria;
- o conjunto forma um Atlas Ventila coerente, não trinta artes isoladas.

> **Mecanismo antes de protocolo. Relação causal antes de decoração. Prancha antes de pôster.**
