# Prompts de geração — lâminas faltantes do Atlas (Ventila 00–29)

O Atlas Respira está completo (20/20: módulos 01–10, Ponte RF1–4, Ocupacional RO1–6). As lâminas que **faltam** são as da série **Ventila (00–29)** — 30 pranchas. Este documento traz prompts prontos para um modelo de imagem que desenha texto com precisão (ex.: gpt-image / equivalente).

**Como usar:** o prompt final de cada módulo = **[BLOCO DE ESTILO]** (seção 1) + **[REGRAS DE TEXTO]** (seção 2) + **o bloco do módulo** (seção 3). Cole os três juntos. Gere em **paisagem 3:2 (1536×1024)**. Ao receber as imagens, o nome de arquivo alvo para integração no `atlas.html` é `assets/figuras/ventila-NN.webp` (ex.: `ventila-00.webp`), href `ventilaN.html`.

---

## 1. BLOCO DE ESTILO (colar em toda geração, sem alterar)

```
Ilustração médica-editorial em estilo aquarela + gravura fina, para um pôster didático de ventilação mecânica. Formato paisagem 3:2. Fundo de papel envelhecido creme (#F4EFE4) com leve vinheta e textura sutil de papel. Paleta restrita e sóbria: tinta verde-petróleo escura (#16383B) para contornos e títulos; terracota/ferrugem (#C0603A) para tags e destaques; azul-petróleo (#3C7F86) para O₂/ar; vermelho-tijolo (#8E2F39) para sangue/CO₂; verde-musgo (#4E7C5A) para acertos/fluxo. Nada de cores neon, nada de gradientes chamativos, nada de aparência 3D-render.

Layout: título no topo, centralizado, em serifa elegante (tipo Fraunces/Georgia), cor verde-petróleo, no formato "NN · Título", ladeado por finas linhas terracota com um pequeno losango. Abaixo, 5 painéis retangulares de cantos arredondados, com borda fina verde-petróleo e preenchimento quase branco. Cada painel tem: um número em um quadrado arredondado verde-petróleo (algarismo branco) no canto superior esquerdo; um título curto ao lado; a ilustração central do mecanismo; e, na base do painel, uma "tag de veredito" em pílula terracota com texto branco curto. Estilo anatômico limpo, alto contraste, legível em celular. Foco em MECANISMO, não decorativo. Traço de caderno científico, coerente entre os painéis.
```

## 2. REGRAS DE TEXTO (colar junto)

```
Todo o texto na imagem deve estar em português do Brasil, grafado exatamente como fornecido, sem erros de ortografia, legível e curto. Não inventar rótulos além dos listados. Preferir poucas palavras por elemento. Símbolos e setas em vez de frases longas. Fórmulas e unidades exatamente como escritas (ex.: cmH₂O, PaCO₂, VEF1, ΔP, τ = R×C). Onde houver curvas de ventilador, manter eixos rotulados (Pressão cmH₂O, Fluxo L/min, Volume mL, tempo s). Sem marca d'água, sem logotipos.
```

## 3. PROMPTS POR MÓDULO

> Cada bloco descreve: **motivo central** e os **5 painéis** (título · o que desenhar · tag terracota). Ancorado na tese do módulo.

### Ventila 00 · A gramática da máquina
Motivo central: um ventilador estilizado com a ideia de "contrato" dos modos (variável controlada × variável livre).
1. Variável controlada · seletor apontando para "volume" OU "pressão"; o que a máquina promete · "a máquina garante 1 coisa"
2. Variável livre · a outra grandeza flutuando como consequência (onda variável) · "a outra varia"
3. Tempo do ciclo · linha do tempo do ciclo: inspiração, pausa, expiração · "quem controla o tempo?"
4. Fluxo · perfis de fluxo (quadrado vs decelerante) · "forma do fluxo"
5. Gatilho e ciclagem · disparo (paciente/tempo) e término (volume/tempo/fluxo) · "início e fim"
Rodapé: contrato — controlada, livre, tempo, fluxo.

