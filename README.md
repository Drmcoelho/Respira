# Respira

Série didática de fisiologia respiratória e ventilação para pensar, não decorar.

## Módulos publicados

- `index.html` — capa da série, agora estruturada em 10 módulos e 4 fases.
- `mvp1.html` — como o ar entra e sai: via aérea, gradiente de pressão, diafragma, resistência, complacência e congestão.
- `mvp2.html` — saturar não é respirar bem: oxigenação, ventilação, curva O₂-Hb, monóxido, anemia e entrega de oxigênio.
- `mvp3.html` — onde o ar e o sangue se encontram: relação V/Q, shunt, espaço morto, resposta ao oxigênio, PEEP e recrutamento.
- `mvp4.html` — a gasometria como narrativa: pH, pCO₂, HCO₃⁻, compensação, fórmula de Winter, ânion-gap e bancada guiada.
- `assets/respira.css` — identidade visual e estilos compartilhados.

## Publicação no GitHub Pages

Configuração sugerida:

1. Abrir **Settings → Pages** no repositório.
2. Em **Build and deployment**, selecionar **Deploy from a branch**.
3. Escolher branch `main` e pasta `/root`.
4. Salvar.

Depois da propagação, a página deve ficar em:

`https://drmcoelho.github.io/Respira/`

## Observação técnica

A versão publicada é estática e sem JavaScript. O formato original em quiz por botões foi convertido para perguntas com resposta expansível (`details/summary`) para aumentar robustez, acessibilidade e compatibilidade com GitHub Pages. O Módulo 4 mantém uma bancada guiada de fórmulas e casos; a bancada calculadora em JavaScript não foi publicada por limitação de escrita do conector.
