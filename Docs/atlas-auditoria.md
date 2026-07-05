# Auditoria Respira - Atlas, modulos, figuras e navegacao

Data da revisao: 2026-07-04  
Repositorio auditado: `Drmcoelho/Respira`  
Escopo principal: parte Respira, com enfase em `index.html`, `atlas.html`, `data/respira-modules.json`, `modules/`, `assets/figuras/` e midias em `assets/respira-ventila-atlas/media/`.

> **Status (2026-07-05): o achado P0 abaixo foi resolvido.** Depois desta auditoria, o Atlas foi expandido para 20 laminas, integrando os modulos 01-10, a Ponte Funcional RF1-4 e o bloco Ocupacional RO1-RO6 completo. As pranchas correspondentes ja existem em `assets/figuras/`, e os metadados de `atlas.html` foram atualizados e nao dizem mais "modulos 1 a 5". O texto abaixo permanece como registro historico do estado antes da correcao — nao editado, para preservar o raciocinio da auditoria original.

## Sumario executivo

O projeto nao esta em estado "quase pronto" do ponto de vista de entrega editorial/navegacional. Ha conteudo e estrutura importante, mas a publicacao esta fragmentada em tres camadas:

1. `index.html` lista 10 modulos Respira principais, alem de trilhas RF e RO.
2. `atlas.html` cobre somente os modulos 01 a 05.
3. `modules/respira-*.html` existe para 01 a 10, mas esses arquivos canonicos sao wrappers que carregam arquivos legados `mvp*-interativo.html`.

O problema central nao e a ausencia total de conteudo. O problema e a diferenca entre:

- modulo existir no repositorio;
- modulo aparecer no indice;
- modulo aparecer no Atlas;
- modulo ter figura/prancha;
- modulo ter navegacao/interacao robusta para usuario final.

Essas cinco coisas hoje nao estao sincronizadas.

## Fontes verificadas

| Fonte | Achado relevante |
|---|---|
| `index.html` | Lista 10 modulos principais Respira como "10 de 10 modulos no ar", alem de RF1-RF4 e RO1-RO6. |
| `data/respira-modules.json` | Confirma mapa canonico dos 10 modulos Respira: 01 a 10, cada um com `canonical_path` e `legacy_path`. |
| `modules/` | Contem os 10 wrappers canonicos `respira-01` a `respira-10`. |
| `atlas.html` | Foi escrito somente para as pranchas dos modulos 01 a 05. O proprio texto/meta fala em "modulos 1 a 5". |
| `assets/figuras/` | Contem apenas `modulo-01.webp` a `modulo-05.webp`. |
| `assets/respira-ventila-atlas/media/` | Contem midias adicionais para varios temas, incluindo R06 e R08, mas isso nao equivale a integracao no Atlas principal. |

## Matriz dos modulos Respira principais