### Ventila 01 · A causa do tubo vem antes do modo
Motivo central: um mapa de decisão "por que este paciente está no ventilador?".
1. Falha de oxigenação · alvéolo com shunt/edema · "não oxigena"
2. Falha de ventilação · CO₂ subindo, bomba fraca · "não ventila"
3. Proteção de via aérea · rebaixamento, risco de aspiração · "não protege"
4. Trabalho excessivo · musculatura exausta, tiragem · "não aguenta o esforço"
5. A pergunta antes do modo · seta: causa → objetivo → só então o modo · "modo é consequência"
Rodapé: indicação define a estratégia.

### Ventila 02 · Máquina, circuito, tubo, via aérea ou pulmão?
Motivo central: corte do sistema respiratório-ventilador com pontos de falha.
1. Máquina/circuito · ventilador e traqueias, vazamento/desconexão · "fonte e circuito"
2. Tubo · tubo endotraqueal, dobra/rolha/mordida · "R ∝ L/d⁴"
3. Via aérea · brônquios estreitados, secreção · "resistência da via"
4. Pulmão · parênquima duro/inflamado · "complacência"
5. Onde está o problema? · árvore de troubleshooting da pressão alta · "isole a camada"
Rodapé: pico alto ≠ sempre pulmão.

### Ventila 03 · Curvas P/F/V são semiologia
Motivo central: três curvas de ventilador em tempo real (pressão, fluxo, volume × tempo).
1. Pressão × tempo · onda de pressão com PEEP, pico, platô · "pressão conta a história"
2. Fluxo × tempo · fluxo inspiratório e expiratório; fluxo que não zera · "fluxo denuncia auto-PEEP"
3. Volume × tempo · subida e platô do volume corrente · "volume entregue"
4. Pausa inspiratória · pico vs platô destacados · "pico − platô = resistivo"
5. Ler à beira do leito · três curvas empilhadas alinhadas no tempo · "curva = exame físico"
Rodapé: a tela é semiologia.

### Ventila 04 · Loops revelam relações
Motivo central: loops pressão-volume e fluxo-volume.
1. Loop P-V normal · alça suave · "trabalho respiratório"
2. Bico de pássaro / hiperdistensão · achatamento no topo do loop P-V · "distende demais"
3. Baixa complacência · loop P-V deitado · "pulmão duro"
4. Loop F-V e secreção · serrilhado no ramo expiratório · "dente de serra = secreção"
5. Auto-PEEP no F-V · fluxo expiratório que não retorna a zero · "não terminou de expirar"
Rodapé: loops mostram o que valores escondem.

### Ventila 05 · VCV — volume é promessa, pressão denuncia
Motivo central: modo volume-controlado com fluxo quadrado.
1. Volume garantido · onda de volume fixa a cada ciclo · "VT prometido"
2. Fluxo constante · fluxo quadrado inspiratório · "fluxo fixo"
3. Pressão como consequência · pressão sobe conforme a mecânica · "pressão varia"
4. Pico × platô · pausa inspiratória revelando resistivo vs elástico · "pico − platô = R×fluxo"
5. Perigo · pressão disparando em pulmão rígido · "volume fixo pode ferir"
Rodapé: VCV promete volume; a pressão avisa.

### Ventila 06 · PCV — pressão é promessa, volume denuncia
Motivo central: modo pressão-controlada com fluxo decelerante.
1. Pressão garantida · patamar de pressão retangular · "ΔP prometido"
2. Fluxo decelerante · fluxo que cai exponencial · "fluxo(t) = (ΔP/R)·e^(−t/τ)"
3. Volume como consequência · VT variando com R e C · "volume varia"
4. Constante de tempo · enchimento em função de τ · "VT = ΔP·C·(1 − e^(−Ti/τ))"
5. Perigo · queda de VT em broncoespasmo · "pressão fixa pode ventilar pouco"
Rodapé: PCV promete pressão; o volume avisa.

