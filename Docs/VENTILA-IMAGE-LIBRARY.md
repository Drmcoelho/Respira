# VENTILA-IMAGE-LIBRARY.md — Acervo visual, fontes e proveniência

> Escopo: imagens para os módulos `ventila00.html`–`ventila29.html`, Atlas Ventila e materiais transversais.
>
> Relação normativa: este documento complementa `CODEX.md` e `Docs/CODEX-VISION.md`.

## 0. Tese

Ventilação mecânica não pode ser ensinada por uma única classe de imagem.

O Ventila precisa combinar, conforme a pergunta didática:

1. **imagem clínica real** — radiografia, tomografia, fotografia de equipamento, tela de ventilador, circuito e contexto de leito;
2. **figura científica licenciada** — anatomia, fisiologia, mecânica, curvas e esquemas provenientes de fontes abertas confiáveis;
3. **referência bibliográfica privada** — livros e documentos legitimamente acessíveis no Google Drive do autor, usados para compreensão, auditoria e reconstrução original;
4. **visual computacional determinístico** — SVG, Canvas, gráficos e simuladores produzidos por código;
5. **imagem original gerada por modelo** — cenas, cortes esquemáticos, metáforas causais e pranchas editoriais inexistentes nas fontes;
6. **composição híbrida** — fotografia ou radiologia real integrada a diagramas, setas, curvas e overlays próprios.

O inventário canônico e executável está em `assets/ventila/manifest.yml`. Ele enumera V00–V29 e X01–X02, ativos requeridos, destinos, referências, método de produção e estado.

## 1. Hierarquia de escolha

Para cada necessidade visual, escolher a fonte nesta ordem:

1. ativo próprio já existente e cientificamente adequado;
2. fonte aberta primária ou institucional com licença verificável;
3. figura científica aberta cuja licença permita a reutilização pretendida;
4. reconstrução vetorial determinística baseada em mecanismo;
5. geração original por modelo;
6. composição híbrida.

Não usar geração por modelo para substituir, fingir ou aproximar de forma hiper-realista uma evidência diagnóstica que deveria ser real.

## 2. Regra de licenciamento

Imagem pública não é automaticamente imagem aberta. Livro disponível no Google Drive não é automaticamente redistribuível.

Antes de incorporar qualquer arquivo externo, registrar:

- autor ou instituição;
- URL ou identificador persistente;
- licença exata;
- data de consulta;
- exigência de atribuição;
- permissão para modificação;
- permissão para redistribuição;
- transformação realizada;
- módulo e função didática.

Sem licença verificável, o material pode servir como referência científica e visual privada, mas não deve ser copiado para o repositório.

## 3. Google Drive: biblioteca privada de referência

Referências centrais já localizadas:

- `Pilbeams Mechanical Ventilation 8th ed 2024.pdf`;
- `Pilbeam's Mechanical Ventilation — Physiological and Clinical Applications, 6e.pdf`;
- `mechanical-ventilation-physiology-an-practice-book.pdf`.

Usos permitidos no fluxo editorial:

- conferir mecanismos;
- comparar terminologia e representações;
- identificar erros em storyboards;
- compreender curvas, loops, modos e circuitos;
- inspirar reconstruções originais sem copiar composição, texto ou figura.

Não extrair figuras para publicação sem licença ou autorização específica.

## 4. Fontes abertas iniciais

O manifesto registra fontes abertas ou potencialmente reutilizáveis já localizadas:

- OpenStax para anatomia e mecânica respiratória;
- CDC Public Health Image Library para radiografias em domínio público;
- Wikimedia Commons para esquemas e curvas com licença individual verificável;
- artigos do PubMed Central como referência científica, observando que a licença pode variar por artigo e figura.

A licença deve ser confirmada na página do ativo, não inferida pelo domínio.

## 5. Matriz de decisão

| Conteúdo | Fonte preferencial | Motivo |
|---|---|---|
| radiografia/TC diagnóstica | imagem clínica aberta ou própria | fidelidade morfológica |
| anatomia básica | OpenStax ou redesenho original | reutilização e consistência |
| curvas e loops | SVG/Canvas determinístico | precisão temporal e geométrica |
| telas de ventilador | interface genérica codificada | evita marca e números inventados |
| circuitos | esquema vetorial próprio | causalidade e legibilidade |
| cenas de UTI/transporte | geração original | anonimato e direção de arte |
| metáforas mecânicas | geração original + overlay | integração pedagógica |
| fórmulas, escalas e rótulos | overlay vetorial | texto exato e acessível |
| figuras de livros privados | referência, não reprodução | direito autoral |

## 6. Pipeline por módulo

1. Ler o HTML canônico e o storyboard no `CODEX.md`.
2. Consultar `assets/ventila/manifest.yml`.
3. Auditar imagens existentes no repositório.
4. Consultar as referências privadas pertinentes.
5. Buscar fontes abertas com licença verificável.
6. Construir curvas, loops, fórmulas e interfaces em código.
7. Gerar a arte-base original necessária.
8. Aplicar overlay determinístico em português.
9. Revisar ciência, causalidade, estética, acessibilidade, licença e integração.
10. Atualizar o manifesto com estado, hash, crédito e revisão.

## 7. Estados permitidos

- `search`: fonte ainda não escolhida;
- `planned`: ativo especificado, ainda não produzido;
- `acquired`: arquivo externo obtido e licença registrada;
- `generated`: arte-base criada;
- `coded`: SVG/Canvas/gráfico determinístico criado;
- `reviewed`: revisão científica e visual concluída;
- `integrated`: incorporado ao HTML e validado;
- `blocked-license`: fonte adequada, mas sem autorização de uso;
- `rejected`: ativo recusado por erro científico, visual, jurídico ou técnico.

## 8. Estrutura de diretórios

```text
assets/ventila/
├── manifest.yml
├── atlas/
├── base/
├── overlays/
├── curves/
├── radiology/
├── equipment/
├── sources/
└── rejects/
```

## 9. Proibições

- copiar figura de livro privado para o site;
- baixar imagem de busca e presumir que é livre;
- apagar crédito ou licença;
- usar radiologia sintética como se fosse caso real;
- permitir que modelo de imagem invente eixos, números, curvas ou fórmulas;
- reproduzir interface proprietária de ventilador;
- misturar fontes incompatíveis sem normalização editorial;
- publicar paciente identificável;
- usar imagem decorativa sem função causal.

## 10. Gate de proveniência

Nenhum ativo externo pode chegar ao HTML publicado sem:

- entrada no manifesto;
- fonte persistente;
- licença verificada;
- crédito pronto para publicação;
- registro das alterações;
- revisão de ausência de identificação do paciente;
- confirmação de que a imagem suporta a tese do módulo.

## 11. Gate para geração por modelo

Toda arte gerada deve registrar:

- módulo e tese;
- prompt utilizado;
- modelo e data;
- referências visuais fornecidas;
- revisão anatômica;
- revisão fisiológica;
- correções realizadas;
- declaração explícita de que não é imagem diagnóstica real quando aplicável.

## 12. Definição de conclusão

O acervo não estará concluído quando houver simplesmente uma imagem para cada módulo. Estará concluído quando cada V00–V29 possuir:

- prancha editorial própria;
- curvas e interfaces precisas quando necessárias;
- evidência radiológica real ou esquema explicitamente identificado;
- origem e licença documentadas;
- overlay legível;
- alt text;
- revisão científica e visual;
- integração responsiva no site;
- coerência com o restante do Atlas.
