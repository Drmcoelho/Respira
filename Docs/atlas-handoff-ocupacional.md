# Handoff — completar o Atlas com o bloco Ocupacional (RO2–RO6)

> Documento de passagem para outra sessão (mesmo modelo, Claude). Objetivo único: **inserir as pranchas RO2 a RO6 no `atlas.html`**, no mesmo formato das demais, e dar push. Todo o resto do Atlas já está pronto e publicado.

Data: 2026-07-04 · Branch de trabalho: `claude/beautiful-cray-gZWCC`

---

## 1. Estado atual (o que JÁ está feito)

O `atlas.html` já cobre **15 pranchas**, cada uma com imagem WebP, detalhamento por painel e quiz de 4 questões, na ordem curricular:

```
01–05  (Respira fundamentos)      ← já existiam
RF1 RF2 RF3 RF4                    ← Ponte Funcional (feito)
RO1                                ← Ocupacional (feito)
06 07 08 09 10                     ← Respira main (feito)
```

Commits relevantes já **no remoto** (`origin/claude/beautiful-cray-gZWCC`):
- `76abfa7` — Atlas: módulos 06–10
- `dd311e4` — Atlas: RF1–4 + RO1
- (docs) `334b2d4` — organização da pasta `Docs/`

O `index.html` já lista todos os módulos (Respira 01–10, RF1–4, RO1–6, Ventila 00–29). A meta do Atlas já foi corrigida (não diz mais "módulos 1 a 5"; diz "série Respira").

## 2. O que FALTA (a tarefa)

Inserir no `atlas.html` **5 pranchas** do bloco Ocupacional: **RO2, RO3, RO4, RO5, RO6**.

Posição no array `FIGURAS` e no menu `.jump`: **logo depois de `ocupacional-1` (RO1) e antes de `modulo-6`** (para manter a ordem 05 → Ponte → Ocupacional → 06).

### Imagens
As pranchas são enviadas pelo usuário como PNG (~3 MB, 1536×1024). Converter para WebP com `sharp` (qualidade 82) para `assets/figuras/`:

| Prancha | Arquivo WebP alvo | Status nesta sessão |
|---|---|---|
| RO2 · Poeiras minerais | `assets/figuras/respira-ocupacional-02.webp` | **já convertida** (pode estar no working tree; reconverter se sumiu) |
| RO3 · Pulmão rural e biomassa | `assets/figuras/respira-ocupacional-03.webp` | **já convertida** |
| RO4 · Solda, tinta e asma ocupacional | `assets/figuras/respira-ocupacional-04.webp` | **já convertida** |
| RO5 · Silicose do jateamento | `assets/figuras/respira-ocupacional-05.webp` | **falta** — imagem não pôde ser aberta |
| RO6 · DPOC da biomassa | `assets/figuras/respira-ocupacional-06.webp` | **falta** |

> ⚠️ **RO5 vs RO6 não confirmados visualmente.** A API de visão rejeitou repetidamente esses 2 uploads (mesmo reduzidos). O usuário precisa **reenviar RO5 e RO6**; confirme qual é qual antes de nomear o WebP: **RO5** tem plano *dose × tempo* / silicose do jateamento; **RO6** tem comparador de *fenótipo (via aérea × enfisema)* da DPOC da biomassa. (Contorno que funcionou para abrir as imagens: reduzir com `sharp(...).resize(760).jpeg({quality:52})` para ~60 KB e dar `Read` no JPEG. Mesmo assim algumas foram rejeitadas — tentar de novo, pode ser intermitente.)

## 3. Receita de integração (exata)

O `atlas.html` tem, no `<script>`, `const FIGURAS=[ ... ];` — um array de objetos. Cada objeto:

```js
{
  id:'ocupacional-2', mod:'Ocupacional · RO-02', titulo:'...', href:'respira-ocupacional-02-poeiras-minerais.html',
  img:'assets/figuras/respira-ocupacional-02.webp',
  alt:'...descrição da prancha...',
  essence:'...uma frase...',
  detalhe:[ {n:'1',t:'Título painel',d:'texto com <code>..</code>/<b>..</b>'}, ... 5 painéis ],
  quiz:[ {stem:'...',choices:[['correta',1],['errada',0],['errada',0],['errada',0]],good:'<b>..</b> ..',bad:'..'}, ... 4 questões ]
}
```