### Ventila 07 · Adaptativos / PRVC — um controlador, não um médico
Motivo central: um algoritmo perseguindo um VT-alvo ajustando a pressão ciclo a ciclo.
1. Alvo de volume · VT-alvo definido · "meta de VT"
2. Ajuste automático de pressão · a pressão sobe/desce buscando o alvo · "o robô titula"
3. Reação à mecânica · resposta a mudança de complacência · "persegue o número"
4. Armadilha do drive · paciente com fome de ar e a máquina reduzindo pressão · "pode mascarar esforço"
5. Supervisão humana · médico revisando limites/alarmes · "controlador precisa de médico"
Rodapé: adaptativo persegue alvo, não julga.

### Ventila 08 · PSV, CPAP, SIMV — dividir o trabalho
Motivo central: partição do trabalho respiratório entre paciente e máquina.
1. PSV · pressão de suporte assistindo cada esforço · "máquina completa o esforço"
2. CPAP · pressão contínua, paciente respira sozinho · "só pressão de base"
3. SIMV · ciclos mandatórios + espontâneos · "mistura de ciclos"
4. Trabalho compartilhado · balança paciente × ventilador · "quem faz quanto"
5. Desmame gradual · redução do suporte com o tempo · "devolver o trabalho"
Rodapé: suporte parcial divide a carga.

### Ventila 09 · Assincronia é desencontro temporal
Motivo central: descompasso entre o drive neural do paciente e a entrega da máquina.
1. Duplo disparo · dois ciclos colados · "1 esforço, 2 ciclos"
2. Esforço ineficaz · deflexão sem ciclo entregue · "esforço sem resposta"
3. Auto-disparo · ciclos sem esforço (oscilação/água) · "máquina dispara sozinha"
4. Ciclagem precoce/tardia · término fora de hora do fluxo · "termina cedo ou tarde"
5. Ler a curva · onda de pressão/fluxo com o desencontro marcado · "drive × entrega"
Rodapé: assincronia se lê na curva.

### Ventila 10 · Esforço entre P-SILI e atrofia
Motivo central: uma balança entre esforço excessivo (lesão) e esforço nulo (atrofia).
1. Esforço excessivo (P-SILI) · pressão transpulmonar alta autoinfligida · "esforço lesa (ΔPL)"
2. Atrofia por inatividade · diafragma afinando (VIDD) · "parado atrofia"
3. Pressão muscular (Pmus) · vetor do esforço do diafragma · "medir o esforço"
4. Sedação/BNM · bloqueio neuromuscular exige sedação real · "bloquear pede sedar"
5. Zona segura · janela intermediária de esforço · "nem demais, nem de menos"
Rodapé: proteger o pulmão e o diafragma.

### Ventila 11 · "Intubado" não é diagnóstico
Motivo central: um classificador que separa fenótipos de paciente ventilado.
1. Obstrutivo · via aérea estreita, auto-PEEP · "dar tempo"
2. Restritivo/SDRA · pulmão pequeno e duro · "proteger com VT baixo"
3. Misto · obstrução + restrição · "qual componente domina"
4. Bomba/neuromuscular · pulmão normal, músculo fraco · "problema é a bomba"
5. Do fenótipo ao plano · setas fenótipo → estratégia · "diagnóstico guia o modo"
Rodapé: fenótipo antes de protocolo.

### Ventila 12 · Desmame e os dois portões
Motivo central: dois portões — respirar (SBT) e proteger a via aérea (extubação).
1. Pré-requisitos · causa resolvida, estável, oxigenando · "pronto para testar?"
2. Teste de respiração espontânea (SBT) · paciente respirando com suporte mínimo · "aguenta respirar?"
3. RSBI · índice FR/VT · "RSBI = FR / VT(L); ≤105"
4. Portão da proteção · tosse, secreção, nível de consciência · "protege a via aérea?"
5. Dois portões · respirar E proteger, ambos abertos · "extubar = os dois"
Rodapé: desmame é respirar; extubação é respirar e proteger.

