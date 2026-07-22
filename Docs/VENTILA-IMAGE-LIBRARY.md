# VENTILA-IMAGE-LIBRARY.md — Acervo visual, fontes e proveniência

> Escopo: imagens para os módulos `ventila00.html`–`ventila29.html`, Atlas Ventila e materiais transversais.
> 
> Relação normativa: este documento complementa `CODEX.md` e `Docs/CODEX-VISION.md`.

---

## 0. Tese

Ventilação mecânica não pode ser ensinada por uma única classe de imagem.

O Ventila precisa combinar, conforme a pergunta didática:

1. **imagem clínica real** — radiografia, tomografia, fotografia de equipamento, tela de ventilador, circuito e contexto de leito;
2. **figura científica licenciada** — anatomia, fisiologia, mecânica, curvas e esquemas provenientes de fontes abertas confiáveis;
3. **referência bibliográfica privada** — livros e documentos legitimamente acessíveis no Google Drive do autor, usados para compreensão, auditoria e reconstrução original;
4. **visual computacional determinístico** — SVG, Canvas, gráficos e simuladores produzidos por código;
5. **imagem original gerada por modelo** — cenas, cortes esquemáticos, metáforas causais e pranchas editoriais inexistentes nas fontes;
6. **composição híbrida** — fotografia ou radiologia real integrada a diagramas, setas, curvas e overlays próprios.

A pergunta não é “qual fonte é melhor?”. A pergunta é:

> Qual combinação de evidências visuais torna este mecanismo dedutível, clinicamente verdadeiro, juridicamente utilizável e editorialmente pertencente ao projeto?

---

## 1. Princípio de seleção por função

Cada imagem deve ter uma função declarada. Não adicionar imagens apenas para ornamentar o módulo.

Funções admitidas:

- **orientar** — mostrar onde estamos no sistema;
- **demonstrar** — tornar um mecanismo visível;
- **comparar** — normal versus falha, antes versus depois, modo versus modo;
- **reconhecer** — treinar assinatura radiológica, gráfica ou de monitor;
- **simular** — permitir manipulação de uma variável;
- **decidir** — conectar achado a conduta;
- **memorizar** — criar âncora visual sem substituir explicação causal;
- **documentar** — registrar equipamento, interface ou situação clínica real.

Toda imagem integrada ao repositório deve declarar pelo menos uma dessas funções no manifesto.

---

## 2. Hierarquia das fontes

### 2.1 Fonte clínica ou técnica primária

Preferir quando o objetivo é reconhecer realidade de leito:

- imagens próprias desidentificadas e autorizadas;
- bases institucionais abertas;
- manuais oficiais de fabricantes, quando a licença permitir;
- documentação técnica oficial;
- artigos científicos com licença compatível;
- repositórios públicos de radiologia e fisiologia.

Use para:

- radiografias e tomografias;
- telas e curvas reais;
- circuitos, interfaces e ventiladores;
- assinaturas de assincronia;
- posicionamento de dispositivos;
- comparação entre equipamento idealizado e equipamento real.

### 2.2 Fonte aberta secundária

Usar figuras de:

- Wikimedia Commons;
- OpenStax;
- NIH, CDC, WHO e outras agências públicas quando a licença ou o regime jurídico permitir;
- periódicos e repositórios com Creative Commons explícita;
- livros-texto open access;
- bancos científicos com termo de reutilização claro.

A presença pública na internet não equivale a licença aberta.

### 2.3 Livros e documentos do Google Drive

Os livros no Drive podem ser usados como:

- fonte de compreensão;
- fonte de conferência anatômica e fisiológica;
- referência para identificar conceitos ausentes;
- base para comparar nomenclaturas;
- inspiração estrutural em nível abstrato;
- fonte bibliográfica citada no texto.

Eles não devem ser tratados automaticamente como banco de imagens redistribuíveis.

Regra operacional:

> Ver no livro não autoriza copiar a figura para o repositório.

Para cada figura de livro, decidir entre:

1. **citação textual sem reprodução**;
2. **link ou referência bibliográfica**;
3. **reconstrução original do conceito**, sem copiar composição, traço, disposição, legenda ou expressão visual protegida;
4. **uso de trecho permitido**, apenas quando juridicamente defensável e documentalmente registrado;
5. **substituição por fonte aberta equivalente**.

