# CODEX-VISION.md — Protocolo para o modelo que realmente vê

> Complemento operacional de `CODEX.md`.
> 
> Este documento deve ser usado quando o agente multimodal recebe as pranchas reais, screenshots do site ou rascunhos gerados. Sua função é impedir que uma análise baseada apenas em HTML, `alt`, nomes de arquivo ou intenção editorial seja apresentada como inspeção visual.

---

## 0. Princípio

O modelo que renderiza não deve ser tratado apenas como uma impressora obediente. Quando ele possui visão multimodal, deve atuar primeiro como **testemunha visual e crítico de design** e somente depois como ilustrador.

A cadeia correta é:

```text
conteúdo clínico + pranchas reais + site renderizado
                        ↓
              CRÍTICO VISUAL MULTIMODAL
                        ↓
     DNA visual observado + lacunas + desvios + oportunidades
                        ↓
                 DIRETOR DE ARTE CLÍNICO
                        ↓
        storyboard + prompt + arte-base + autocrítica
                        ↓
             REVISOR VISUAL SOBRE O RENDER
                        ↓
                  versão aprovada
```

Não use a cadeia reduzida:

```text
HTML → resumo textual → “faça um infográfico bonito”
```

Ela produz imagens que ilustram o assunto, mas não pertencem realmente à obra.

---

## 1. Regra de honestidade perceptiva

Só diga **“vi”, “observei”, “a prancha mostra”, “o desenho faz”** quando o raster, screenshot ou frame correspondente estiver efetivamente disponível na entrada multimodal.

Quando só houver código, `alt`, legenda ou descrição, use:

- “o HTML declara”;
- “o `alt` descreve”;
- “a intenção editorial parece ser”;
- “não foi possível confirmar visualmente”.

O `alt` é evidência da intenção semântica, não prova de que a composição conseguiu realizá-la.

---

## 2. Pacote mínimo que o crítico deve receber

Para falar como quem de fato viu, entregue ao modelo um **pacote de referência visual**, preferencialmente nesta ordem:

1. `contact-sheet-respira-atlas.webp` — as 20 pranchas do Atlas Respira;
2. `contact-sheet-exploracao.webp` — as seis pranchas de Exploração;
3. screenshots desktop de `index.html`, `atlas.html`, `ventila.html` e do módulo-alvo;
4. screenshots mobile das mesmas páginas;
5. imagem integral de três a cinco pranchas representativas em resolução legível;
6. screenshots dos laboratórios, SVGs ou Canvas do módulo-alvo em dois ou três estados causais;
7. ativos clínicos locais relevantes, como radiografias, TC, curvas ou fotografias;
8. primeira geração da nova prancha, quando houver, para revisão comparativa.

Não envie apenas uma prancha isolada e peça ao modelo para deduzir toda a identidade da série. A gramática visual mora na repetição e também nas exceções.

### Referências representativas obrigatórias

Selecione pelo menos:

- uma prancha fundacional;
- uma de troca gasosa;
- uma de prova funcional;
- uma terapêutica;
- uma ocupacional;
- uma de Exploração com alta densidade informacional.

O modelo deve ver simultaneamente unidade e diversidade.

---

## 3. Primeira tarefa: autópsia visual, não geração

Antes de criar qualquer prompt, o crítico deve executar uma leitura em cinco escalas.

### 3.1 Escala da série

Observar e registrar:

- proporção dominante;
- número típico de painéis;
- recorrência de grades horizontais, verticais ou híbridas;
- posição de títulos, números, legendas e conclusões;
- quantidade real de texto incorporado;
- densidade média e variação entre módulos;
- uso de espaço vazio;
- sequência do olhar;
- presença de uma conclusão visual ou apenas enumeração;
- quais pranchas parecem pertencer claramente à mesma família;
- quais parecem exceções ou deriva estilística.

### 3.2 Escala da prancha

Para cada referência, descrever:

- ponto focal inicial;
- caminho provável do olhar;
- hierarquia entre painéis;
- equilíbrio entre anatomia, curva, ícone e texto;
- onde a causalidade é visível;
- onde a causalidade depende da legenda;
- zonas congestionadas;
- elementos redundantes;
- elementos importantes pequenos demais;
- se a composição funciona sem zoom;
- se funciona em largura de celular.

### 3.3 Escala do vocabulário visual

Extrair o que foi **realmente observado**, não o que a documentação recomenda:

- espessura e regularidade dos contornos;
- grau de achatamento ou volume das formas;
- tratamento de pulmões, alvéolos, capilares, coração e dispositivos;
- uso de silhuetas humanas;
- estilo das setas;
- aparência das curvas;
- gradações, sombras e texturas;
- tratamento de radiografia e TC;
- consistência dos ícones;
- código cromático efetivo;
- contraste entre normal, falha, risco e benefício;
- presença de metáforas visuais recorrentes.

### 3.4 Escala cognitiva