### Ventila 13 · Traqueostomia é plataforma, não cura
Motivo central: tubo traqueal e a física de Poiseuille; caminho de decanulação.
1. Indicações · desmame prolongado, proteção, higiene · "plataforma de desmame"
2. Poiseuille · resistência ∝ 1/d⁴; tubo mais curto e largo · "R ∝ L/d⁴"
3. Menos espaço morto e sedação · trabalho respiratório menor · "menos carga"
4. Cânula e cuff · anatomia da cânula, cuff, fenestra · "componentes"
5. Decanulação · escada de retirada progressiva · "sair da cânula"
Rodapé: traqueostomia compra condição de desmame.

### Ventila 14 · O pulmão na tela
Motivo central: um campo alveolar heterogêneo com quatro fenômenos simultâneos.
1. Shunt · alvéolo cheio/colapsado com sangue passando · "sangue sem ar"
2. Recrutamento · alvéolo colapsado reabrindo com PEEP · "abrir o fechado"
3. Hiperdistensão · alvéolo já aberto estirando demais · "distender demais"
4. Auto-PEEP · unidade que não esvazia · "ar preso"
5. Heterogeneidade · os quatro no mesmo pulmão · "o mesmo pulmão, zonas diferentes"
Rodapé: a PEEP ideal equilibra abrir sem estourar.

### Ventila 15 · PSV · VCV · PCV lado a lado
Motivo central: comparador dos três modos e a inversão causal.
1. PSV · esforço do paciente + suporte · "paciente inicia"
2. VCV · volume fixo, pressão consequente · "promete volume"
3. PCV · pressão fixa, volume consequente · "promete pressão"
4. Inversão causal · o que é promessa em um é consequência no outro · "promessa × consequência"
5. Leitura de curvas · as três assinaturas de onda lado a lado · "reconhecer pela curva"
Rodapé: o mesmo pulmão, três contratos.

### Ventila 16 · Tutor adaptativo de sessão
Motivo central: um grafo de conhecimento com domínio (mastery) por nó.
1. Grafo de pré-requisitos · nós conectados (mecânica → modos → assincronia) · "o que vem antes"
2. Mastery (BKT) · barras de domínio por conceito · "quanto você sabe"
3. Diagnóstico do erro · nó fraco destacado · "onde falha"
4. Remediação dirigida · seta voltando ao pré-requisito · "reforço no ponto certo"
5. Progressão · caminho iluminando conforme domina · "avançar com base"
Rodapé: aprender pelo mecanismo, não pela memória.

### Ventila 17 · SDRA — recrutabilidade antes da PEEP
Motivo central: a balança recrutamento × hiperdistensão × custo hemodinâmico.
1. Baby lung · pulmão aerado pequeno em meio a colapso · "pouco pulmão são"
2. Recrutar · unidades reabrindo com PEEP · "ganho: mais área"
3. Hiperdistensão · unidades sadias estirando · "custo: estresse"
4. Custo hemodinâmico · PEEP comprimindo o retorno venoso · "o VD paga"
5. PEEP só compra se recruta · gangorra ganho vs custo · "recrutabilidade decide"
Rodapé: PEEP não é dose fixa; depende de recrutar.

### Ventila 18 · Obstrutivo grave — dar tempo para sair
Motivo central: resistência alta, constante de tempo longa e auto-PEEP.
1. Via aérea estreitada · broncoespasmo/secreção · "R alto"
2. Constante de tempo · τ longo, esvaziamento lento · "τ = R×C"
3. Auto-PEEP · fluxo expiratório que não zera; ar preso · "não terminou de sair"
4. Tempo expiratório · alongar a expiração (menor FR) · "dar tempo"
5. Hipercapnia permissiva · aceitar CO₂ para não lesar · "não perseguir número"
Rodapé: no obstrutivo, tempo é remédio.

