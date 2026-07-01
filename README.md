# Respira / Ventila

Série didática de fisiologia respiratória e ventilação mecânica para pensar, não decorar.

O projeto é dividido em duas partes:

- **Respira** — fisiologia respiratória, oxigenação, relação V/Q, gasometria, síndromes, terapêutica, suporte não invasivo e fundamentos de ventilação.
- **Ventila** — ventilação mecânica aplicada, em progressão socrática, visual, interativa e clinicamente ancorada.

A tese editorial é simples: **mecanismo antes de protocolo**. Cada módulo deve ensinar a ler a fisiologia que aparece na tela, no monitor, na curva, no tubo, no pulmão e na decisão clínica.

## Estado atual

### Respira

A Parte A possui 10 módulos interativos, publicados como HTML estático:

| Nº | Arquivo legado | Canônico opcional | Tema |
|---:|---|---|---|
| 01 | `mvp1-interativo.html` | `modules/respira-01-mecanica.html` | Mecânica: resistência, complacência, constante de tempo, auto-PEEP |
| 02 | `mvp2-interativo.html` | `modules/respira-02-oxigenacao.html` | Oxigenação, curva O₂-Hb, conteúdo arterial e entrega |
| 03 | `mvp3-interativo.html` | `modules/respira-03-vq-shunt-espaco-morto.html` | V/Q, shunt, espaço morto, resposta ao oxigênio |
| 04 | `mvp4-interativo.html` | `modules/respira-04-gasometria.html` | Gasometria como narrativa: pH, CO₂, HCO₃⁻, Winter, ânion-gap |
| 05 | `mvp5-interativo.html` | `modules/respira-05-arquitetura-pulmonar.html` | Laplace, surfactante, recrutamento e PEEP |
| 06 | `mvp6-interativo.html` | `modules/respira-06-sindromes.html` | Grandes síndromes respiratórias |
| 07 | `mvp7-interativo.html` | `modules/respira-07-terapeutica.html` | Terapêutica como forças sobre eixos fisiológicos |
| 08 | `mvp8-interativo.html` | `modules/respira-08-oxigenio-suporte-nao-invasivo.html` | Oxigênio e suporte não invasivo |
| 09 | `mvp9-interativo.html` | `modules/respira-09-ventilacao-mecanica-fundamentos.html` | VM fundamentos: equação do movimento, VCV/PCV, ondas, pausa, auto-PEEP |
| 10 | `mvp10-interativo.html` | `modules/respira-10-ventilacao-protetora-desmame.html` | Ventilação protetora e desmame |

### Ventila

A Parte B está organizada em `ventila.html` e módulos `ventila0.html` a `ventila26.html`, na raiz do repositório.