O modelo pode estudar uma figura privada para compreender o mecanismo, mas o resultado final deve ser uma expressão original e auditável.

### 2.4 Geração por modelo

Usar quando:

- não existe imagem adequada;
- a imagem existente não mostra causalidade;
- é necessário integrar órgão, variável, curva e decisão;
- a cena precisa ser didaticamente impossível na fotografia;
- o módulo exige comparação contrafactual;
- a identidade visual da série precisa prevalecer sobre heterogeneidade de fontes.

Não usar geração como substituto automático de:

- radiologia real;
- curvas que podem ser desenhadas por código;
- fórmulas e números;
- telas técnicas que exigem fidelidade;
- anatomia em que uma fonte aberta validada é superior.

### 2.5 Visual determinístico

Preferir SVG, Canvas ou gráficos programáticos para:

- curvas pressão-tempo, fluxo-tempo e volume-tempo;
- loops pressão-volume e fluxo-volume;
- equação do movimento;
- decomposição resistiva e elástica;
- constantes de tempo;
- mecânica em dois compartimentos;
- comparação VCV × PCV;
- trigger, ciclagem e assincronias;
- tendências temporais;
- escalas, eixos, números e fórmulas.

Curva fisiológica não deve ser “artisticamente aproximada” quando pode ser matematicamente construída.

---

## 3. Matriz de decisão

| Necessidade | Fonte preferencial | Complemento | Evitar |
|---|---|---|---|
| reconhecer RX/TC | imagem clínica aberta ou própria | overlay próprio | radiologia inventada por IA |
| ensinar mecanismo microscópico | fonte aberta validada ou geração original | legenda vetorial | copiar figura de livro |
| comparar modos ventilatórios | SVG/Canvas determinístico | cena clínica gerada | telas falsas com números ilegíveis |
| mostrar circuito/equipamento | foto oficial licenciada ou própria | esquema vetorial | equipamento híbrido inexistente |
| ensinar assincronia | curva real ou simulada | paciente/circuito esquemático | curva decorativa |
| construir prancha editorial | composição híbrida | overlays determinísticos | colagem sem unidade |
| mostrar contexto humano | foto própria licenciada ou geração | silhueta esquemática | paciente identificável sem base legal |

---

## 4. Proveniência obrigatória

Nenhum ativo novo deve entrar sem registro de proveniência.

### 4.1 Manifesto mínimo por imagem

Manter um arquivo `assets/ventila/manifest.json` ou equivalente estruturado.

Campos mínimos:

```json
{
  "id": "v05-plate-01",
  "file": "assets/ventila/v05/v05-plate-01.webp",
  "module": "ventila05.html",
  "title": "VCV: variável controlada e custo oculto",
  "function": ["demonstrar", "comparar", "decidir"],
  "source_class": "generated|open-source|own-clinical|drive-reference|deterministic|hybrid",
  "source_title": null,
  "source_creator": null,
  "source_url": null,
  "license": "CC BY 4.0|CC0|public-domain|own|generated|reference-only|other",
  "license_url": null,
  "accessed_at": "YYYY-MM-DD",
  "original_file": null,
  "modifications": "crop, redrawing, overlay, annotation, recolor",
  "attribution_text": null,
  "patient_identifiable": false,
  "deidentification_checked": true,
  "clinical_review": "pending|approved|rejected",
  "visual_review": "pending|approved|rejected",
  "copyright_review": "pending|approved|rejected",
  "prompt_file": null,
  "generation_model": null,
  "generation_date": null,
  "notes": null
}
```

### 4.2 Classes de proveniência

- `open-source`: reutilização baseada em licença aberta explícita;
- `own-clinical`: imagem própria, desidentificada e com base de uso documentada;
- `drive-reference`: material privado consultado, não redistribuído;
- `generated`: imagem original produzida por modelo;
- `deterministic`: visual produzido por código;
- `hybrid`: composição com duas ou mais classes anteriores.

`drive-reference` nunca deve apontar para um arquivo copiado para `assets/` sem autorização específica.

---

## 5. Estrutura de diretórios proposta

