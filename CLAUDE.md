# CLAUDE.md — Projeto Respira / Ventila

> Manual operacional para qualquer instância de Claude, humano ou agente que trabalhe neste repositório.
>
> Leia antes de editar. Este arquivo deve refletir o estado real do projeto, não uma arquitetura idealizada.

## 0. TL;DR operacional

1. **Não reduzir.** Só corrigir, ampliar, restaurar ou refinar sem perda.
2. **HTML single-file é fonte canônica publicada.** Cada módulo deve abrir sozinho no navegador.
3. **Não introduzir build obrigatório.** Sem bundler, sem pipeline, sem etapa que alguém possa esquecer de rodar.
4. **Não transformar autonomia em DRY prematuro.** Duplicação em módulo fechado é custo latente, não defeito ativo.
5. **Ventila agora vai até 26.** Não voltar para a matriz antiga de 12 módulos.
6. **Sempre preservar links antigos.** Não quebrar `mvp*`, `ventilaN.html`, `ventila.html` ou deep-links Respira↔Ventila.
7. **Mecanismo antes de protocolo.** Curva, pulmão, tubo, drive e decisão clínica precisam conversar.
8. **Material didático, não prescrição.** Toda estimativa clínica precisa de caixa de honestidade quando aplicável.

## 1. Identidade e proveniência

- **Autor:** Dr. Matheus M. Coelho · CRM-SP 151.318 · Limeira/SP.
- **Dedicatória recorrente:** “Para a Dani”, discreta, no rodapé ou fecho.
- **Intenção:** livre para usar, compartilhar e ensinar.
- **Parte A:** Respira — fisiologia respiratória.
- **Parte B:** Ventila — ventilação mecânica aplicada.

URL pública principal:

```txt
https://drmcoelho.github.io/Respira/
```

Índice Ventila:

```txt
https://drmcoelho.github.io/Respira/ventila.html
```

## 2. Tese editorial

> **Ventilar é governar uma interação entre paciente, máquina, tubo, pulmão, drive neural, fármacos e tempo. O ventilador não é tratamento; é uma intervenção mecânica que compra tempo, transfere trabalho, impõe energia e cria riscos.**

A série deve ensinar o aluno a perguntar:

```txt
por que está na máquina?
→ o que a máquina controla?
→ o que varia como consequência?
→ o paciente está sincronizado ou lutando?
→ a sedação trata sofrimento/drive ou mascara erro mecânico?
→ o pulmão está protegido ou ferido?
→ já dá para devolver o trabalho?
```

Não pode virar apostila de modos. Modo ventilatório sem fisiologia vira catecismo de botão.

## 3. Decisão arquitetural definitiva por enquanto

### 3.1 O que foi decidido

O projeto deve privilegiar **artefatos autossuficientes**:

```txt
um arquivo .html → abre → funciona
```

Essa decisão é mais importante do que DRY, build limpo, separação elegante ou pipeline moderno.

Motivo: o material é feito para compartilhamento, ensino, UPA, iPhone, Windows alheio, GitHub Pages, arquivo salvo, uso offline e longevidade. Um build step não melhora o que a Dani vê. Pior: pode criar divergência entre fonte e publicado.

### 3.2 O que NÃO fazer

Não propor como padrão:

- `build.mjs` obrigatório;
- bundler;
- SPA;
- dependência de servidor;
- módulos JS externos obrigatórios para runtime;
- CSS externo obrigatório para Ventila;
- JSON como fonte única de verdade se isso enfraquecer o HTML publicado;
- extração de conteúdo que resuma, compacte ou apague nuances.

### 3.3 O que pode existir

Pode existir como camada auxiliar:

- snippet local de referência;
- script de validação;
- manifestos para auditoria;
- wrappers canônicos compatíveis;
- geradores de PDF;
- JSON exportado de forma lossless;
- scripts locais não obrigatórios.

Mas nada disso substitui o HTML publicado como fonte funcional.

## 4. Herança do Respira

Respira possui 10 módulos interativos. Eles são a fisiologia de base que Ventila reaproveita por deep-link.

| Arquivo | Conteúdo | Uso em Ventila |
|---|---|---|
| `mvp1-interativo.html` | Mecânica: R, C, τ, auto-PEEP | Ventila 3, 6, 8, 9, 14, 15 |
| `mvp2-interativo.html` | O₂-Hb, saturação, conteúdo, entrega | Oxigenação e entrega |
| `mvp3-interativo.html` | V/Q, shunt, espaço morto, resposta ao O₂ | Ventila 11, 14 |
| `mvp4-interativo.html` | Gasometria, Winter, AG, Δ-Δ | Hipercapnia permissiva, casos |
| `mvp5-interativo.html` | Laplace, surfactante, recrutamento, PEEP | Ventila 4, 5, 14 |
| `mvp6-interativo.html` | Síndromes | Fenótipos e salas de decisão |
| `mvp7-interativo.html` | Terapêutica como forças | Linguagem de alavancas |
| `mvp8-interativo.html` | O₂ e suporte não invasivo | Ventila 8 |
| `mvp9-interativo.html` | VM fundamentos: equação do movimento, VCV/PCV, ondas | Ventila 3, 5, 6, 15 |
| `mvp10-interativo.html` | Protetora, mechanical power, desmame | Ventila 10, 12, 13 |