| Modulo | Titulo | Presente no `index.html` | Presente em `data/respira-modules.json` | Wrapper canonico em `modules/` | Presente no `atlas.html` | Prancha em `assets/figuras/` | Midia/figura dentro do modulo | Risco de navegacao |
|---:|---|---|---|---|---|---|---|---|
| 01 | Como o ar entra e sai | Sim | Sim | Sim | Sim | Sim: `modulo-01.webp` | Nao auditado integralmente no interativo; Atlas cobre | Baixo/moderado: ha redirecionadores legados |
| 02 | Saturar nao e respirar bem | Sim | Sim | Sim | Sim | Sim: `modulo-02.webp` | Nao auditado integralmente no interativo; Atlas cobre | Baixo/moderado: ha redirecionadores legados |
| 03 | Onde o ar e o sangue se encontram | Sim | Sim | Sim | Sim | Sim: `modulo-03.webp` | Nao auditado integralmente no interativo; Atlas cobre | Baixo/moderado: ha redirecionadores legados |
| 04 | A gasometria como narrativa | Sim | Sim | Sim | Sim | Sim: `modulo-04.webp` | `mvp4.html` sem `<img>`/`figure` encontrado | Moderado: interativo por codigo, sem figura real interna identificada |
| 05 | A arquitetura que respira | Sim | Sim | Sim | Sim | Sim: `modulo-05.webp` | Nao auditado integralmente no interativo; Atlas cobre | Baixo/moderado: ha redirecionadores legados |
| 06 | As grandes sindromes | Sim | Sim | Sim | Nao | Nao | Sim: `r06-pneumonia.jpg`, `r06-pulmonary-edema.jpg`, `r06-pneumothorax.jpg` em `mvp6.html` | Moderado: links para labs por hash; nao aparece no Atlas |
| 07 | A terapeutica - as forcas | Sim | Sim | Sim | Nao | Nao | Nao foi encontrado bloco de imagem/figura no trecho auditado de `mvp7.html` | Alto: cadeia wrapper -> interativo -> base; varios links dependem de hash/labs externos |
| 08 | Oxigenio e suporte nao invasivo | Sim | Sim | Sim | Nao | Nao | Sim: `r08-venturi-mask.png`, `r08-bipap.jpg` em `mvp8.html` | Moderado: tem imagens e lab, mas nao aparece no Atlas |
| 09 | Ventilacao mecanica - fundamentos | Sim | Sim | Sim | Nao | Nao | Nao: `mvp9.html` sem `<img>`/`figure` encontrado | Moderado/alto: interativo por SVG/DOM; sem figura real; nao aparece no Atlas |
| 10 | Ventilacao protetora e desmame | Sim | Sim | Sim | Nao | Nao | Nao: `mvp10.html` sem `<img>`/`figure` encontrado | Moderado/alto: interativo por codigo; links para labs externos; nao aparece no Atlas |

## Atlas

### Confirmado

O `atlas.html` esta limitado aos modulos 01 a 05:

- menu interno: 01, 02, 03, 04, 05;
- array `FIGURAS`: entradas `modulo-1` a `modulo-5`;
- imagens chamadas: `assets/figuras/modulo-01.webp` a `assets/figuras/modulo-05.webp`;
- metadados descrevem "pranchas dos modulos 1 a 5".

### Consequencia

O Atlas nao representa o estado real do projeto. Ele sugere uma serie visual fechada de 5 pranchas, enquanto o indice principal e o mapa canonico declaram 10 modulos Respira. Portanto, para usuario final, ha uma quebra editorial clara: os modulos 06 a 10 existem em outras rotas, mas nao entram no Atlas.

## Figuras e midias

### Pranchas principais em `assets/figuras/`

| Arquivo | Status |
|---|---|
| `modulo-01.webp` | Existe |
| `modulo-02.webp` | Existe |
| `modulo-03.webp` | Existe |
| `modulo-04.webp` | Existe |
| `modulo-05.webp` | Existe |
| `modulo-06.webp` | Ausente |
| `modulo-07.webp` | Ausente |
| `modulo-08.webp` | Ausente |
| `modulo-09.webp` | Ausente |
| `modulo-10.webp` | Ausente |

### Midias avulsas existentes em `assets/respira-ventila-atlas/media/`

Ha midias respiratorias adicionais, incluindo:

- R01: `r01-airway-tree.svg`, `r01-flow-volume-loop.svg`;
- R02: `r02-oxyhemoglobin.svg`, `r02-pulse-oximeter.jpg`;
- R03: `r03-vq-mismatch.jpg`, `r03-vq-paired.jpg`;
- R04: `r04-acid-base.svg`, `r04-davenport.jpg`;
- R05: `r05-alveolus.png`, `r05-respiratory-zone.jpg`;
- R06: `r06-pneumonia.jpg`, `r06-pneumothorax.jpg`, `r06-pulmonary-edema.jpg`;
- R08: `r08-bipap.jpg`, `r08-venturi-mask.png`.