Regras de conteúdo (aprendidas): **strings JS entre aspas simples; NÃO usar aspas simples (`'`) dentro do texto** — usar aspas duplas ou reescrever (senão quebra o JS do atlas). Exatamente **1** alternativa correta por questão (`choices` com um único `1`).

### Passos
1. Converter os PNGs para WebP (ver tabela). `sharp(src).webp({quality:82,effort:6}).toFile(out)`.
2. Inserir os 5 objetos **antes** do objeto `modulo-6`. Âncora robusta: a string `"{\n  id:'modulo-6',"`. Fazer `h.replace(anchor, NOVOS_OBJETOS + ',\n' + anchor)`.
3. Inserir 5 links no `.jump` **antes** de `<a href="#modulo-6">06 · Síndromes</a>`: `RO2 · Poeiras`, `RO3 · Rural & biomassa`, `RO4 · Asma ocupacional`, `RO5 · Silicose`, `RO6 · DPOC biomassa` (ids `#ocupacional-2..6`).
4. Validar:
   - Extrair o `<script>` e rodar `node --check`.
   - `eval` do array `FIGURAS` e checar: `f.img` existe em disco; cada questão tem exatamente 1 correta; total de figuras = 20.
5. Renderizar 1–2 seções por vez com Playwright (element screenshot de `#ocupacional-2` etc.) para conferir que a imagem carrega. (Chromium em `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`; `playwright-core` via `npm i playwright-core --no-save`, rodar com `NODE_PATH=$PWD/node_modules`.)
6. **Commit e push IMEDIATO** (ver §5).

## 4. Conteúdo pronto para RO2–RO6 (detalhamento + quiz)

RO2, RO3, RO4 foram **confirmados pela prancha**. RO5 e RO6 estão escritos a partir do **conteúdo dos módulos** (que esta sessão construiu) — confira contra a prancha real quando reenviada.

### RO2 — `id:'ocupacional-2'` · `Ocupacional · RO-02` · "Poeiras minerais" · `respira-ocupacional-02-poeiras-minerais.html`
essence: `Partículas que ficam e fibrosam: cada poeira mineral tem um alvo e uma complicação a rastrear.`
Painéis (da prancha: Sílica / Asbesto / Carvão / Berílio / Metais duros):
1. **Sílica** — nódulos nos lobos superiores, gânglios em "casca de ovo"; rastrear TB (silicotuberculose) sempre.
2. **Asbesto** — placas pleurais (marcador) e fibrose basal; risco de mesotelioma e câncer (sinergia com tabaco).
3. **Carvão** — nódulos antracóticos; forma complicada = fibrose maciça progressiva (FMP).
4. **Berílio** — granulomas que imitam sarcoidose; exige história + teste de proliferação linfocitária (BeLPT).
5. **Metais duros** — pneumonia intersticial de células gigantes; fibrose ocupacional.
Quiz:
- "Na silicose, o rastreio obrigatório é de:" → **Tuberculose** / Diabetes / Anemia / Litíase. good: silicotuberculose é regra.
- "O marcador de exposição ao asbesto é:" → **Placas pleurais** / Caverna apical / Nódulo maligno / Derrame sempre maligno.
- "Fibrose maciça progressiva (FMP) é:" → **Coalescência de nódulos em massas (sílica/carvão)** / Um tumor benigno / Exclusiva do asbesto / Sinônimo de TB.
- "A doença do berílio é importante porque:" → **Imita sarcoidose (precisa de história + BeLPT)** / Some sozinha / Não tem relação com exposição / Só dá sintoma cutâneo.