Responder:

- qual pergunta a prancha faz antes de explicar;
- o que o aluno consegue deduzir só olhando;
- qual armadilha cognitiva ficou visível;
- se a imagem mostra mecanismo ou apenas categorias;
- se existe comparação contrafactual;
- se benefício e custo aparecem juntos;
- se a decisão clínica nasce da figura ou foi apenas anexada no final;
- se a prancha ensina relação causal, classificação ou memória visual;
- se a intenção declarada no HTML foi efetivamente realizada.

### 3.5 Escala da execução

Registrar defeitos de renderização:

- texto deformado ou incorreto;
- números e fórmulas suspeitos;
- anatomia impossível;
- setas ambíguas;
- mãos, rostos ou equipamentos artificiais;
- curvas fisiologicamente incoerentes;
- rótulos que disputam espaço;
- baixa resolução;
- compressão excessiva;
- inconsistência de perspectiva;
- painéis com estilos incompatíveis dentro da mesma prancha.

---

## 4. Verdade renderizada versus intenção declarada

O crítico deve produzir uma tabela de divergência.

| Elemento | Intenção declarada no módulo | O que foi visto | Consequência didática | Correção proposta |
|---|---|---|---|---|
| causalidade | o aluno deveria perceber X causando Y | a seta não liga X a Y / relação clara | dedução possível ou perdida | mudança concreta |
| hierarquia | painel 4 deveria ser a virada | painel 1 domina visualmente | narrativa se inverte | redistribuir escala/contraste |
| anatomia | diferenciar alvéolo, interstício e capilar | compartimentos se confundem | mecanismo de difusão fica impreciso | redesenhar corte |
| decisão | mostrar custo e benefício | só o benefício está destacado | imagem vira propaganda de intervenção | adicionar custo concorrente |

Essa tabela é central. Ela transforma o modelo visual em alguém que confronta a obra com a própria ambição.

---

## 5. Extração do DNA visual observado

Depois de ver o conjunto, produzir um **DNA visual empírico** em três classes.

### 5.1 Invariantes observados

Elementos que aparecem de modo recorrente e devem ser preservados:

- estrutura de painel;
- paleta real;
- formas de numeração;
- anatomia esquemática;
- grau de simplificação;
- integração entre curva e órgão;
- relação imagem-texto;
- acabamento editorial.

### 5.2 Variações legítimas

Elementos que mudam porque o conteúdo exige:

- tabela versus storyboard;
- mapa de quadrantes versus sequência temporal;
- radiologia versus ilustração vetorial;
- cena clínica versus corte microscópico;
- uso de quatro, cinco ou seis painéis;
- presença de um painel dominante.

### 5.3 Acidentes e vícios que não devem ser canonizados

Não transformar erro repetido em identidade:

- excesso de texto pequeno;
- painéis igualmente importantes quando existe uma virada causal;
- radiologia pseudo-realista imprecisa;
- setas decorativas;
- legenda que carrega todo o raciocínio;
- anatomia genérica repetida sem função;
- densidade uniforme que elimina ritmo;
- ausência de contraste entre mecanismo e consequência.

O resultado deve separar **assinatura autoral** de **limitação histórica do gerador**.

---

## 6. O modelo visual como coautor, não imitador

Depois de extrair o DNA, o modelo deve propor evolução.

Não basta dizer:

> “faça igual às pranchas anteriores”.

A instrução correta é:

> “preserve os invariantes que dão unidade à série, elimine os acidentes que reduzem legibilidade e explore uma solução nova que revele melhor a tese causal deste módulo”.

A nova prancha deve parecer descendente da série, não cópia de uma irmã específica.

### Teste de parentesco

A prancha é aprovada quando:

- colocada ao lado das referências, pertence claramente ao mesmo projeto;
- vista isoladamente, possui uma tese visual própria;
- não depende de repetir exatamente a grade de outra prancha;
- melhora alguma fragilidade observada nas referências;
- continua reconhecível depois de remover título e logotipo.

---

## 7. Prompt-mestre para o crítico visual multimodal

Use o texto abaixo com as imagens anexadas.

