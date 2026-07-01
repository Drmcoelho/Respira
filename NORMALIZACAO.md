# Respira / Ventila · normalização de nomenclatura

## Objetivo

Este arquivo documenta a nomenclatura pública e a política de compatibilidade do projeto.

A normalização existe para tornar os caminhos legíveis e semanticamente estáveis, sem quebrar links antigos e sem enfraquecer a propriedade mais importante do projeto: **cada módulo publicado deve continuar funcionando como HTML autocontido**.

## Regra-mãe atual

**O HTML publicado é a fonte canônica funcional.**

Wrappers, aliases, índices e arquivos de dados auxiliares podem existir para navegação, documentação, auditoria ou exportação futura. Eles não substituem o artefato principal se criarem dependência de build, fetch, loader ou pipeline.

Em outras palavras:

```txt
abre o .html → funciona
```

é mais importante do que:

```txt
não repetir CSS/JS nunca
```

Duplicação aceita em módulo fechado não é erro ativo; é o custo deliberado da autonomia.

## Respira

Respira nasceu com nomes históricos `mvp*`. Eles permanecem por compatibilidade.

Formato canônico opcional:

```txt
modules/respira-NN-slug.html
```

Critérios:

- `respira` identifica a Parte A;
- `NN` preserva ordenação lexical e didática;
- `slug` descreve o conteúdo, não a etapa histórica de desenvolvimento;
- arquivos `mvp*` permanecem vivos para não quebrar links antigos;
- wrappers em `/modules/` são camada de conveniência, não obrigação arquitetural.

## Mapa Respira

| Nº | Título | Canônico opcional | Legado |
|---:|---|---|---|
| 01 | Como o ar entra e sai | `modules/respira-01-mecanica.html` | `mvp1-interativo.html` |
| 02 | Saturar não é respirar bem | `modules/respira-02-oxigenacao.html` | `mvp2-interativo.html` |
| 03 | Onde o ar e o sangue se encontram | `modules/respira-03-vq-shunt-espaco-morto.html` | `mvp3-interativo.html` |
| 04 | A gasometria como narrativa | `modules/respira-04-gasometria.html` | `mvp4-interativo.html` |
| 05 | A arquitetura que respira | `modules/respira-05-arquitetura-pulmonar.html` | `mvp5-interativo.html` |
| 06 | As grandes síndromes | `modules/respira-06-sindromes.html` | `mvp6-interativo.html` / `mvp6.html` |
| 07 | A terapêutica — as forças | `modules/respira-07-terapeutica.html` | `mvp7-interativo.html` / `mvp7.html` |
| 08 | Oxigênio e suporte não invasivo | `modules/respira-08-oxigenio-suporte-nao-invasivo.html` | `mvp8-interativo.html` / `mvp8.html` |
| 09 | Ventilação mecânica — os fundamentos | `modules/respira-09-ventilacao-mecanica-fundamentos.html` | `mvp9-interativo.html` / `mvp9.html` |
| 10 | Ventilação protetora e desmame | `modules/respira-10-ventilacao-protetora-desmame.html` | `mvp10-interativo.html` / `mvp10.html` |

## Respira · Ponte Funcional

Sub-série **aditiva** entre a arquitetura (Respira 05) e as síndromes (Respira 06). Não renumera nem substitui a matriz 01–10; entra como uma camada própria, com slug semântico na raiz (mesma regra-mãe: o HTML autocontido é a fonte canônica).

| Nº | Título | Arquivo (raiz, canônico) |
|---:|---|---|
| RF-01 | Volumes e capacidades | `respira-ponte-01-volumes-capacidades.html` |
| RF-02 | Espirometria | `respira-ponte-02-espirometria.html` |
| RF-03 | Padrões funcionais | `respira-ponte-03-padroes.html` |
| RF-04 | DLCO e troca | `respira-ponte-04-dlco.html` |

Ordem de leitura: Respira 01–05 → **Ponte Funcional** → **Respira Ocupacional** → Respira 06 (síndromes) → 07–10. No índice, a Ponte e o bloco Ocupacional aparecem como seções próprias entre os cards 05 e 06.

## Respira · Ocupacional

Bloco **aditivo**, lido após a Ponte Funcional e antes das síndromes. Foco na realidade ocupacional brasileira (sub-representada na literatura de referência). Arquivos na raiz com slug semântico; nada renumerado.

| Nº | Título | Arquivo (raiz, canônico) |
|---:|---|---|
| RO-01 | Profissão como sinal vital | `respira-ocupacional-01-profissao-sinal-vital.html` |
| RO-02 | Poeiras minerais | `respira-ocupacional-02-poeiras-minerais.html` |
| RO-03 | Pulmão rural e biomassa | `respira-ocupacional-03-rural-biomassa.html` |
| RO-04 | Solda, tinta e asma ocupacional | `respira-ocupacional-04-asma-ocupacional.html` |

## Ventila

Ventila usa os arquivos de raiz como canônicos publicados:

```txt
ventila.html
ventila0.html
ventila1.html
...
ventila15.html
...
ventila29.html
```

A decisão atual é **não mover Ventila para uma arquitetura dependente de `/modules/` nem de build obrigatório**.

Pode haver no futuro aliases canônicos como:

```txt
modules/ventila-00-gramatica-da-maquina.html
modules/ventila-15-tutor-psv-vcv-pcv.html
```

Mas eles só devem ser criados se forem wrappers estáticos ou redirecionamentos compatíveis, sem quebrar a regra principal:

```txt
arquivo publicado autocontido continua abrindo sozinho
```

## Política de legado

Não apagar arquivos legados até que:

1. todos os links internos tenham sido auditados;
2. os links externos antigos tenham sido preservados por alias ou wrapper;
3. a navegação no GitHub Pages tenha sido testada;
4. a mudança não reduza a robustez offline;
5. o arquivo antigo não seja mais necessário para materiais compartilhados.

## Política sobre JSON, loaders e extração futura

A extração de questões para JSON, a criação de manifestos de dados ou a geração de PDFs podem ser úteis como camadas auxiliares.

Mas não são prioridade arquitetural enquanto criarem uma segunda fonte de verdade ou exigirem pipeline.

Status atual:

- `data/respira-modules.json` pode servir para auditoria, navegação ou ferramentas externas;
- loaders/wrappers podem preservar compatibilidade;
- JSON de questões pode ser estudado no futuro;
- nada disso deve substituir o HTML autocontido já validado;
- qualquer extração deve ser **lossless**: nunca reduzir, nunca resumir, nunca apagar nuances clínicas.

## Política de alteração

A normalização só é aceitável se obedecer a quatro travas:

1. **compatibilidade:** links antigos continuam funcionando;
2. **autocontenção:** o módulo publicado abre sozinho;
3. **não redução:** conteúdo clínico/didático não é compactado;
4. **auditabilidade:** a mudança deixa claro qual arquivo é canônico e qual é alias.

A pergunta de decisão não é “há duplicação?”. Há. A pergunta correta é:

> Esta mudança aumenta a robustez do artefato publicado ou apenas satisfaz elegância de manutenção abstrata?

Se for apenas elegância, não fazer.