Deep-links conhecidos:

```txt
mvp1  #r= c= rr=                       &m=sim
mvp2  #pao2= p50= hb= co=              &m=curve
mvp3  #s= d= f= c=                     &m=lab
mvp4  #ph= co2= hco3= na= cl= alb=     &m=bench
mvp5  #ra= rb= peep= surf=             &m=lab
mvp9  #lab
mvp10 #lab | #proteger | #desmamar
```

Use esses links quando o Ventila precisar apontar de volta para a fisiologia base.

## 5. Matriz atual do Ventila

| Nº | Arquivo | Tese / função | Motor visual principal |
|---:|---|---|---|
| 00 | `ventila0.html` | Gramática da máquina; variável controlada, variável livre, tempo e fluxo | contrato dos modos |
| 01 | `ventila1.html` | A causa do tubo vem antes do modo | mapa de falhas |
| 02 | `ventila2.html` | Máquina, circuito, tubo, via aérea ou pulmão? | circuito e tubo |
| 03 | `ventila3.html` | Curvas P/F/V são semiologia | ondas em tempo real |
| 04 | `ventila4.html` | Loops revelam relações que valores isolados escondem | loops P-V / F-V |
| 05 | `ventila5.html` | VCV: volume é promessa; pressão denuncia | volume-alvo e pressão consequente |
| 06 | `ventila6.html` | PCV: pressão é promessa; volume denuncia | pressão por tempo |
| 07 | `ventila7.html` | PRVC/adaptativo é controlador, não médico | algoritmo perseguindo alvo |
| 08 | `ventila8.html` | PSV/CPAP/SIMV dividem trabalho | paciente × máquina |
| 09 | `ventila9.html` | Assincronia é desencontro temporal | drive neural × entrega |
| 10 | `ventila10.html` | Esforço entre P-SILI e atrofia; BNM exige sedação real | Pmus, ΔPL, VIDD |
| 11 | `ventila11.html` | “Intubado” não é diagnóstico | classificador fenotípico |
| 12 | `ventila12.html` | Desmame é respirar; extubação é respirar e proteger | SBT e dois portões |
| 13 | `ventila13.html` | Traqueostomia é plataforma, não cura | tubo, Poiseuille, decanulação |
| 14 | `ventila14.html` | O pulmão na tela: shunt, recrutamento, hiperdistensão, auto-PEEP | campo alveolar |
| 15 | `ventila15.html` | PSV · VCV · PCV: inversão causal e leitura de curvas | tutor comparativo multimodal |

## 6. Fórmulas e motores — invariantes

Unidades preferenciais:

- C em L/cmH₂O quando cálculo interno exigir;
- C em mL/cmH₂O na UI quando mais intuitivo;
- fluxo em L/s;
- VT em L ou mL conforme contexto, deixando explícito;
- pressão em cmH₂O;
- tempo em s;
- RR em incursões/min.

Fórmulas centrais:

```txt
Paw(t) = PEEP + V(t)/C + R·V̇(t)
τ = R·C
```

VCV, fluxo constante:

```txt
Ti = VT / fluxo
Ppico = PEEP + VT/C + R·fluxo
Pplatô = PEEP + VT/C
Ppico − Pplatô = R·fluxo
Pplatô − PEEP = VT/C
```

PCV / PSV, pressão aplicada com fluxo decelerante:

```txt
VT = ΔP·C·(1 − e^(−Ti/τ))
fluxo(t) = (ΔP/R)·e^(−t/τ)
```

Auto-PEEP didático:

```txt
Te < ~3τ → esvaziamento incompleto → volume residual → auto-PEEP estimada
```

Trabalho resistivo de tubo:

```txt
R ∝ L/d⁴
```

Desmame:

```txt
RSBI = FR / VT(L)
```

Todas as fórmulas clínicas em UI devem vir acompanhadas de uma declaração de simplificação quando houver risco de interpretação prescritiva.

## 7. Padrão estrutural dos módulos

Um módulo Ventila típico deve conter:

1. **Caso clínico em cinco atos.**
2. **Trilha socrática.**
3. **Ilustração dinâmica.**
4. **Laboratório/instrumento interativo.**
5. **Quiz robusto.**
6. **Links de aprofundamento.**
7. **Honestidade do modelo.**

A ordem pode variar. Ventila 15, por exemplo, expande o padrão com múltiplos tutores: modo, clínica, fórmula/biofísica e leitura gráfica. Isso é ampliação válida, não quebra.

## 8. Caso clínico — cinco atos

Formato preferido:

1. Entrada — por que está no ventilador?
2. Leitura — o que monitor/exame/gaso/curvas mostram?
3. Decisão — o que parece lógico?
4. Pegadinha — onde a decisão intuitiva lesa?
5. Reavaliação — qual leitura muda a conduta?

