# Plano de geracao das proximas laminas do Atlas Respira

Data: 2026-07-04  
Escopo: expansao do `atlas.html` a partir do estado atual confirmado.

> **Status (2026-07-05): "Lote 1" (as dez laminas abaixo) foi concluido.** `atlas.html` agora tem 15 laminas: modulos 01-10, Ponte Funcional RF1-4 e Ocupacional RO1. As pranchas correspondentes existem em `assets/figuras/`. O plano abaixo permanece como registro do que foi decidido e executado.
>
> **Atualizacao (2026-07-05, mesma data): o "lote seguinte" foi concluido.** RO2 (Poeiras minerais), RO3 (Pulmao rural e biomassa), RO4 (Solda, tinta e asma ocupacional), RO5 (Silicose acelerada do jateamento) e RO6 (DPOC da biomassa) ganharam lamina, arquivo `.webp` em `assets/figuras/respira-ocupacional-0{2,3,4,5,6}.webp` e entrada completa em `atlas.html` (paineis + quiz). `atlas.html` tem agora 20 laminas: os 10 modulos Respira, RF1-4 e **RO1-RO6 completo**. Nao ha mais pendencia de lamina no bloco Ocupacional.

## Estado atual do Atlas

O `atlas.html` esta implementado como Atlas de pranchas dos modulos 01 a 05.

Atualmente ele contem:

- menu interno com 5 entradas: 01, 02, 03, 04, 05;
- array `FIGURAS` com 5 objetos;
- imagens em `assets/figuras/modulo-01.webp` a `assets/figuras/modulo-05.webp`;
- detalhamento painel a painel para cada prancha;
- questoes interativas especificas para cada prancha;
- links finais para os modulos interativos correspondentes.

Problema editorial: o `index.html` declara 10 modulos Respira principais, alem de Ponte Funcional e Respira Ocupacional. Logo, o Atlas visual esta atrasado em relacao ao indice e ao mapa canonico.

## Decisao de lote

As proximas 10 laminas devem ser o primeiro lote de expansao apos as 5 existentes.

Prioridade escolhida:

1. Completar os 10 modulos Respira principais: laminas 06 a 10.
2. Incluir a Ponte Funcional completa: RF1 a RF4.
3. Iniciar Respira Ocupacional com RO1.

Isso produz um Atlas de 15 laminas:

- 5 ja existentes;
- 5 novas dos modulos Respira 06 a 10;
- 4 novas da Ponte Funcional;
- 1 nova de Respira Ocupacional.

O lote seguinte deve cobrir RO2 a RO6.

## Convencao de arquivos proposta

Manter as pranchas principais em `assets/figuras/`.

Para evitar ambiguidade entre modulo principal, Ponte Funcional e Ocupacional, usar nomes explicitos:

| Tipo | Arquivo proposto |
|---|---|
| Respira 06 | `assets/figuras/modulo-06.webp` |
| Respira 07 | `assets/figuras/modulo-07.webp` |
| Respira 08 | `assets/figuras/modulo-08.webp` |
| Respira 09 | `assets/figuras/modulo-09.webp` |
| Respira 10 | `assets/figuras/modulo-10.webp` |
| Ponte RF1 | `assets/figuras/respira-ponte-01.webp` |
| Ponte RF2 | `assets/figuras/respira-ponte-02.webp` |
| Ponte RF3 | `assets/figuras/respira-ponte-03.webp` |
| Ponte RF4 | `assets/figuras/respira-ponte-04.webp` |
| Ocupacional RO1 | `assets/figuras/respira-ocupacional-01.webp` |

## Padrao visual obrigatorio

Cada lamina deve preservar o padrao das pranchas 01 a 05:

- fundo claro e didatico;
- composicao em paineis numerados;
- leitura de mecanismo antes de protocolo;
- texto curto por painel;
- alto contraste;
- estilo medico-editorial, nao decorativo;
- imagem/diagrama central com valor cognitivo real;
- exportacao em `.webp` para publicacao;
- idealmente mesma proporcao das pranchas atuais para nao quebrar o layout do Atlas.

## Lote 1 - dez novas laminas

### Lamina 06 - As grandes sindromes