### Ventila 19 · Coração-pulmão — o VD no ventilador
Motivo central: o ventrículo direito sob pressão positiva.
1. Retorno venoso · pressão intratorácica reduzindo o enchimento · "pré-carga cai"
2. Resistência vascular pulmonar · vasos comprimidos em volumes altos/baixos · "RVP em U"
3. Sobrecarga do VD · VD dilatado · "pós-carga sobe"
4. Interdependência do septo · septo desviando para a esquerda · "septo empurra o VE"
5. Equilíbrio · PEEP/volume que poupam o VD · "proteger o coração direito"
Rodapé: a pressão positiva é vista pelo VD.

### Ventila 20 · Neuroventilação — CO₂ é hemodinâmica
Motivo central: o CO₂ como regulador do fluxo cerebral e da PIC.
1. PaCO₂ e vasos cerebrais · CO₂ alto dilata, baixo contrai · "CO₂ move o vaso"
2. Fluxo sanguíneo cerebral · relação CO₂ × fluxo · "hipocapnia reduz fluxo"
3. Pressão intracraniana · balão de volume intracraniano · "PIC e complacência"
4. O preço da hiperventilação · isquemia por vasoconstrição mantida · "hipocapnia isquemia"
5. Alvo estreito · janela de PaCO₂ segura · "mirar faixa, não extremos"
Rodapé: ventilar o cérebro é modular o CO₂.

### Ventila 21 · Prona e resgate — redistribuir antes de escalar
Motivo central: a posição prona redistribuindo V/Q e estresse.
1. Supino · consolidação dorsal, colapso dependente · "peso comprime o dorso"
2. Prona · redistribuição da ventilação/perfusão · "abrir o dorso"
3. V/Q regional · casamento melhor em prona · "V encontra Q"
4. Estresse mais homogêneo · pulmão distribuindo a carga · "menos estresse regional"
5. Resposta além da SpO₂ · mecânica e prognóstico, não só saturação · "olhar além do número"
Rodapé: prona é terapia da heterogeneidade.

### Ventila 22 · APRV — abrir sem aprisionar
Motivo central: dois níveis de pressão com terminação de fluxo controlada.
1. P-high / T-high · patamar alto sustentado recrutando · "manter aberto"
2. Release T-low · liberação breve para ventilar · "soltar por pouco tempo"
3. Terminação de fluxo · T-low curto guiado por % do pico de fluxo expiratório · "cortar antes de esvaziar"
4. Auto-PEEP intencional · ar residual mantendo recrutamento · "aprisionar de propósito, com cuidado"
5. Risco · T-low longo demais desrecruta / curto demais aprisiona · "ajuste fino"
Rodapé: abrir sustentando, ventilar liberando pouco.

### Ventila 23 · ECMO / ECCO₂R — a máquina compra proteção
Motivo central: circuito extracorpóreo como ponte, não cura.
1. Drenagem e retorno · cânulas e bomba · "sangue sai e volta"
2. Oxigenador (fluxo) · troca de O₂ dependente do fluxo de sangue · "fluxo = oxigenação"
3. Sweep (CO₂) · gás varredura removendo CO₂ · "sweep = ventilação"
4. Ultraproteção · ventilador quase em repouso · "pulmão descansa"
5. Ponte, não cura · seta para recuperação/transplante · "compra tempo"
Rodapé: extracorpóreo protege enquanto o pulmão sara.

### Ventila 24 · Obesidade, gestação, abdome — a parede pesa
Motivo central: a complacência do sistema não é a do pulmão.
1. Parede pesada · tórax/abdome comprimindo · "a parede empurra"
2. Pressão pleural alta · Ppl elevada consumindo pressão · "parede rouba pressão"
3. Complacência do sistema × pulmonar · dois molas em série · "Crs ≠ Cpulmão"
4. Pressão transpulmonar · o que realmente distende o pulmão · "PL = Palv − Ppl"
5. Recrutar e posicionar · cabeceira elevada, PEEP contra colapso · "vencer a parede"
Rodapé: platô alto pode ser parede, não pulmão.