| Nº | Arquivo | Tema |
|---:|---|---|
| 00 | `ventila0.html` | Gramática da máquina, contrato dos modos, variável livre, tempo de ciclo e área do fluxo |
| 01 | `ventila1.html` | Por que este paciente está no ventilador? |
| 02 | `ventila2.html` | Máquina, circuito, tubo e paciente |
| 03 | `ventila3.html` | Curvas I: pressão, fluxo e volume |
| 04 | `ventila4.html` | Curvas II: loops pressão-volume e fluxo-volume |
| 05 | `ventila5.html` | VCV profundamente: volume é promessa, pressão é consequência |
| 06 | `ventila6.html` | PCV profundamente: pressão por tempo, volume como consequência |
| 07 | `ventila7.html` | Modos híbridos, adaptativos e PRVC |
| 08 | `ventila8.html` | PSV, CPAP, SIMV e trabalho respiratório |
| 09 | `ventila9.html` | Assincronias paciente-ventilador |
| 10 | `ventila10.html` | Sedação e bloqueio neuromuscular: esforço entre P-SILI e atrofia |
| 11 | `ventila11.html` | Fenótipos → plano: “intubado” não é diagnóstico |
| 12 | `ventila12.html` | Desmame, extubação e falha: os dois portões |
| 13 | `ventila13.html` | Traqueostomia como plataforma de desmame + Mega Revisão Parte 1 |
| 14 | `ventila14.html` | Aplicação integrada: o pulmão na tela + Mega Revisão Parte 2 |
| 15 | `ventila15.html` | Tutor visual PSV · VCV · PCV: consolidação dos modos e inversão causal |
| 16 | `ventila16.html` | Tutor adaptativo de sessão: BKT, grafo de pré-requisitos e remediação dirigida |
| 17 | `ventila17.html` | SDRA — recrutabilidade antes da PEEP: PEEP só compra pulmão quando recrutamento supera hiperdistensão e custo hemodinâmico. |
| 18 | `ventila18.html` | Obstrutivo grave — dar tempo para sair: Resistência, constante de tempo, auto-PEEP e hipercapnia permissiva sem perseguir números com FR lesiva. |
| 19 | `ventila19.html` | Coração-pulmão — o VD no ventilador: Retorno venoso, resistência vascular pulmonar e septo: a pressão positiva vista pelo ventrículo direito. |
| 20 | `ventila20.html` | Neuroventilação — CO₂ também é hemodinâmica: PaCO₂, fluxo cerebral, PIC e o preço isquêmico da hiperventilação mantida. |
| 21 | `ventila21.html` | Prona e resgate — redistribuir antes de escalar: Posição como terapia da heterogeneidade: V/Q, estresse regional e resposta que vai além da SpO₂. |
| 22 | `ventila22.html` | APRV — abrir sem aprisionar: Phigh/Plow não bastam: T-high, T-low e terminação do fluxo governam recrutamento e ventilação. |
| 23 | `ventila23.html` | ECMO e ECCO₂R — quando a máquina compra proteção: Fluxo, sweep, referência precoce e ultraprotação: suporte extracorpóreo como ponte, não cura. |
| 24 | `ventila24.html` | Obesidade, gestação e abdome — a parede pesa: Complacência do sistema não é complacência pulmonar: parede e abdome mudam a leitura das pressões. |
| 25 | `ventila25.html` | Pediatria e neonatologia — pulmão pequeno, tempo curto: Tubo estreito, vazamento, volume garantido e a física específica do recém-nascido e da criança. |
| 26 | `ventila26.html` | Fora da UTI — transporte e contingência: Oxigênio, bateria, circuito, fixação e plano B: robustez operacional faz parte da ventilação. |
| 27 | `ventila27.html` | Pulmão restritivo — ventilar pequeno e duro: baixa complacência, driving alto, baixa reserva; o baby lung pouco recrutável. |
| 28 | `ventila28.html` | Pulmão misto — não entra, não sai, não cabe: obstrução + restrição, qual componente mata primeiro neste minuto. |
| 29 | `ventila29.html` | Ocupacional na UTI — o pulmão ferido do trabalho: anamnese, imagem, função, gasometria e estratégia ventilatória costuradas. |

## Contrato arquitetural atual

A decisão atual do projeto é: **HTML single-file autocontido é a fonte canônica publicada**.

Isso é intencional. Cada módulo deve abrir diretamente no navegador, sem build obrigatório, sem servidor, sem fetch, sem backend, sem toolchain e sem dependência de pipeline. A propriedade central é: **abrir o `.html` e funcionar**.

O projeto não é um app SaaS. É um conjunto de instrumentos didáticos portáteis. A robustez operacional vale mais do que elegância abstrata de manutenção.

Consequências práticas:

- não introduzir build step obrigatório;
- não exigir bundler;
- não separar CSS/JS se isso tornar o arquivo publicado dependente de pipeline;
- não trocar autonomia por DRY prematuro;
- não remover conteúdo para “limpar” ou “compactar”;
- nunca reduzir módulos robustos: **somente corrigir, ampliar ou restaurar**;
- preservar rotas antigas e deep-links funcionais;
- aceitar duplicação quando ela compra antifragilidade.

Duplicação em HTML autocontido é custo latente de manutenção, não defeito ativo. Só se torna problema real se houver mudanças compartilhadas frequentes. Enquanto os módulos estiverem fechados e validados, a regra é: **não mexer no que funciona para satisfazer estética de arquitetura**.

## Publicação no GitHub Pages

Configuração sugerida:

1. Abrir **Settings → Pages** no repositório.
2. Em **Build and deployment**, selecionar **Deploy from a branch**.
3. Escolher branch `main` e pasta `/root`.
4. Salvar.

Página principal:

```txt
https://drmcoelho.github.io/Respira/
```

Índice Ventila:

```txt
https://drmcoelho.github.io/Respira/ventila.html
```

## Política de alteração

Antes de alterar qualquer módulo:

1. preservar integralmente o conteúdo existente;
2. corrigir falhas sem reduzir escopo;
3. ampliar quando necessário;
4. manter o arquivo autocontido;
5. testar sintaxe e runtime básico;
6. confirmar links relativos;
7. manter a caixa de honestidade do modelo;
8. manter o rodapé autoral e a dedicatória discreta quando presentes.

A regra editorial final é: **não amputar complexidade clínica para produzir limpeza visual ou manutenção aparente**. O material existe para ensinar raciocínio, não para parecer minimalista.