Interpretacao: o repositorio tem um banco de midia mais rico do que o Atlas mostra. O problema e de integracao editorial: essas midias nao foram consolidadas no `atlas.html` principal, e nao ha pranchas `modulo-06.webp` a `modulo-10.webp`.

## Navegacao e arquitetura

### Camada canonica

Os arquivos em `modules/respira-*.html` sao wrappers. Eles nao contem o modulo completo; carregam a versao legada por `assets/js/legacy-module-loader.js`.

Exemplo verificado:

- `modules/respira-07-terapeutica.html` carrega `../assets/js/legacy-module-loader.js`;
- esse loader faz `fetch('../mvp7-interativo.html')`;
- `mvp7-interativo.html`, por sua vez, faz `fetch('mvp7.html')`;
- `mvp7.html` contem o conteudo real.

### Risco pratico

Essa arquitetura cria uma cadeia fragil:

1. pagina canonica;
2. loader JS;
3. fetch da pagina legada interativa;
4. segundo fetch da base;
5. `document.write`;
6. hashes/links para laboratorios externos.

Se qualquer camada falhar, o usuario ve uma tela de carregamento, um fallback ou links que parecem nao levar a lugar nenhum.

## Modulos com maior risco

### Modulo 07 - Terapeutica

Status: critico.

Motivos:

- nao aparece no Atlas;
- nao possui prancha `modulo-07.webp`;
- arquivo canonico e wrapper;
- arquivo interativo tambem e wrapper;
- base real fica em `mvp7.html`;
- links de laboratorio dependem de hashes em outros modulos (`mvp1-interativo.html#...`, `mvp3-interativo.html#...`, etc.);
- se o carregamento via fetch/document.write falhar, a experiencia vira "clico e nada acontece" ou "abre mas nao sai do lugar".

Conclusao: o 07 existe como conteudo, mas nao esta robusto como produto final navegavel.

### Modulo 09 - Ventilacao mecanica fundamentos

Status: incompleto visualmente.

Motivos:

- nao aparece no Atlas;
- nao possui prancha `modulo-09.webp`;
- `mvp9.html` nao tem `<img>` nem `figure` encontrado;
- depende de interatividade por DOM/SVG/codigo;
- o tema exige imagem/curva/onda forte para didatica.

Conclusao: pode ter simulador funcional, mas falta camada visual editorial no padrao Atlas.

### Modulo 10 - Ventilacao protetora e desmame

Status: incompleto visualmente.

Motivos:

- nao aparece no Atlas;
- nao possui prancha `modulo-10.webp`;
- `mvp10.html` nao tem `<img>` nem `figure` encontrado;
- possui links para laboratorios mecanisticos, mas sem prancha propria consolidada.

Conclusao: conteudo interativo existe, mas a entrega visual esta abaixo do padrao dos modulos 01 a 05.

## Modulos com figuras fora do Atlas

### Modulo 06

Tem imagens internas:

- pneumonia/consolidacao lobar;
- edema pulmonar;
- pneumotorax.

Problema: essas imagens nao viraram prancha `modulo-06.webp` nem entrada no `atlas.html`.

### Modulo 08

Tem imagens internas:

- mascara de Venturi;
- VNI/BiPAP.

Problema: essas imagens tambem nao viraram prancha `modulo-08.webp` nem entrada no `atlas.html`.

## Trilhas adicionais presentes no indice

O `index.html` tambem lista trilhas que aumentam a percepcao de incompletude quando o Atlas fica restrito a 5 pranchas:

### Ponte funcional

- RF1: `respira-ponte-01-volumes-capacidades.html`;
- RF2: `respira-ponte-02-espirometria.html`;
- RF3: `respira-ponte-03-padroes.html`;
- RF4: `respira-ponte-04-dlco.html`.

### Respira ocupacional