### Ventila 25 · Pediatria e neonatologia — pulmão pequeno, tempo curto
Motivo central: a física específica do recém-nascido e da criança.
1. Tubo estreito · resistência altíssima em cânula fina · "R ∝ 1/d⁴"
2. Vazamento periportal · fuga ao redor do tubo sem cuff · "escape audível"
3. Volume garantido · modos que asseguram VT minúsculo preciso · "mL contam muito"
4. Constante de tempo curta · τ pequeno, ciclos rápidos · "tempo curto"
5. Reserva mínima · dessatura rápido na apneia · "pouca margem"
Rodapé: pouco volume, pouco tempo, muita atenção.

### Ventila 26 · Fora da UTI — transporte e contingência
Motivo central: robustez operacional (a checklist do transporte).
1. Oxigênio · cálculo de autonomia do cilindro · "quanto O₂ resta?"
2. Bateria e energia · autonomia elétrica do ventilador · "plano de energia"
3. Circuito e fixação · tubo fixado, conexões seguras · "nada solta"
4. Monitorização · SpO₂, capnografia, alarmes · "olhos no paciente"
5. Plano B · ambu e via aérea de resgate à mão · "falhou? plano B"
Rodapé: transporte seguro é preparo, não sorte.

### Ventila 27 · Pulmão restritivo — ventilar pequeno e duro
Motivo central: baby lung pouco recrutável, driving alto.
1. Baixa complacência · pulmão pequeno e rígido · "pouco volume cabe"
2. Driving pressure · ΔP alto por unidade de volume · "ΔP = Pplatô − PEEP"
3. VT pequeno · volume corrente reduzido (às vezes <6 mL/kg) · "ventilar pequeno"
4. Pouca recrutabilidade · fibrose que não reabre · "PEEP alta hiperdistende"
5. Reserva baixa · dessatura rápido, VD sensível · "cuidar do VD"
Rodapé: no pulmão pequeno, proteção vem antes do número.

### Ventila 28 · Pulmão misto — qual componente mata primeiro
Motivo central: obstrução e restrição no mesmo pulmão, com forças opostas.
1. Componente obstrutivo · auto-PEEP, ar aprisionado · "quer tempo"
2. Componente restritivo · driving alto, pulmão duro · "quer volume baixo"
3. Conflito · setas em sentidos opostos · "tempo × volume baixo"
4. Quem mata primeiro · triagem: colapso hemodinâmico (auto-PEEP) vs barotrauma (driving) · "trate o que descompensa agora"
5. Manobra de resgate · desconectar para deixar expirar no colapso por auto-PEEP · "soltar o ar preso"
Rodapé: não há ajuste único; trate o componente letal do minuto.

### Ventila 29 · Ocupacional na UTI — o pulmão que veio ferido do trabalho
Motivo central: costurar anamnese + imagem + função + gasometria + estratégia.
1. Anamnese ocupacional · jateamento, solda, biomassa, asbesto · "a profissão importa"
2. Imagem · TC com fibrose/massas em lobos superiores · "não é SDRA típica"
3. Função e gasometria · restrição prévia, hipercapnia crônica compensada · "não perseguir normocapnia"
4. Baixa recrutabilidade + VD · fibrose pouco recrutável, cor pulmonale · "PEEP modesta"
5. Rastrear e integrar · silicotuberculose e estratégia protetora · "história muda a ventilação"
Rodapé: o pulmão ocupacional já chega ferido — a história guia a máquina.

---

## 4. Depois de gerar
1. Enviar as imagens (de preferência 2–3 por vez; se a pré-visualização falhar, reduzir para JPEG pequeno).
2. Converter para WebP: `assets/figuras/ventila-00.webp` … `ventila-29.webp`.
3. Criar um Atlas Ventila próprio (ou estender o `atlas.html`) com o mesmo objeto `FIGURAS` (id `ventila-NN`, href `ventilaN.html`, detalhamento + quiz) — o conteúdo de detalhamento/quiz pode ser derivado de cada módulo, como foi feito no Atlas Respira.

*Estilo calibrado a partir das 20 pranchas já publicadas do Atlas Respira.*