O Ato 4 é ativo clínico alto. Não apagar pegadinhas. Elas são o mecanismo de ensino.

## 9. Feedback de quiz

As alternativas devem ser curtas, plausíveis e equilibradas. A correta não pode ser a mais longa nem a mais “bonita”.

O feedback deve carregar o peso didático. Estrutura ideal:

```txt
Mecanismo
Por que a correta
A armadilha
À beira do leito
Ponte
```

Em HTML, a forma concreta pode ser objeto JS, strings estruturadas, blocos `.gab` ou equivalente. O que importa é a função didática.

## 10. Validação antes de publicar

Checklist mínimo:

```txt
1. O HTML abre sozinho?
2. A sintaxe JS compila?
3. Abas/nav funcionam?
4. Trilha inicia, responde e finaliza?
5. Quiz inicia, responde e finaliza?
6. Sliders atualizam readouts?
7. Animação roda ou respeita prefers-reduced-motion?
8. Links relativos existem?
9. Deep-links Respira/Ventila não foram quebrados?
10. A caixa de honestidade está presente?
11. Nenhum conteúdo foi reduzido?
```

Quando possível, validar com navegador real ou jsdom com stubs:

```js
beforeParse(w){
  w.Element.prototype.scrollIntoView = () => {};
  w.scrollTo = () => {};
}
```

A validação não precisa virar pipeline obrigatório. Pode ser script local de segurança.

## 11. Lições técnicas do projeto

- Verificar HTML cru, não cache.
- A âncora `<a>` pode envolver card inteiro; cuidado ao inferir mapeamento por texto próximo.
- `jsdom` não implementa `scrollIntoView`/`scrollTo`; stubar.
- `const` top-level não vira `window`; `function` top-level vira. Se precisar testar de fora, exponha explicitamente.
- Sliders com `step` arredondam valor; use valores na grade.
- Disclaimers de honestidade são parte da confiança.
- Índice pode perder costuras em reconstrução; reler após mudanças.
- Não mexer em módulo validado por gosto de refactor.

## 12. Política específica sobre build e DRY

A versão anterior deste documento sugeria núcleo separado e build inline. Essa orientação está superada.

Decisão atual:

```txt
single-file autocontido publicado > build elegante
```

DRY só paga se a duplicação doer de verdade. A pergunta não é “há duplicação?”, porque há. A pergunta é:

```txt
com que frequência ainda mudaremos código compartilhado?
```

Se a resposta for “quase nunca”, não buildar é correto.

Se algum dia a evolução pesada exigir DRY, a forma preferida é:

- `/src` local de referência;
- snippets auditáveis;
- scripts auxiliares opcionais;
- cópia manual consciente;
- sem tornar o deploy dependente do build.

## 13. Política de links e rotas

Rotas públicas antigas não devem quebrar.

Manter vivos:

- `index.html`
- `ventila.html`
- `ventila0.html` a `ventila26.html`
- `mvp1-interativo.html` a `mvp10-interativo.html`
- aliases/wrappers existentes em `/modules/`

Ao criar rota nova, preferir adicionar, não substituir.

## 14. Estilo de prosa

Idioma: PT-BR.

Tom: direto, clínico, socrático, visual, causal.

Priorizar:

- mecanismo;
- contraste;
- analogia precisa;
- leitura de curva;
- armadilha real;
- decisão à beira do leito;
- ponte para módulo anterior.

Evitar:

- protocolo sem fisiologia;
- “sempre/nunca” sem mecanismo;
- respostas genéricas;
- listas decorativas;
- moralismo clínico;
- simplificação que apaga a nuance.

## 15. Honestidade clínica

Todo módulo é material didático. Não é diretriz, prescrição individual, calculadora clínica validada nem substituto de julgamento profissional.

Quando o modelo for monocompartimental, dizer isso.
Quando o limiar for heurístico, dizer isso.
Quando o número for estimativa, dizer isso.
Quando o fenômeno real depender de heterogeneidade pulmonar, esforço, parede torácica, hemodinâmica ou sedação, dizer isso.

## 16. Definition of Done

### Por módulo

- abre sozinho;
- não depende de build;
- mantém tese explícita;
- preserva ou amplia conteúdo;
- tem interação funcional;
- usa mecanismo como eixo;
- tem pegadinha clínica real;
- tem feedback robusto;
- tem caixa de honestidade;
- tem links vivos;
- tem rodapé autoral/dedicatória quando aplicável.

### Do projeto

- Respira 10 módulos vivos;
- Ventila 0–26 vivos;
- `ventila.html` atualizado;
- links Respira↔Ventila preservados;
- nenhuma redução de módulos robustos;
- documentação alinhada com a arquitetura real.

## 17. Frase-guia

Respira ensinou a respirar pensando.

Ventila deve ensinar a usar a máquina sem apagar o mecanismo que ela está substituindo.

*Fim do CLAUDE.md. Se uma decisão operacional mudar, atualize este arquivo para refletir o estado real, não o plano ideal.*