- RO1: `respira-ocupacional-01-profissao-sinal-vital.html`;
- RO2: `respira-ocupacional-02-poeiras-minerais.html`;
- RO3: `respira-ocupacional-03-rural-biomassa.html`;
- RO4: `respira-ocupacional-04-asma-ocupacional.html`;
- RO5: `respira-ocupacional-05-silicose-jateamento.html`;
- RO6: `respira-ocupacional-06-dpoc-biomassa.html`.

Observacao: esses 10 modulos adicionais aparecem no indice principal, mas nao foram incluidos na auditoria visual profunda deste arquivo. Eles devem receber uma segunda rodada de auditoria propria, porque aumentam o total percebido pelo usuario para muito alem dos 10 Respira principais.

## Lista objetiva de pendencias

### P0 - Quebra de confianca do produto

- Atualizar `atlas.html` para deixar de dizer/parecer que o Atlas cobre a serie se ele cobre so 01 a 05.
- Ou expandir o Atlas para 01 a 10.
- Sincronizar texto de `atlas.html`, `index.html` e `data/respira-modules.json`.

### P1 - Figuras ausentes no padrao Atlas

Criar/integrar:

- `assets/figuras/modulo-06.webp`;
- `assets/figuras/modulo-07.webp`;
- `assets/figuras/modulo-08.webp`;
- `assets/figuras/modulo-09.webp`;
- `assets/figuras/modulo-10.webp`.

### P1 - Navegacao canonica fragil

Rever a arquitetura:

- evitar cadeia dupla wrapper -> wrapper -> base;
- preferir que `modules/respira-07-terapeutica.html` contenha o conteudo final autocontido ou carregue uma unica fonte robusta;
- preservar links antigos, mas nao depender deles como experiencia primaria;
- testar rotas canonicas diretamente em GitHub Pages.

### P1 - Modulo 07

- Transformar o 07 em pagina final robusta;
- testar todos os links de laboratorio;
- adicionar prancha propria;
- revisar se hashes como `#r=...`, `#lab`, `#m=...` realmente ativam o estado esperado nos modulos de destino.

### P2 - Modulos 09 e 10

- Criar figuras/pranchas visuais;
- considerar screenshots didaticos das ondas, pausa inspiratoria, driving pressure, mechanical power, TRE/RSBI;
- integrar no Atlas.

### P2 - Modulos 06 e 08

- As imagens internas ja existem;
- falta transformar isso em entrada de Atlas/prancha;
- falta padronizar a experiencia visual com 01 a 05.

### P3 - RF e RO

- Auditar todos os RF1-RF4 e RO1-RO6;
- verificar se tem figuras;
- verificar se aparecem em algum Atlas ou se precisam de Atlas proprio;
- verificar se a navegacao volta para `index.html` e se os links internos funcionam.

## Checklist de verificacao manual no navegador

Usar no GitHub Pages:

- abrir `atlas.html`;
- confirmar visualmente que so aparecem 01 a 05;
- clicar cada prancha 01 a 05;
- abrir cada modulo canonico 01 a 10 em `modules/`;
- em cada modulo, testar:
  - botao de iniciar trilha;
  - troca de aba/segmento;
  - laboratorio/sala;
  - links externos para outros labs;
  - retorno ao indice;
  - funcionamento de hash/deep-link;
  - carregamento de imagens;
  - console sem erro vermelho.

## Conclusao

O projeto tem base boa, mas a entrega publicada esta incompleta e desalinhada.

O ponto mais importante: o Atlas nao e uma visao completa da parte Respira. Ele cobre 5 pranchas, enquanto o proprio projeto declara 10 modulos principais Respira, alem de trilhas RF e RO no indice.

Portanto, a avaliacao honesta e:

- conteudo: parcialmente robusto;
- arquitetura: funcional, mas fragil por wrappers e legados;
- Atlas: incompleto;
- figuras: incompletas;
- navegacao: exige revisao completa;
- estado de produto: ainda nao pronto para ser considerado final.