```text
assets/ventila/
├── manifest.json
├── ATTRIBUTIONS.md
├── source-register.csv
├── shared/
│   ├── anatomy/
│   ├── equipment/
│   ├── radiology/
│   ├── waveforms/
│   └── icons/
├── v00/
├── v01/
├── ...
├── v29/
└── atlas/

prompts/ventila/
├── README.md
├── v00/
│   ├── brief.md
│   ├── critic-output.md
│   ├── generation-prompt.md
│   ├── negative-prompt.md
│   └── review.md
└── ...
```

Não armazenar livros completos, páginas escaneadas ou PDFs protegidos dentro do repositório público.

---

## 6. Pipeline de aquisição

### Etapa A — inventário do módulo

Para cada `ventilaNN.html`, extrair:

- tese;
- objetivos;
- conceitos causais;
- imagens existentes;
- Canvas/SVG existentes;
- lacunas de reconhecimento;
- lacunas de mecanismo;
- lacunas de decisão;
- risco de redundância.

### Etapa B — busca em quatro frentes

Executar em paralelo:

1. **fontes abertas públicas**;
2. **biblioteca privada do Google Drive**;
3. **ativos clínicos próprios ou já licenciados**;
4. **oportunidades de geração e visual determinístico**.

### Etapa C — mapa de cobertura

Para cada conceito, registrar:

| Conceito | Já coberto? | Fonte disponível | Licença | Qualidade | Ação |
|---|---|---|---|---|---|
| exemplo | parcial | figura aberta | CC BY | alta | adaptar e atribuir |
| exemplo | não | livro do Drive | referência privada | alta | redesenhar originalmente |
| exemplo | não | nenhuma | — | — | gerar por modelo |
| exemplo | parcial | curva em HTML | própria | média | reconstruir em SVG |

### Etapa D — seleção

Escolher a fonte pela combinação:

- verdade clínica;
- força didática;
- adequação jurídica;
- legibilidade;
- pertencimento editorial;
- possibilidade de manutenção;
- custo de integração.

### Etapa E — produção

- baixar ou materializar apenas o que pode ser legitimamente usado;
- preservar o original quando necessário para auditoria;
- produzir versões normalizadas;
- gerar arte original onde houver lacuna;
- aplicar texto, fórmulas e números deterministicamente;
- registrar proveniência e transformações.

### Etapa F — revisão

Quatro revisões independentes:

1. **científica**;
2. **visual/didática**;
3. **copyright/proveniência**;
4. **integração técnica e responsividade**.

---

## 7. Google Drive como biblioteca de referência

A busca no Drive deve ser orientada por conceito, não apenas por título de livro.

Consultas típicas:

- mechanical ventilation equation of motion;
- pressure controlled ventilation waveform;
- volume controlled ventilation decelerating flow;
- patient ventilator asynchrony double triggering;
- intrinsic PEEP flow time curve;
- stress index airway pressure;
- transpulmonary pressure esophageal manometry;
- recruitability and PEEP;
- driving pressure compliance;
- ARDS heterogeneity baby lung;
- mechanical power ventilator induced lung injury.

Para cada achado relevante no Drive, registrar:

- livro/documento;
- edição;
- capítulo;
- página;
- conceito encontrado;
- se há figura relevante;
- se a figura pode ou não ser reutilizada;
- qual reconstrução original seria necessária;
- qual fonte aberta equivalente deve ser procurada.

O Drive alimenta a compreensão e a auditoria; não elimina a obrigação de criar uma expressão visual própria.

---

## 8. Fontes abertas: critérios mínimos

Uma imagem aberta só é aprovada quando houver:

- autor ou instituição identificável;
- página de origem;
- licença explícita;
- compatibilidade da licença com o repositório;
- qualidade suficiente;
- ausência de dados pessoais indevidos;
- interpretação clínica correta;
- atribuição preparada.

### Licenças

Preferência prática:

1. domínio público / CC0;
2. CC BY;
3. CC BY-SA, após avaliar compatibilidade;
4. outras Creative Commons, apenas após verificar restrições;
5. uso meramente referencial quando não houver permissão de redistribuição.

Evitar ativos “free”, “royalty-free” ou “educational use” sem termos precisos e preservados.

---

## 9. Geração por modelo

Toda imagem gerada deve ter:

- brief clínico;
- referências visuais fornecidas ao modelo;
- declaração da tese visual;
- prompt usado;
- negative prompt;
- modelo e data;
- primeiro render preservado quando útil;
- crítica multimodal;
- correções executadas;
- aprovação científica.

### O modelo não deve inventar

- valores numéricos;
- nomes de modos;
- fórmulas;
- parâmetros de ventilador;
- anatomia incompatível;
- conexões de circuito impossíveis;
- radiologia diagnóstica;
- interfaces de equipamento apresentadas como reais.

### Divisão de trabalho

**Modelo de imagem:**

- anatomia esquemática;
- cena clínica não identificável;
- textura editorial;
- composição;
- relações espaciais;
- metáfora causal;
- integração visual entre painéis.

**Código/overlay:**

- textos;
- números;
- fórmulas;
- eixos;
- curvas precisas;
- tabelas;
- rótulos;
- escalas;
- símbolos técnicos.

---

## 10. Composição híbrida

A unidade visual do Ventila não virá de obrigar todas as fontes a parecerem iguais. Virá de uma moldura editorial consistente.

Elementos de normalização:

- proporção e margens;
- paleta semântica;
- títulos e numeração;
- contornos e setas;
- legendas;
- tratamento de recortes;
- molduras para radiologia e fotografia;
- escala de densidade;
- posição da conclusão;
- créditos discretos e acessíveis.

Uma radiografia deve continuar parecendo radiografia. Uma curva deve continuar matematicamente limpa. A unidade está na direção de arte, não na adulteração da natureza da fonte.

---

## 11. Lotes de trabalho

### Lote 1 — gramática mínima

Prioridade:

- V00 — contrato ventilatório;
- V03 — equação do movimento;
- V05 — VCV;
- V06 — PCV;
- V15 — comparação de modos/linguagem de curvas.

Objetivo: estabelecer a gramática de anatomia + ventilador + curva + decisão.

### Lote 2 — assinaturas e reconhecimento

- loops;
- auto-PEEP;
- assincronias;
- mecânica heterogênea;
- manobras e monitorização.

Objetivo: combinar curvas determinísticas, imagens clínicas e overlays.

### Lote 3 — dano, estratégia e casos

- VILI;
- driving pressure;
- potência mecânica;
- recrutamento;
- posição prona;
- casos integrativos.

Objetivo: mostrar benefício versus custo e decisões fenótipo-dependentes.

---

## 12. Entregável por módulo

Cada módulo deve terminar com:

1. inventário visual atual;
2. mapa de lacunas;
3. achados open-source;
4. achados bibliográficos do Drive;
5. decisão de reutilizar, adaptar, redesenhar, gerar ou codificar;
6. manifesto de proveniência;
7. pranchas e ativos produzidos;
8. overlays;
9. textos alternativos;
10. créditos;
11. revisão científica;
12. revisão visual;
13. teste desktop/mobile;
14. lista de pendências.

---

## 13. Gates de aprovação

Uma imagem só entra quando responde “sim” a todos os gates aplicáveis:

### Científico

- o mecanismo está correto?
- anatomia, direção e relações estão corretas?
- curvas e equipamentos são coerentes?

### Didático

- há uma pergunta ou tese visual?
- o aluno deduz algo olhando?
- a imagem reduz carga cognitiva em vez de aumentá-la?

### Jurídico

- a licença foi confirmada?
- a atribuição está completa?
- o ativo privado não foi redistribuído indevidamente?
- dados clínicos estão desidentificados?

### Editorial

- pertence ao Ventila?
- a fonte preserva sua natureza?
- a composição tem hierarquia e ritmo?

### Técnico

- arquivo otimizado?
- dimensões adequadas?
- fallback e `alt` presentes?
- responsivo?
- sem dependência externa frágil?

---

## 14. Regra final

O acervo visual do Ventila não será uma pasta de figuras encontradas.

Será uma **biblioteca clínica argumentada**, em que cada ativo possui:

- origem;
- licença;
- função;
- transformação;
- tese didática;
- revisão;
- lugar preciso na narrativa.

> Fontes abertas fornecem evidência reutilizável. Os livros do Drive fornecem profundidade e conferência. O código fornece precisão. O modelo fornece síntese visual inédita. A direção de arte transforma tudo isso em uma única obra.