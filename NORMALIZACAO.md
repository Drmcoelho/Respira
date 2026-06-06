# Respira · normalização de nomenclatura

## Objetivo

O projeto deixou de ser uma sequência de MVPs e passou a ser uma série didática utilizável como produto. Por isso, os nomes públicos dos módulos passam a seguir uma nomenclatura canônica, semanticamente estável e apropriada para exportação, manutenção, PDF e curso.

## Regra canônica

Formato:

```txt
modules/respira-NN-slug.html
```

Critérios:

- `respira` identifica a série.
- `NN` preserva ordenação lexical e didática.
- `slug` descreve o conteúdo, não a etapa histórica de desenvolvimento.
- arquivos `mvp*` permanecem como camada legada para não quebrar links antigos.

## Mapa Respira

| Nº | Título | Canônico | Legado |
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

## Manifesto de dados

O arquivo `data/respira-modules.json` é a fonte de referência para automações externas, incluindo geradores de PDF, auditoria de conteúdo e futura extração das questões para JSON.

## Estado atual da migração

Esta etapa criou wrappers canônicos em `/modules/` que carregam os arquivos legados existentes por meio de `assets/js/legacy-module-loader.js`.

Isso preserva o funcionamento atual, evita quebrar links antigos e permite que a página inicial use URLs limpas imediatamente.

## Próxima etapa recomendada

A migração ideal é extrair `const QUESTIONS` dos HTMLs para arquivos JSON próprios:

```txt
data/questions/respira-01.json
data/questions/respira-02.json
...
data/questions/respira-10.json
```

Depois disso:

- o quiz interativo consome JSON;
- o PDF consome o mesmo JSON;
- o gabarito deixa de depender de parsing de JavaScript dentro de HTML;
- o conteúdo passa a ter uma única fonte de verdade.

## Política de legado

Não apagar `mvp*` até que:

1. todos os links externos tenham sido substituídos;
2. o PDF tenha sido gerado a partir dos JSONs;
3. a navegação interna tenha sido testada no GitHub Pages;
4. os wrappers canônicos estejam estáveis.