### RO3 — `id:'ocupacional-3'` · `Ocupacional · RO-03` · "Pulmão rural e biomassa" · `respira-ocupacional-03-rural-biomassa.html`
essence: `Três caminhos do campo: irritante (biomassa), imune (mofo/aves) e tóxico (agrotóxico).`
Painéis (da prancha: Fogão a lenha / Mofo e feno / Aves / Cana-algodão-grãos / Agrotóxicos):
1. **Fogão a lenha** — fumaça de biomassa em ambiente fechado → DPOC não tabágica (sobretudo mulher rural).
2. **Mofo e feno** — actinomicetos termofílicos → pneumonite de hipersensibilidade (pulmão do fazendeiro).
3. **Aves** — proteínas aviárias → antígeno inalado (pulmão do criador de aves).
4. **Cana / algodão / grãos** — poeira orgânica → bagaçose, bissinose ("febre de segunda"), doença do silo.
5. **Agrotóxicos** — irritante/tóxico: paraquat fibrosa o pulmão; organofosforado dá quadro colinérgico agudo.
Quiz:
- "Mulher rural, nunca fumou, fogão a lenha, obstrução: causa provável?" → **DPOC por biomassa** / Asma alérgica / Fibrose idiopática / Normal.
- "A pneumonite de hipersensibilidade ocorre por:" → **Resposta imune a antígenos orgânicos inalados** / Fibrose por partícula mineral / Broncoespasmo por frio / Infecção aguda.
- "Sintomas que melhoram na folga sugerem:" → **Componente reativo/ocupacional (afastar cedo pode reverter)** / Doença fixa / Genética / Simulação.
- "O paraquat é temido no pulmão porque:" → **Causa fibrose pulmonar progressiva** / Só tosse leve / Melhora com O2 alto / Não afeta o pulmão.

### RO4 — `id:'ocupacional-4'` · `Ocupacional · RO-04` · "Solda, tinta e asma ocupacional" · `respira-ocupacional-04-asma-ocupacional.html`
essence: `Sensibilizante × irritante × sistêmico: a asma que nasce no trabalho e o diário de pico de fluxo que a prova.`
Painéis (da prancha: Isocianatos / Solda-fumos metálicos / RADS / Pico de fluxo trabalho×folga / Febre dos fumos):
1. **Isocianatos** — sensibilizante nº 1 (TDI/MDI; tintas, vernizes, espumas de poliuretano); latência, piora no trabalho.
2. **Solda — fumos metálicos** — óxidos de ferro, manganês, níquel, cromo; bronquite, siderose.
3. **RADS** — irritante em dose única alta; início súbito, **sem latência**, sintomas persistentes.
4. **Pico de fluxo** — diário trabalho × folga: cai na semana, recupera na folga (dente-de-serra) = asma ocupacional.
5. **Febre dos fumos metálicos** — síndrome sistêmica (febre, calafrios, mialgia) 4–12 h após soldar; autolimitada, **não é asma**.
Quiz:
- "Asma ocupacional por sensibilizante (isocianato) tem:" → **Latência, piora no trabalho, melhora na folga** / Início após exposição única / Sem relação com trabalho / Melhora ao voltar.
- "A RADS ocorre após:" → **Exposição única e intensa a irritante, sem latência** / Anos de exposição imune / Exposição mínima repetida / Infecção viral.
- "A ferramenta que liga sintoma e trabalho é:" → **Diário seriado de pico de fluxo** / Radiografia / Hemograma / Gasometria isolada.
- "A febre dos fumos metálicos é:" → **Quadro gripal autolimitado, não é asma** / Asma grave irreversível / Pneumoconiose / Câncer.

### RO5 — `id:'ocupacional-5'` · `Ocupacional · RO-05` · "Silicose do jateamento" · `respira-ocupacional-05-silicose-jateamento.html`
> Escrito do módulo (confirmar contra a prancha real).
essence: `A dose que encurta a latência: jateamento e a silicose acelerada e aguda.`
Painéis prováveis:
1. **Jateamento** — dose extrema de sílica respirável (areia; jateamento de jeans).
2. **Acelerada** — latência de 5–10 anos, mais inflamatória, FMP precoce.
3. **Aguda (silicoproteinose)** — meses a poucos anos; preenchimento alveolar, "crazy paving"; alta letalidade.
4. **Complicações** — silicotuberculose (rastrear TB) e autoimunidade (esclerose sistêmica, AR, vasculites).
5. **Prevenção / evento sentinela** — substituir o abrasivo, via úmida, ventilação, EPI; um caso jovem denuncia o coletivo (notificar).
Quiz:
- "Por que o jateamento causa silicose em poucos anos?" → **A concentração de sílica respirável é altíssima (dose extrema)** / A sílica é diferente / Trabalhadores mais velhos / Acaso.
- "A silicose aguda (silicoproteinose) mostra:" → **Preenchimento alveolar, crazy paving, curso rápido e grave** / Só placas pleurais / Nódulos estáveis / Função normal.
- "Na silicose acelerada, o rastreio de TB é:" → **Ainda mais crítico (risco muito elevado)** / Dispensável / Só com febre / Irrelevante.
- "A medida que de fato resolve é:" → **Eliminar a exposição (substituir abrasivo, via úmida, EPI)** / Mais oxigênio / Trocar broncodilatador / Aumentar produtividade.