Arquivo: `assets/figuras/modulo-06.webp`  
Modulo: `modules/respira-06-sindromes.html` / `mvp6.html`

Paineis sugeridos:

1. SDRA: shunt + baixa complacencia + surfactante inativado.
2. DPOC/asma: resistencia alta + constante de tempo + auto-PEEP.
3. Edema agudo: liquido alveolar, complacencia baixa e shunt.
4. Pneumonia/atelectasia: unidade preenchida/fechada e hipoxemia refrataria parcial.
5. TEP/fibrose: espaco morto versus difusao/rigidez.

Midias existentes uteis:

- `r06-pneumonia.jpg`;
- `r06-pulmonary-edema.jpg`;
- `r06-pneumothorax.jpg`.

Observacao: precisa virar uma prancha de sintese, nao apenas colagem de radiografias.

### Lamina 07 - Terapeutica como vetores fisiologicos

Arquivo: `assets/figuras/modulo-07.webp`  
Modulo: `modules/respira-07-terapeutica.html` / `mvp7.html`

Paineis sugeridos:

1. Abrir o cano: broncodilatador reduz resistencia.
2. Recrutar o alveolo: PEEP, CPAP, prona, surfactante quando aplicavel.
3. Secar e amolecer: diuretico/nitrato no edema.
4. Casar V/Q: O2, alto fluxo, iNO como ponte.
5. Proteger/tamponar/resgatar: volume baixo, permissive hypercapnia, bicarbonato com ventilacao, ECMO.

Imagem central sugerida: mapa vetorial com eixos R, C, shunt, recrutamento, conteudo de O2 e pH.

Prioridade: alta. E a lamina mais importante para corrigir a percepcao de modulo vazio.

### Lamina 08 - Oxigenio e suporte nao invasivo

Arquivo: `assets/figuras/modulo-08.webp`  
Modulo: `modules/respira-08-oxigenio-suporte-nao-invasivo.html` / `mvp8.html`

Paineis sugeridos:

1. Baixo fluxo: FiO2 entregue depende da demanda inspiratoria.
2. Venturi: arraste de ar e FiO2 mais previsivel.
3. Alto fluxo: fluxo total, lavagem de espaco morto, umidificacao e PEEP leve.
4. CPAP: pressao continua para recrutamento.
5. BiPAP: IPAP/EPAP, descarga muscular e ventilacao.

Midias existentes uteis:

- `r08-venturi-mask.png`;
- `r08-bipap.jpg`.

Observacao: a lamina deve mostrar escalada de suporte, nao apenas dispositivos isolados.

### Lamina 09 - Ventilacao mecanica: fundamentos

Arquivo: `assets/figuras/modulo-09.webp`  
Modulo: `modules/respira-09-ventilacao-mecanica-fundamentos.html` / `mvp9.html`

Paineis sugeridos:

1. Equacao do movimento: `Paw = R x fluxo + V/C + PEEP`.
2. VCV: volume prometido, pressao como consequencia.
3. PCV: pressao prometida, volume como consequencia.
4. Pico, plato e driving pressure.
5. Pausa inspiratoria e leitura de onda.

Imagem central sugerida: ventilador + curvas pressao/fluxo/volume com anotacoes.

Observacao: precisa de figura forte porque o modulo atual e muito codigo/interatividade e pouca imagem real.

### Lamina 10 - Ventilacao protetora e desmame

Arquivo: `assets/figuras/modulo-10.webp`  
Modulo: `modules/respira-10-ventilacao-protetora-desmame.html` / `mvp10.html`

Paineis sugeridos:

1. Volume corrente por peso predito, nao por peso real.
2. Plato, driving pressure e stress/strain.
3. Mechanical power: volume, pressao, fluxo e frequencia como energia.
4. Hipercapnia permissiva: proteger pulmao antes de normalizar numero.
5. Desmame: TRE, RSBI, carga versus capacidade.

Imagem central sugerida: balanca entre protecao pulmonar e capacidade da bomba respiratoria.

### Lamina RF1 - Volumes e capacidades

Arquivo: `assets/figuras/respira-ponte-01.webp`  
Modulo: `respira-ponte-01-volumes-capacidades.html`

Paineis sugeridos:

1. Volumes: VC, VRI, VRE, VR.
2. Capacidades: CI, CRF, CV, CPT.
3. Aprisionamento: VR e CRF sobem.
4. Restricao verdadeira: CPT cai.
5. Reserva funcional: o que sobra quando o paciente descompensa.

Imagem central sugerida: barras empilhadas comparando normal, obstrutivo e restritivo.

### Lamina RF2 - Espirometria

Arquivo: `assets/figuras/respira-ponte-02.webp`  
Modulo: `respira-ponte-02-espirometria.html`

Paineis sugeridos:

1. VEF1 e CVF.
2. Relacao VEF1/CVF.
3. Curva fluxo-volume normal.
4. Obstrucao: concavidade e queda de fluxo.
5. Resposta broncodilatadora.

Imagem central sugerida: curva fluxo-volume + espirograma tempo-volume.

### Lamina RF3 - Padroes funcionais

Arquivo: `assets/figuras/respira-ponte-03.webp`  
Modulo: `respira-ponte-03-padroes.html`

Paineis sugeridos:

1. Obstrutivo: relacao baixa.
2. Restritivo: CPT baixa.
3. Misto: relacao baixa + CPT baixa.
4. Pseudorrestritivo: CVF baixa por aprisionamento, CPT normal/alta.
5. Matriz razao x CPT.

Imagem central sugerida: quadrante diagnostico relacao VEF1/CVF versus CPT.

### Lamina RF4 - DLCO e troca

Arquivo: `assets/figuras/respira-ponte-04.webp`  
Modulo: `respira-ponte-04-dlco.html`

Paineis sugeridos:

1. Barreira alveolo-capilar.
2. Area de troca.
3. Hemoglobina e volume sanguineo capilar.
4. DLCO baixa parenquimatosa/vascular.
5. DLCO preservada em restricao extrapulmonar.

Imagem central sugerida: alvéolo-capilar com caminhos do CO/O2 e comparador parenquima versus parede.

### Lamina RO1 - Profissao como sinal vital

Arquivo: `assets/figuras/respira-ocupacional-01.webp`  
Modulo: `respira-ocupacional-01-profissao-sinal-vital.html`

Paineis sugeridos:

1. Profissao antes de diagnostico: o que faz, onde, ha quanto tempo.
2. Exposicao real: poeira, fumaça, mofo, metal, solvente, biomassa.
3. EPI real versus EPI prescrito.
4. Temporalidade: melhora em folga/afastamento, piora no trabalho.
5. Nexo: colegas doentes, ambiente compartilhado, imagem e funcao respiratoria.

Imagem central sugerida: anamnese ocupacional em fluxograma circular, como um quinto sinal vital.

## Alteracoes necessarias em `atlas.html`

Para cada nova lamina:

1. Adicionar link no menu `.jump`.
2. Adicionar novo objeto no array `FIGURAS`.
3. Preencher:
   - `id`;
   - `mod`;
   - `titulo`;
   - `href`;
   - `img`;
   - `alt`;
   - `essence`;
   - `detalhe` com paineis;
   - `quiz` com 4 perguntas.
4. Atualizar metadados do Atlas para nao dizer "modulos 1 a 5".
5. Atualizar rodape, se necessario, para refletir Atlas expandido.

## Ordem de execucao recomendada

1. Gerar lamina 06.
2. Gerar lamina 08, aproveitando midias ja existentes.
3. Gerar lamina 07, por ser conceitualmente central e atualmente a mais fragil.
4. Gerar lamina 09.
5. Gerar lamina 10.
6. Gerar RF1 a RF4.
7. Gerar RO1.
8. Atualizar `atlas.html` em uma unica leva apos validar as imagens.
9. Testar GitHub Pages.
10. Abrir segunda auditoria para RO2 a RO6.

## Criterio de pronto

Uma lamina so entra no Atlas quando cumprir todos os itens:

- arquivo `.webp` presente em `assets/figuras/`;
- proporcao compativel com as pranchas atuais;
- texto legivel em desktop e mobile;
- painel numerado coerente com o modulo;
- `alt` descritivo;
- objeto `FIGURAS` completo;
- link para o modulo funcionando;
- quiz especifico da prancha;
- teste visual no `atlas.html` publicado.
