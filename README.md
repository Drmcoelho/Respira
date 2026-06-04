# Respira

Série didática de fisiologia respiratória e ventilação — para **pensar, não decorar**.
Raciocínio socrático, da física do ar que entra até a ventilação mecânica à beira do leito.
Material livre para usar, compartilhar e ensinar.

## Estrutura da série

São **10 módulos** organizados em **4 fases**. Atualmente **6 estão publicados**; os
módulos 7–10 aparecem como "em breve" no índice.

| # | Módulo | Página canônica |
|---|--------|-----------------|
| 01 | Como o ar entra e sai — mecânica, resistência × complacência, simulador | `mvp1-interativo.html` |
| 02 | Saturar não é respirar bem — oxigenação × ventilação, curva O₂-Hb | `mvp2-interativo.html` |
| 03 | Onde o ar e o sangue se encontram — V/Q, shunt, espaço morto | `mvp3-interativo.html` |
| 04 | A gasometria como narrativa — pH, pCO₂, HCO₃⁻, Winter, ânion-gap | `mvp4-interativo.html` |
| 05 | A arquitetura que respira — surfactante, complacência, Laplace | `mvp5-interativo.html` |
| 06 | As grandes síndromes — SDRA, DPOC, asma, edema, fibrose por mecanismo | `mvp6-interativo.html` |

- `index.html` — capa da série, manifesto e os cards dos 10 módulos.
- `ideia.html` — a filosofia por trás da série.
- `assets/respira.css` — folha de estilo compartilhada (usada pela versão estática do Módulo 4).

## Convenções de arquivos

- `mvpN-interativo.html` — **versão canônica** de cada módulo: trilha de quiz com feedback
  por mecanismo e, na maioria dos módulos, um simulador interativo em JavaScript. É para
  onde o `index.html` aponta.
- `mvpN.html` — **redirect** para a versão canônica, existente para os módulos 1, 2, 3,
  5 e 6. Todos **preservam o `location.hash`** ao redirecionar, para que deep-links na
  forma curta (`mvp3.html#s=42&d=35&...`) cheguem ao laboratório no estado certo — a
  "Sala das síndromes" do Módulo 6 usa esse mecanismo para reabrir os labs dos módulos 1–5.
- `mvp4.html` — exceção: no lugar do stub há a **versão estática legada** (sem JavaScript,
  com perguntas em `details/summary`), mantida como alternativa robusta e como referência.

## Interatividade

Diferente das primeiras iterações estáticas, os módulos canônicos usam JavaScript:
trilhas de quiz com alternativas embaralhadas e feedback imediato, e simuladores
(mecânica respiratória, curva O₂-Hb, laboratório de V/Q, bancada de gasometria,
laboratório de Laplace). O Módulo 6 costura a série reabrindo esses laboratórios no
estado exato de cada síndrome.

## Publicação no GitHub Pages

O deploy é automático via GitHub Actions: o workflow `.github/workflows/pages.yml`
publica o conteúdo a cada push na branch `main` (e pode ser disparado manualmente em
**Actions → Deploy Respira to GitHub Pages → Run workflow**).

Para isso funcionar, em **Settings → Pages → Build and deployment**, a origem deve
estar como **GitHub Actions**.

Depois da propagação, a página fica em:

`https://drmcoelho.github.io/Respira/`

## Autoria

Dr. Matheus M. Coelho · CRM-SP 151.318 · Limeira.