### RO6 — `id:'ocupacional-6'` · `Ocupacional · RO-06` · "DPOC da biomassa" · `respira-ocupacional-06-dpoc-biomassa.html`
> Escrito do módulo (confirmar contra a prancha real).
essence: `A fumaça que não é cigarro: o fenótipo de via aérea da DPOC da biomassa.`
Painéis prováveis:
1. **Biomassa** — fogão a lenha em ambiente fechado, mulher rural que nunca fumou.
2. **Fenótipo de via aérea** — mais bronquite/via aérea e **menos enfisema** que a DPOC do tabaco.
3. **Antracofibrose** — antracose brônquica com distorção/estenose; associada à tuberculose.
4. **Subdiagnóstico** — espirometria subutilizada; "a DPOC que nunca fumou" — pergunte o fogão.
5. **Prevenção** — fogão melhorado com chaminé, ventilação, combustível limpo (GLP).
Quiz:
- "DPOC em mulher rural que nunca fumou, fogão a lenha:" → **DPOC por biomassa** / Asma alérgica / Fibrose idiopática / Normal.
- "Comparada à DPOC do tabaco, a da biomassa tende a ter:" → **Mais via aérea/bronquite, menos enfisema** / Mais enfisema e bolhas / Nenhuma obstrução / Restrição pura.
- "A antracofibrose brônquica associa-se a:" → **Tuberculose** / Asma sazonal / Refluxo / Nada.
- "A prevenção mais eficaz é:" → **Fogão melhorado, ventilação e combustível limpo** / Só broncodilatador / Fechar janelas / Cozinhar mais tempo.

## 5. Disciplina de git (IMPORTANTE — houve perda por reset)

O container é reciclado sem aviso e **descarta trabalho não-pushado** e os uploads. Portanto:
- Fazer commit e **`git push -u origin claude/beautiful-cray-gZWCC` IMEDIATAMENTE** após cada bloco integrado (não acumular local).
- Identidade já configurada; se pedir, `git config user.email noreply@anthropic.com && git config user.name Claude`.
- Mensagem de commit termina com:
  `Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>` e a linha `Claude-Session: ...` (padrão do harness).
- **Não** criar PR sem o usuário pedir. Os commits do Atlas estão na mesma branch do PR #8 (docs). Ao final, atualizar o título/escopo do PR #8 ou alinhar com o usuário.

## 6. Armadilhas conhecidas do ambiente

- **`sharp` e `playwright-core` somem** do `node_modules` a cada `npm i` de um deles (removem o outro) e a cada reset. Reinstalar sob demanda: `npm i sharp --no-save` / `npm i playwright-core --no-save`; rodar scripts com `NODE_PATH=$PWD/node_modules`.
- **API de visão rejeita imagens grandes** de forma intermitente ("media removed"). Contorno: `sharp(png).resize(700).jpeg({quality:50})` → `Read` no JPEG pequeno. Ainda assim pode falhar; tentar de novo.
- `Date.now()`/`Math.random()` etc. não são o problema aqui; o `atlas.html` embaralha o quiz no cliente.
- Verificar sempre com HTML cru + `node --check`, não confiar em cache.

## 7. Definition of Done desta tarefa

- `atlas.html` com **20 pranchas** (01–10, RF1–4, RO1–6), na ordem curricular.
- Cada RO com 5 painéis + 4 questões (1 correta cada); imagem WebP presente.
- Menu `.jump` com os 5 links novos; meta coerente.
- Renderização conferida (imagem carrega) em ao menos 1 prancha nova.
- Tudo **commitado e pushado**.
- Fecha o P0 da auditoria (`Docs/atlas-auditoria.md`): Atlas cobre toda a série.

*Fim do handoff. Referências: `Docs/atlas-laminas-plano.md` (plano original), `Docs/atlas-auditoria.md` (auditoria).*
