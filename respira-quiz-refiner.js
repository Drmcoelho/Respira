/* Respira · refinamento psicométrico das trilhas
   Princípio: alternativas curtas, plausíveis e balanceadas; robustez transferida
   para o feedback pós-resposta. Sem preenchimento genérico de alternativas. */
(function(){
  const script = document.currentScript;
  const moduleId = script?.dataset?.module || '';
  const TARGETS = [2,0,3,1,1,3,0,2,0,2,1,3,2,1,0,3,2,0];

  const R = {
    m7: {
      short: [
        {answer:2, opts:['lista por doença','via de administração','força sobre eixo fisiológico','ordem alfabética']},
        {answer:0, opts:['R↓, τ↓, auto-PEEP↓','complacência↑','recrutamento alveolar','conteúdo de O₂↑']},
        {answer:3, opts:['dose baixa','não funciona na asma','efeito imediato inalatório','anti-inflamatório tardio']},
        {answer:1, opts:['sobe muito','quase não sobe','sobe se aumentar fluxo','depende só da Hb']},
        {answer:1, opts:['broncodilata','mantém alvéolo aberto','aumenta hemoglobina','elimina CO₂']},
        {answer:3, opts:['igual ao prematuro','é proibido no adulto','funciona só com PEEP alta','não muda desfecho']},
        {answer:0, opts:['C↑ e shunt↓','só remove líquido','só melhora saturação','não muda mecânica']},
        {answer:2, opts:['erro de coleta','alcalose sempre','gera CO₂ ventilável','sem relação']},
        {answer:0, opts:['oxigenação↑ sem sobrevida↑','mortalidade↓ comprovada','piora sempre','só funciona em criança']},
        {answer:2, opts:['droga inalada','apenas conforto','recruta e casa V/Q','sem evidência']},
        {answer:1, opts:['qual antibiótico?','qual eixo e qual força?','qual imagem?','qual dose máxima?']}
      ],
      deep: [
        'A unidade de raciocínio deixa de ser “nome da droga” e vira vetor: eixo fisiológico, direção da força e custo. Isso preserva transferência: o mesmo mapa serve para asma, edema, SDRA e hipercapnia.',
        'O β2 age no cano, não no balão. Ao reduzir resistência, encurta a constante de tempo; com expiração mais completa, cai aprisionamento e auto-PEEP. A melhora ventilatória nasce da mecânica, não da saturação.',
        'Corticoide não é botão de broncodilatação. Ele reduz edema/inflamação da parede brônquica em escala de horas; por isso é prevenção de recaída e consolidação de resposta, não resgate minuto-a-minuto.',
        'No shunt verdadeiro, sangue atravessa regiões não ventiladas; FiO₂ alta só enriquece alvéolos abertos. A solução mecanística é recrutar, drenar ou redistribuir V/Q — não simplesmente “mais oxigênio”.',
        'PEEP é uma tala pneumática: mantém unidades abertas no fim da expiração. Ela substitui mecanicamente parte do papel do surfactante, mas cobra preço hemodinâmico e risco de hiperdistensão.',
        'No prematuro falta surfactante; na SDRA adulta o ambiente alveolar inflamatório inativa e distribui mal o surfactante exógeno. O alvo molecular parece certo, mas o sistema onde ele cai está errado.',
        'No edema cardiogênico o líquido causa dois problemas simultâneos: endurece o pulmão e cria shunt por alvéolo inundado. Diurese e vasodilatação reduzem carga hídrica; pressão positiva compra tempo recrutando.',
        'Bicarbonato converte acidose fixa em CO₂. Se a ventilação não elimina esse CO₂, o pH pode piorar. A pergunta decisiva é: existe ventilação alveolar suficiente para pagar essa conta?',
        'iNO é resgate fisiológico, não terapia modificadora de história natural: melhora casamento V/Q por vasodilatação seletiva onde há ventilação, mas não remove a lesão alveolar que determina desfecho.',
        'Prona é terapêutica física: muda gradientes gravitacionais, reabre dorso, reduz heterogeneidade e melhora V/Q. Por isso sua força é estrutural, não farmacológica.',
        'A pergunta final é sempre vetorial: que eixo está fora do lugar, em que direção, e qual intervenção empurra com melhor relação benefício/custo naquele paciente.'
      ]
    },
    m8: {
      short: [
        {answer:2, opts:['número no fluxômetro','tamanho da narina','fluxo entregue vs demanda','cor da mucosa']},
        {answer:0, opts:['menor no dispneico','igual nos dois','maior no dispneico','zero no repouso']},
        {answer:3, opts:['usa O₂ puro','tem reservatório','mede a respiração','fluxo total excede demanda']},
        {answer:1, opts:['fluxo baixo','bolsa + válvulas','plástico rígido','umidificação']},
        {answer:1, opts:['sedação e nebulização','lava CO₂ + PEEP leve','hemodiálise respiratória','mede débito cardíaco']},
        {answer:3, opts:['seca diretamente','baixa FC','O₂ a 100%','recruta e descarrega VE']},
        {answer:0, opts:['IPAP−EPAP ventila','EPAP sozinha ventila','FiO₂ alta baixa CO₂','umidificação baixa CO₂']},
        {answer:2, opts:['sempre segura','cura SDRA','pode atrasar intubação','só serve para criança']},
        {answer:0, opts:['reinalação de CO₂','FiO₂ excessiva','resseca nariz','sem problema']},
        {answer:2, opts:['disponibilidade','preço do dispositivo','mecanismo + demanda','preferência isolada']},
        {answer:1, opts:['subir fluxômetro','FiO₂ confiável + pressão','trocar máscara','esperar sozinho']}
      ],
      deep: [
        'Baixo fluxo é mistura, não prescrição de FiO₂. O paciente completa a inspiração com ar ambiente; quanto maior a demanda inspiratória, maior a diluição do O₂ entregue.',
        'A mesma cânula muda de significado conforme o drive. No paciente calmo, o fluxo suplementar pesa mais na mistura; no taquipneico, vira fração pequena de um fluxo inspiratório muito maior.',
        'Venturi resolve o problema por engenharia de fluxo: o jato entranha ar numa proporção definida e entrega fluxo total suficiente para não depender do puxão inspiratório do paciente.',
        'A não-reinalante cria um reservatório inspiratório de O₂. Se a bolsa colaba, o sistema deixou de ser reservatório e voltou a ser mistura instável com ar ambiente.',
        'HFNC não é “cateter forte”: é dispositivo de alto fluxo aquecido/umidificado, com FiO₂ estável, lavagem de espaço morto e pequena pressão expiratória dependente de vazamento/boca aberta.',
        'CPAP no edema une dois módulos: recruta alvéolo inundado e altera hemodinâmica torácica, reduzindo retorno venoso e pós-carga do VE. Por isso a resposta pode ser muito rápida.',
        'BiPAP separa funções: EPAP ajuda a vencer auto-PEEP/recrutar; pressão de suporte gera volume corrente e aumenta ventilação alveolar. CO₂ cai pela ventilação, não pela FiO₂.',
        'Na hipoxemia de SDRA, insistir em VNI pode mascarar falência e manter esforço inspiratório lesivo. A pergunta não é “tolerou máscara?”, mas se esforço, troca e trajetória permitem segurança.',
        'Máscara simples adiciona espaço morto. Fluxo baixo não lava o CO₂ expirado dentro da máscara; por isso existe piso operacional de fluxo que não existe da mesma forma no cateter nasal.',
        'Escolher dispositivo é casar mecanismo e demanda: hipoxemia precisa fração/recrutamento; hipercapnia precisa suporte ventilatório; demanda alta exige fluxo que a cubra.',
        'Escalada não é estética de interface: é sair de mistura imprevisível para fração controlada e, quando necessário, adicionar pressão para abrir alvéolo ou ventilar bomba cansada.'
      ]
    },
    m9: {
      short: [
        {answer:2, opts:['gravidade','coração','resistência + elastância','saturação']},
        {answer:0, opts:['pressão flutua','pressão fica fixa','pressão zera','não há pressão']},
        {answer:3, opts:['pressão explode','PEEP some','modo sem risco','volume cai silenciosamente']},
        {answer:1, opts:['vazamento','some a parcela resistiva','PEEP aumentou','pulmão esvaziou']},
        {answer:1, opts:['driving pressure','parcela resistiva','PEEP','complacência']},
        {answer:3, opts:['atrito do tubo','frequência','FiO₂','estiramento alveolar']},
        {answer:0, opts:['via aérea/resistência','SDRA/edema','coração','PEEP isolado']},
        {answer:2, opts:['secreção isolada','tubo mordido','complacência/sistema','broncoespasmo puro']},
        {answer:0, opts:['estiramento do baby lung','inclui FiO₂','é mais fácil','não tem sentido']},
        {answer:2, opts:['sim, sempre','estoura pulmão','não se platô não sobe','só por FiO₂ alta']},
        {answer:1, opts:['sensor quebrou','aprisionamento/auto-PEEP','PEEP alto sempre','volume baixo']},
        {answer:3, opts:['decorar modos','confiar em alarme','subir PEEP','ler equação + pausa']}
      ],
      deep: [
        'A equação do movimento transforma o ventilador em problema mensurável: pressão total se reparte em resistência do fluxo, carga elástica do volume e pressão basal expiratória.',
        'No VCV, o ventilador garante volume; a pressão denuncia o paciente. Se R ou elastância sobem, o painel mostra isso como aumento de pico/platô.',
        'No PCV, o teto de pressão protege contra pico alto, mas esconde queda de volume. O parâmetro crítico passa a ser volume corrente exalado e ventilação minuto.',
        'A pausa é uma manobra diagnóstica porque zera fluxo. Sem fluxo, R·fluxo desaparece; o platô revela a pressão elástica que distende unidades alveolares.',
        'Pico−platô é o preço do cano. Quando cresce, pense em secreção, broncoespasmo, tubo dobrado/mordido ou circuito; não em baby lung rígido.',
        'Driving é platô−PEEP: volume dividido pela complacência disponível. Em SDRA, normaliza o volume pelo pulmão que ainda ventila, não pelo tamanho corporal.',
        'Pico alto com platô normal separa a emergência respiratória da emergência mecânica: o tubo/cano está caro; o parênquima não recebeu pressão elástica excessiva.',
        'Pico e platô altos significam que a pressão chegou ao alvéolo ou ao sistema toracopulmonar. Aqui entram SDRA, edema, pneumotórax, seletiva, distensão abdominal e auto-PEEP.',
        'O baby lung explica por que 6 mL/kg pode ainda ser demais: o volume é baixo para o corpo, mas alto para a fração aerada. ΔP captura essa desproporção.',
        'Fluxo alto aumenta pressão resistiva e encurta tempo inspiratório; isso pode afetar conforto e tempo expiratório, mas não aumenta distensão alveolar se platô/driving não sobem.',
        'Fluxo expiratório que não zera é gráfico de tempo insuficiente: o próximo ciclo começa antes do esvaziamento terminar. A solução é dar tempo e tratar R.',
        'Domínio básico é decompor forma de onda: o que é cano, o que é tecido, o que é PEEP, e o que você fixou no modo escolhido.'
      ]
    },
    m10: {
      short: [
        {answer:2, opts:['infecção apenas','oxigênio apenas','volu/baro/atelectrauma','tempo de uso apenas']},
        {answer:0, opts:['peso predito por altura','peso real','peso ideal estético','peso de admissão']},
        {answer:3, opts:['FiO₂ 100%','PEEP zero','fluxo máximo','platô, driving e VC baixo']},
        {answer:1, opts:['saturação','energia por minuto','débito cardíaco','temperatura do gás']},
        {answer:1, opts:['sempre cai','pode não cair','zera','não muda']},
        {answer:3, opts:['CO₂ alto é bom','rim corrige já','PaCO₂ não importa','proteção vale a acidose']},
        {answer:0, opts:['baixo colapsa; alto distende','ambos só dessaturam','baixo dá pneumotórax','não faz diferença']},
        {answer:2, opts:['só acordar','só febre ceder','causa melhorando + pouco suporte','esperar 14 dias']},
        {answer:0, opts:['suporte mínimo observado','extubar direto','sedar mais','desligar O₂']},
        {answer:2, opts:['número arbitrário','mede coração','rápido e raso = fadiga','mede febre']},
        {answer:1, opts:['fígado','coração','rim','intestino']},
        {answer:3, opts:['cor da urina','glicemia','peso','via aérea protegida']},
        {answer:2, opts:['decorar parâmetros','confiar no aparelho','proteger e soltar por mecanismo','subir PEEP até saturar']}
      ],
      deep: [
        'VILI é biomecânica aplicada: deformação excessiva, pressão, abertura/fechamento repetido e resposta inflamatória. A meta não é “ventilar bonito”, é reduzir agressão mecânica cumulativa.',
        'Peso predito é proxy de tamanho pulmonar. Obesidade aumenta massa corporal, não número de alvéolos; usar peso real transforma cálculo protetor em volutrauma.',
        'Platô limita pressão alveolar, driving limita estiramento relativo ao pulmão disponível, e VC baixo reduz amplitude de deformação. O trio protege melhor que qualquer número isolado.',
        'Mechanical power troca foco de pressão instantânea para dose energética por minuto. Frequência, volume, fluxo e pressão entram na mesma conta de agressão acumulada.',
        'A troca VC baixo por FR alta pode conservar PaCO₂ às custas de energia. Às vezes a escolha protetora é aceitar hipercapnia permissiva, não perseguir gasometria normal.',
        'Hipercapnia permissiva é decisão de dano comparativo: uma acidose respiratória tolerável pode ser menos deletéria que aumentar volume/pressão e perpetuar VILI.',
        'PEEP tem ponto ótimo. Pouco PEEP deixa atelectrauma; excesso transforma unidades abertas em regiões hiperdistendidas, aumenta espaço morto e derruba retorno venoso/débito.',
        'Desmame antes de elegibilidade é teste falso: se causa, troca, hemodinâmica ou sedação ainda estão ruins, o teste reprova o contexto, não a bomba respiratória.',
        'TRE é teste de esforço respiratório controlado. Ele pergunta se músculo, pulmão, troca gasosa e circulação sustentam baixa assistência por tempo suficiente.',
        'RSBI alto é assinatura de carga maior que capacidade: o paciente reduz volume para poupar trabalho por ciclo, acelera, aumenta ventilação de espaço morto e caminha para fadiga.',
        'Retirar pressão positiva muda o coração: aumenta retorno venoso e pós-carga do VE. Um VE limítrofe converte desmame em edema, mesmo com mecânica respiratória aceitável.',
        'Extubação exige duas vitórias: respirar e proteger via aérea. TRE avalia a primeira; consciência, tosse, secreção e cuff leak selecionado avaliam a segunda.',
        'O capstone é uma ética mecânica: entregar a menor energia capaz de sustentar vida e retirar suporte assim que carga e capacidade permitirem.'
      ]
    }
  };

  function redistribute(q, qi){
    if(!q || !Array.isArray(q.opts) || q.opts.length !== 4) return;
    const oldAnswer = Number(q.answer);
    if(!Number.isInteger(oldAnswer) || oldAnswer < 0 || oldAnswer > 3) return;
    const target = TARGETS[qi % TARGETS.length];
    if(oldAnswer === target) return;
    const old = q.opts.slice();
    const ordered = new Array(4);
    ordered[target] = old[oldAnswer];
    const wrongs = old.map((o,i)=>({o,i})).filter(x=>x.i !== oldAnswer);
    const shift = qi % wrongs.length;
    const rotated = wrongs.slice(shift).concat(wrongs.slice(0, shift));
    let wi = 0;
    for(let pos=0; pos<4; pos++) if(pos !== target) ordered[pos] = rotated[wi++].o;
    q.opts = ordered;
    q.answer = target;
  }

  function byStemExtra(q){
    const s = String(q?.stem || '').toLowerCase();
    if(/sdra|surfactante|laplace|peep/.test(s)) return 'Na SDRA, a pista central costuma ser colapso/recrutamento, baixa complacência e shunt. O mecanismo correto precisa explicar por que FiO₂ isolada tem teto e por que pressão/prona mudam a distribuição do ar.';
    if(/dpoc|asma|bronco|auto-peep|expira/.test(s)) return 'Nas obstrutivas, a variável dominante é tempo: resistência alta alonga τ e impede esvaziamento. A resposta correta deve falar de R, fluxo expiratório e aprisionamento, não apenas de saturação.';
    if(/edema|cardiogênico|diurético|cpap/.test(s)) return 'No edema, líquido endurece o pulmão e inunda alvéolo; por isso complacência e shunt mudam juntos. A intervenção efetiva ou retira líquido/carga cardíaca ou recruta enquanto a causa é tratada.';
    if(/embolia|espaço morto|perfusão/.test(s)) return 'Na embolia, o problema é ventilação sem perfusão: espaço morto sobe. A gasometria pode mostrar hipoxemia e hipocapnia inicial, mas o eixo primário é Q perdido, não alvéolo cheio.';
    if(/fibrose|difusão|complacência/.test(s)) return 'Na fibrose, a parede fica rígida e a difusão encurta a reserva ao esforço. O paciente compensa com respiração rápida e pequena porque volume grande custa caro demais.';
    if(/pneumonia|atelectasia|shunt/.test(s)) return 'Pneumonia e atelectasia convergem para shunt quando há perfusão de unidade mal ventilada. O₂ ajuda só nas unidades abertas; a solução real exige reabrir, drenar ou tratar o preenchimento alveolar.';
    return '';
  }

  function appendDeep(q, text){
    if(!text) return;
    const box = `<div class="fb-deep" style="margin-top:10px;padding-top:10px;border-top:1px solid rgba(0,0,0,.09)"><strong>Leitura de mecanismo.</strong> ${text}</div>`;
    q.good = String(q.good || '') + box;
    q.bad = String(q.bad || '') + box;
  }

  function refine(){
    if(typeof QUESTIONS === 'undefined' || !Array.isArray(QUESTIONS) || window.__respiraRefined) return;
    window.__respiraRefined = true;
    const rule = R[moduleId] || {};
    QUESTIONS.forEach((q, qi)=>{
      const patch = rule.short?.[qi];
      if(patch){
        q.opts = patch.opts.slice();
        q.answer = patch.answer;
      } else {
        redistribute(q, qi);
      }
      appendDeep(q, rule.deep?.[qi] || byStemExtra(q));
    });
  }

  refine();
})();