```text
Você recebeu um conjunto de pranchas didáticas reais do projeto Respira/Ventila e screenshots do site publicado. Sua primeira função NÃO é gerar uma nova imagem. Atue como crítico visual multimodal, diretor de arte e especialista em comunicação científica.

Observe somente o que está efetivamente visível. Não use alt text, nomes de arquivo ou descrições externas como substitutos da imagem. Quando algo não puder ser confirmado visualmente, declare a limitação.

1. Faça uma autópsia visual da série: composição, hierarquia, densidade, caminho do olhar, paleta efetiva, contornos, anatomia, curvas, iconografia, radiologia, tipografia incorporada, legibilidade desktop/mobile e coerência entre pranchas.
2. Separe invariantes autorais, variações legítimas e defeitos/acidentes que não devem ser repetidos.
3. Para cada prancha, identifique: tese visual, mecanismo visível, armadilha cognitiva, ponto de virada, decisão clínica e o que depende excessivamente de legenda.
4. Confronte a intenção declarada do módulo com a verdade renderizada: o que a imagem realmente comunica, omite ou comunica de forma contrária.
5. Extraia um DNA visual empírico da série.
6. Só depois analise o módulo-alvo e proponha como a nova prancha pode pertencer à família sem copiar uma composição existente.
7. Produza uma matriz de continuidade e inovação: o que preservar, o que corrigir e o que explorar pela primeira vez.
8. Não elogie genericamente. Toda avaliação deve apontar evidência visual concreta.

Sua saída deve conter:
- diagnóstico da série;
- diagnóstico das referências individualmente;
- verdade renderizada versus intenção;
- DNA visual observado;
- vícios a evitar;
- oportunidades inéditas para o módulo-alvo;
- recomendação de direção de arte antes do storyboard.
```

---

## 8. Prompt-mestre para o ilustrador depois da crítica

A crítica visual deve ser anexada ao prompt do ilustrador.

```text
Você é o ilustrador clínico do projeto Respira/Ventila. Recebeu:
A) as pranchas reais da série;
B) a autópsia produzida pelo crítico visual multimodal;
C) o HTML e a tese clínica do módulo-alvo;
D) um storyboard aprovado;
E) a gramática e os gates de CODEX.md.

Não copie literalmente nenhuma prancha. Preserve os invariantes observados que produzem parentesco visual e corrija os vícios identificados pela crítica.

A imagem deve permitir deduzir a cadeia:
sistema → variável → falha → assinatura → decisão.

Mostre benefício e custo quando coexistirem. Faça curvas, anatomia, equipamento e contexto clínico falar a mesma língua. Gere arte-base com texto mínimo; reserve áreas para overlay tipográfico determinístico.

Antes de renderizar, declare em uma frase:
- qual é a tese visual;
- qual é o ponto de virada;
- qual elemento receberá o foco inicial;
- qual relação causal deve ser compreendida sem legenda.

Depois gere a imagem conforme o storyboard e o negative prompt de CODEX.md.
```

---

## 9. Revisão do primeiro render

O mesmo modelo, ou preferencialmente uma segunda instância multimodal, deve receber:

- as referências originais;
- a crítica anterior;
- o prompt usado;
- o primeiro render;
- o overlay tipográfico, se já aplicado.

Ele deve responder em quatro colunas:

| Gate | Evidência visual observada | Falha | Correção executável |
|---|---|---|---|
| científico | anatomia, direção, curva, variável | erro específico | redesenho específico |
| causal | ligação entre variável e consequência | elo ausente | seta, comparação ou painel |
| editorial | hierarquia, ritmo, densidade | congestionamento | simplificação concreta |
| parentesco | invariantes da série | deriva estilística | ajuste de forma/paleta/grade |

Não aceitar “está bom” como revisão. Cada gate deve conter evidência.

---

## 10. Protocolo de comparação contrafactual

Uma prancha clínica se torna muito mais forte quando não mostra apenas um estado, mas a diferença entre decisões.

Sempre testar se o módulo comporta:

- antes × depois;
- normal × falha;
- variável controlada × variável livre;
- ganho × custo;
- intervenção adequada × mesma intervenção no fenótipo errado;
- curva esperada × curva observada;
- pulmão homogêneo idealizado × pulmão heterogêneo real;
- número melhor × mecanismo pior.

O crítico deve apontar quando as pranchas existentes já usam essa lógica e quando uma nova prancha pode aprofundá-la.

---

## 11. Entregável do modelo que viu

Para cada lote de referências, entregar:

1. **Declaração de alcance perceptivo** — quais imagens e resoluções foram efetivamente vistas;
2. **Autópsia da série**;
3. **Autópsia de cada referência**;
4. **DNA visual empírico**;
5. **Verdade renderizada versus intenção**;
6. **Mapa de vícios e oportunidades**;
7. **Direção de arte para o módulo-alvo**;
8. **Storyboard**;
9. **Prompt de geração**;
10. **Negative prompt**;
11. **Manifesto de overlay**;
12. **Revisão do render produzido**;
13. **Resultado dos gates**.

---

## 12. Definição de sucesso

O modelo pode falar “como quem viu” quando:

- recebeu os rasters ou screenshots reais;
- consegue apontar evidências espaciais concretas;
- diferencia intenção textual de realização gráfica;
- reconhece padrões recorrentes sem inventá-los;
- identifica defeitos que o `alt` jamais revelaria;
- usa as referências para evoluir a série, não apenas imitá-la;
- revisa o render final comparando-o diretamente com a obra existente.

> O modelo que vê não recebe apenas um estilo. Ele recebe uma obra, interpreta sua gramática e devolve o próximo capítulo visual.
