#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import html
import json
import pathlib
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "respira-ventila-atlas" / "media"

# local, Commons filename, module, title, license, guided reading, pitfall, bridge
ITEMS = [
    ("r01-airway-tree.svg", "Lungs diagram detailed.svg", "Respira 01", "Arvore respiratoria e escala anatomica", "CC BY 2.5", "Siga traqueia, bronquios e bronquiolos ate a regiao alveolar; a queda progressiva do calibre individual contrasta com o aumento da area transversal total.", "Nao converter anatomia em resistencia linear: calibre, fluxo, volume pulmonar e distribuicao em paralelo interagem.", "Abre resistencia, complacencia, constante de tempo e heterogeneidade regional."),
    ("r01-flow-volume-loop.svg", "Flow-volume-loop.svg", "Respira 01", "Loop fluxo-volume", "CC BY-SA 3.0", "Leia o ramo expiratorio, o pico de fluxo e a concavidade; compare a forma, nao apenas valores isolados.", "Um loop esquematico nao diagnostica sozinho obstrucao nem substitui qualidade tecnica da espirometria.", "Conecta mecanica espontanea a limitacao de fluxo e aprisionamento."),
    ("r02-oxyhemoglobin.svg", "Oxygen-Haemoglobin dissociation curves.svg", "Respira 02", "Curva de dissociacao oxigenio-hemoglobina", "Licenca livre indicada na pagina-fonte", "Separe o plato, onde grande variacao de PaO2 pouco muda saturacao, da porcao ingreme, onde pequenas quedas custam muito conteudo ligado a Hb.", "Saturacao nao e conteudo arterial: anemia grave pode manter SpO2 com CaO2 baixo.", "Prepara P50, efeito Bohr, CaO2 e entrega sistemica de oxigenio."),
    ("r02-pulse-oximeter.jpg", "Pulse oximeter.jpg", "Respira 02", "Oximetria no mundo real", "Licenca livre indicada na pagina-fonte", "Observe sensor, local de medida e contexto perfusional; o numero depende de sinal pulsatil e nao mede ventilacao.", "Nao tratar SpO2 como gasometria, PaO2, PaCO2 ou prova de perfusao adequada.", "Ancora dis-hemoglobinas, baixa perfusao, movimento e limites da oximetria."),
    ("r03-vq-mismatch.jpg", "Missmatch V-P Szintigrahie der Lunge bei Lungenembolie 58M - NM - 001.jpg", "Respira 03", "Mismatch ventilacao-perfusao", "Licenca livre indicada na pagina-fonte", "Compare distribuicao ventilatoria e perfusional e procure territorio ventilado que perdeu perfusao.", "A imagem demonstra um mecanismo regional; nao representa toda hipoxemia nem quantifica automaticamente gravidade hemodinamica.", "Diferencia V/Q baixo, shunt e espaco morto."),
    ("r03-vq-paired.jpg", "Gamma Camera Scan of Ventilation and Perfusion of Lungs.jpg", "Respira 03", "Ventilacao e perfusao lado a lado", "Licenca livre indicada na pagina-fonte", "Leia os dois mapas como pares: cada unidade alveolar precisa receber gas e sangue para trocar eficientemente.", "Imagem pequena e historica nao deve ser usada para decisao diagnostica contemporanea isolada.", "Transforma V/Q em geografia pulmonar visivel."),
    ("r04-davenport.jpg", "Davenport fig 5.jpg", "Respira 04", "Diagrama de Davenport", "Licenca livre indicada na pagina-fonte", "Localize pH, bicarbonato e linhas de PaCO2 antes de seguir o deslocamento respiratorio ou metabolico.", "Nao decorar quadrantes sem verificar cronologia, compensacao esperada e disturbios mistos.", "Organiza Henderson-Hasselbalch como mapa, nao como lista."),
    ("r04-acid-base.svg", "Acid-base nomogram.svg", "Respira 04", "Nomograma acido-base", "Licenca livre indicada na pagina-fonte", "Use a posicao conjunta de pH, PaCO2 e bicarbonato para testar coerencia interna.", "Nomograma nao substitui anion gap, delta-delta, lactato nem contexto clinico.", "Faz ponte para compensacoes e narrativas gasometricas complexas."),
    ("r05-alveolus.png", "Pulmonary Alveolus (NIH BioArt 567).png", "Respira 05", "Unidade alveolo-capilar", "NIH BioArt; reutilizacao conforme pagina-fonte", "Identifique pneumocitos, capilar, intersticio e a distancia minima para difusao gasosa.", "O desenho aumenta escalas diferentes; nao inferir espessuras ou proporcoes quantitativas.", "Abre barreira de difusao, edema, lesao epitelial e reparo."),
    ("r05-respiratory-zone.jpg", "2309 The Respiratory Zone.jpg", "Respira 05", "Zona respiratoria", "CC BY 3.0", "Siga bronquiolo respiratorio, ductos e sacos alveolares e note onde conducao se transforma em troca.", "Nao confundir bronquiolo terminal com unidade de troca efetiva.", "Conecta arquitetura, area de troca, Laplace e surfactante."),
    ("r06-pneumonia.jpg", "X-ray of lobar pneumonia.jpg", "Respira 06", "Consolidacao lobar", "Licenca livre indicada na pagina-fonte", "Procure opacidade focal e distribuicao anatomica; relacione preenchimento alveolar a shunt e baixa resposta ao oxigenio.", "Radiografia isolada nao identifica agente nem separa sempre pneumonia de atelectasia ou edema.", "Abre o atlas sindromico por mecanismo alveolar."),
    ("r06-pulmonary-edema.jpg", "Pulmonary oedema.jpg", "Respira 06", "Edema pulmonar", "Licenca livre indicada na pagina-fonte", "Observe padrao bilateral e sinais de comprometimento intersticial/alveolar; pense em agua extravascular e queda de complacencia.", "Padrao radiologico nao define sozinho origem cardiogenica ou permeabilidade aumentada.", "Contrasta edema, SDRA e pneumonia dentro da mesma falha de troca."),
    ("r06-pneumothorax.jpg", "Pneumothorax CXR.jpg", "Respira 06", "Pneumotorax", "Licenca livre indicada na pagina-fonte", "Procure linha pleural, ausencia periferica de trama e sinais de deslocamento mediastinal.", "Nao esperar radiografia quando a instabilidade exige reconhecimento e tratamento imediatos.", "Mostra falha pleural mecanica, distinta de falha alveolar."),
    ("r08-venturi-mask.png", "Adult with air entrainment (Venturi) mask.png", "Respira 08", "Mascara de Venturi", "Licenca livre indicada na pagina-fonte", "Identifique entrada de oxigenio e portas de arraste de ar; a geometria produz FiO2 mais previsivel quando o fluxo total supera demanda.", "Cor do adaptador e fluxo recomendado dependem do fabricante; a figura nao autoriza decorar valores universais.", "Abre FiO2, fluxo total, demanda inspiratoria e dispositivos controlados."),
    ("r08-bipap.jpg", "BIPAP.JPG", "Respira 08", "Ventilacao nao invasiva aplicada", "CC BY-SA 4.0", "Observe interface, vedacao, circuito e relacao paciente-maquina; pressao so chega ao sistema se a interface funcionar.", "Foto nao demonstra indicacao, ajuste correto nem tolerancia; vazamento e risco de aspiracao continuam clinicos.", "Conecta CPAP/BiPAP a recrutamento, descarga muscular e monitorizacao de falha."),
    ("v00-servo-i.jpg", "Servo I Ventilator.jpg", "Ventila 00", "Painel de um ventilador real", "Licenca livre indicada na pagina-fonte", "Separe variaveis ajustadas, monitoradas e alarmes; procure onde o aparelho explicita o contrato do modo.", "Nao transferir menus ou nomes proprietarios para todos os ventiladores.", "Materializa a gramatica pressao-fluxo-volume-tempo."),
    ("v00-mechanical-ventilators.png", "Mechanical Ventilators.png", "Ventila 00", "Ventiladores e diversidade de interfaces", "Licenca livre indicada na pagina-fonte", "Compare como equipamentos distintos exibem controles semelhantes por linguagens diferentes.", "Interface diferente nao significa fisiologia diferente; nome comercial nao substitui taxonomia do modo.", "Treina traducao entre maquinas."),
    ("v01-intubation-kit.jpg", "Intubation endotracheal tube laryngoscope.jpg", "Ventila 01", "Laringoscopio e tubo", "CC BY 3.0", "Reconheca que entrar no ventilador exige primeiro via aerea, posicionamento e estrategia de seguranca.", "A foto nao ensina sequencia rapida, dose, confirmacao por capnografia ou resgate de via aerea dificil.", "Ancora o tubo como intervencao, nao como diagnostico."),
    ("v02-endotracheal-tube.png", "Endotracheal Tube.png", "Ventila 02", "Tubo endotraqueal e cuff", "CC BY conforme pagina-fonte", "Observe conector, marcacoes, cuff e linha de insuflacao; cada componente introduz resistencia, volume compressivel e risco.", "Cuff nao deve ser interpretado como selo absoluto nem inflado por intuicao.", "Abre resistencia do tubo, vazamento, pressao do cuff e lesao traqueal."),
    ("v02-tube-position.jpg", "Airway with endotracheal tube, showing the position of an ET tube in the trachea.jpg", "Ventila 02", "Posicao do tubo na via aerea", "CC BY-SA 4.0", "Siga ponta, traqueia e carina; conecte profundidade a ventilacao unilateral e deslocamento com posicao cervical.", "Desenho anatomico nao substitui capnografia, exame e confirmacao de profundidade.", "Transforma mau posicionamento em causa mecanica antes de culpar o pulmao."),
    ("v03-pressures.png", "Ventilator pressures labeled.png", "Ventila 03", "Pressao de pico, plato e PEEP", "Licenca livre indicada na pagina-fonte", "Separe componente resistivo de elastico: pico inclui ambos; plato aproxima pressao alveolar em pausa adequada.", "Plato invalido com esforco, vazamento ou pausa inadequada nao deve alimentar calculos automaticos.", "Abre driving pressure e diagnostico pico versus plato."),
    ("v03-flow-time.jpg", "Ventilatorwaveformsflowtime.jpg", "Ventila 03", "Curva fluxo-tempo", "Licenca livre indicada na pagina-fonte", "Observe forma inspiratoria e se o fluxo expiratorio retorna a zero antes do proximo ciclo.", "Auto-PEEP pode existir sem ser visualmente obvia; confirmar com contexto e manobras apropriadas.", "Torna aprisionamento e constante de tempo visiveis."),
    ("v04-static-pv.jpg", "Airway pressure release ventilation static pressure-volume figure 2007.jpg", "Ventila 04", "Curva pressao-volume estatica", "Licenca livre indicada na pagina-fonte", "Localize inflexoes, complacencia e regiao de hiperdistensao; leia a curva como comportamento do sistema.", "Pontos de inflexao nao fornecem PEEP universal nem provam recrutabilidade individual.", "Abre loops, histerese e custo da pressao."),
    ("v05-mechanical-ventilator.jpg", "Mechanical ventilator.jpg", "Ventila 05", "VCV em equipamento real", "Licenca livre indicada na pagina-fonte", "Procure volume e fluxo definidos e pressao resultante; relacione mudanca de mecanica a mudanca de pressao.", "A fotografia nao confirma modo ativo nem ajuste adequado ao paciente.", "Ancora a inversao causal do VCV."),
    ("v06-biology-ventilation.gif", "Biology of ventilation.gif", "Ventila 06", "Pressao positiva e insuflacao", "Licenca livre indicada na pagina-fonte", "Acompanhe pressao aplicada, expansao e troca; em PCV, tempo e gradiente determinam o volume entregue.", "Animacao simplifica parede toracica, esforco e heterogeneidade regional.", "Ancora a inversao causal do PCV."),
    ("v08-cpap.png", "CPAP.png", "Ventila 08", "CPAP como pressao basal", "CC BY-SA 3.0", "Leia CPAP como pressao continua sem ciclos mandatarios; o paciente continua produzindo ventilacao minuto.", "CPAP nao e sinonimo de suporte inspiratorio nem garante ventilacao alveolar.", "Distingue CPAP, PSV e modos mandatarios."),
    ("v08-niv.jpg", "Non-invasive ventilation.jpg", "Ventila 08", "Interface de ventilacao nao invasiva", "CC BY 3.0", "Observe apoio, vedacao e pontos de pressao; conforto e vazamento modificam sincronia e eficacia.", "Nao generalizar interface nem presumir protecao de via aerea.", "Abre gatilho, ciclagem, vazamento e falha da VNI."),
    ("v08-cpap-patient.png", "Depiction of a Sleep Apnea patient using a CPAP machine.png", "Ventila 08", "Circuito paciente-interface", "Licenca livre indicada na pagina-fonte", "Siga maquina, tubo e mascara e identifique onde resistencia e vazamento podem aparecer.", "Ilustracao domiciliar nao representa suporte agudo nem monitorizacao de UTI.", "Ajuda a separar principio fisico de contexto assistencial."),
    ("v10-syringe-pump.jpg", "Syringe infusion pump.jpg", "Ventila 10", "Bomba de seringa", "CC BY-SA 4.0", "Observe que sedacao e drogas vasoativas chegam por sistemas com programacao, atraso, oclusao e concentracao.", "Foto de bomba nao valida dose, compatibilidade ou programacao.", "Traz farmacologia para a seguranca operacional."),
    ("v10-icu-infusion.jpg", "3rd Medical Battalion nurses and Corpsmen conduct ICU training 200424-M-RB959-1029 (49863735818).jpg", "Ventila 10", "Bombas no ecossistema da UTI", "Dominio publico dos EUA", "Leia linhas, bombas e monitorizacao como um sistema; sedacao, hemodinamica e ventilacao mudam juntas.", "Cena de treinamento nao deve ser apresentada como protocolo universal.", "Contextualiza titulacao, vigilancia e erro de sistema."),
    ("v13-tracheostomy-types.svg", "Diagram showing a fenestrated and a non fenestrated tracheostomy tube CRUK 066.svg", "Ventila 13", "Canulas fenestrada e nao fenestrada", "Cancer Research UK open knowledge", "Compare trajeto do fluxo, fenestra e relacao com fala, cuff e via aerea superior.", "Fenestra nao significa automaticamente fala segura; posicao, cuff e permeabilidade precisam ser avaliados.", "Abre escolha de canula, desmame e decanulacao."),
    ("v13-tracheostomy-tube.jpg", "Tracheostomy tube.jpg", "Ventila 13", "Canula de traqueostomia real", "Licenca livre indicada na pagina-fonte", "Identifique flange, cuff, conector, canula interna e obturador quando presentes.", "Modelos variam; nunca assumir componentes ou compatibilidade pela aparencia.", "Conecta anatomia a higiene, resistencia e emergencias."),
    ("v13-head-neck-tracheostomy.jpg", "Head neck tracheostomy.jpg", "Ventila 13", "Traqueostomia na anatomia cervical", "Licenca livre indicada na pagina-fonte", "Siga o estoma diretamente ate a traqueia e perceba o bypass da via aerea superior.", "Diagrama nao mostra trajetos falsos, sangramento ou variacoes anatomicas.", "Explica espaco morto, umidificacao e perda de funcoes nasais."),
    ("v17-ards-xray.jpg", "ARDS X-Ray.jpg", "Ventila 17", "Radiografia de SDRA", "GFDL", "Observe opacidades bilaterais e heterogeneidade; conecte imagem a pulmao pequeno funcional, sem inferir recrutabilidade.", "Radiografia nao mede potencial de recrutamento nem separa por si edema hidrostatico.", "Complementa a imagem de progressao ja arquivada."),
    ("v18-emphysema-ct.jpg", "Emphysema CT.JPG", "Ventila 18", "Enfisema em tomografia", "CC BY", "Procure areas de baixa atenuacao e destruicao do parenquima; relacione a perda de recolhimento elastico e expiracao prolongada.", "Imagem de enfisema terminal nao representa todo paciente obstrutivo nem determina ajuste ventilatorio isolado.", "Explica tempo expiratorio, colapso dinamico e auto-PEEP."),
    ("v20-transcranial-doppler.jpg", "Transcranial doppler.jpg", "Ventila 20", "Janela e insonacao transcraniana", "Licenca livre indicada na pagina-fonte", "Observe posicionamento do transdutor e territorio interrogado; Doppler mede velocidade, nao fluxo cerebral absoluto.", "Indice de pulsatilidade nao e monitor direto e infalivel de PIC.", "Conecta PaCO2, resistencia cerebral e neuromonitorizacao."),
    ("v20-tcd-waveform.png", "Transcranial doppler ultrasonography of normal middle cerebral artery flow.png", "Ventila 20", "Espectro Doppler da cerebral media", "CC BY 4.0", "Leia sistole, diastole e envelope espectral antes de calcular indices.", "Traçado normal de referencia nao autoriza metas universais nem substitui tendencia individual.", "Mostra como ventilacao pode mudar hemodinamica cerebral."),
    ("v23-ecmo-cannulas.png", "Ecmo-cannulas.png", "Ventila 23", "Canulacao neonatal para ECMO", "Licenca livre indicada na pagina-fonte", "Siga drenagem e retorno e reconheca que configuracao define recirculacao, descarga e riscos vasculares.", "Esquema neonatal nao representa todas as configuracoes VV/VA adultas.", "Abre canulacao, fluxo de sangue e suporte versus cura."),
    ("v23-ecmo-schema.png", "Ecmo schema-1-de.png", "Ventila 23", "Circuito extracorporeo", "Licenca livre indicada na pagina-fonte", "Siga paciente, bomba, oxigenador e retorno; separe fluxo sanguineo de sweep gas.", "Diagrama simplificado nao mostra todos os sensores, shunts, alarmes ou complicacoes.", "Prepara ultraprotectao e fisiologia do oxigenador."),
    ("v24-alpha1-ct.jpeg", "Alpha 1-antitrypsine deficiency lung CT scan.JPEG", "Ventila 24", "Tomografia e heterogeneidade mecanica", "Licenca livre indicada na pagina-fonte", "Observe distribuicao basal de enfisema e bolhas; diferentes regioes recebem volume e pressao de modo desigual.", "A imagem ilustra parenquima, nao o componente de parede toracica ou pressao abdominal.", "Complementa a separacao entre complacencia pulmonar e do sistema."),
]


def commons_url(filename: str) -> str:
    canonical = filename.replace(" ", "_")
    digest = hashlib.md5(canonical.encode("utf-8")).hexdigest()
    quoted = urllib.parse.quote(canonical, safe="()!,'-._~")
    return f"https://upload.wikimedia.org/wikipedia/commons/{digest[0]}/{digest[:2]}/{quoted}"


def source_page(filename: str) -> str:
    return "https://commons.wikimedia.org/wiki/File:" + urllib.parse.quote(filename.replace(" ", "_"), safe="()!,'-._~")


def fetch_url(url: str) -> str:
    return "https://i0.wp.com/" + url.removeprefix("https://")


def signature_ok(path: pathlib.Path) -> bool:
    head = path.read_bytes()[:512].lstrip()
    suffix = path.suffix.lower()
    if suffix in {".jpg", ".jpeg"}:
        return head.startswith(b"\xff\xd8\xff")
    if suffix == ".png":
        return head.startswith(b"\x89PNG\r\n\x1a\n")
    if suffix == ".gif":
        return head.startswith((b"GIF87a", b"GIF89a"))
    if suffix == ".svg":
        return b"<svg" in head
    return False


def download(url: str, target: pathlib.Path) -> None:
    request = urllib.request.Request(url, headers={"User-Agent": "RespiraEducationalProject/2.0 open-media archival", "Accept": "*/*"})
    last_error = None
    for attempt in range(6):
        try:
            with urllib.request.urlopen(request, timeout=120) as response:
                target.write_bytes(response.read())
            if not signature_ok(target):
                raise ValueError(f"unexpected signature for {target.name}")
            return
        except Exception as exc:
            last_error = exc
            target.unlink(missing_ok=True)
            time.sleep(min(90, 5 * (2 ** attempt)))
    raise RuntimeError(f"failed to fetch {url}: {last_error}")


def write_docs() -> None:
    manifest = []
    atlas = ["# Atlas aberto · Respira e Ventila", "", "Cada figura e uma entrada didatica: leitura orientada, limite interpretativo e ponte para o modulo. Nenhuma imagem substitui avaliacao clinica, laudo, monitorizacao ou protocolo local.", ""]
    attribution = ["# Attribution · Respira/Ventila open media", "", "Arquivos obtidos do Wikimedia Commons. A pagina-fonte vinculada e a referencia legal final para autoria, versao da licenca e historico do arquivo.", "", "| Arquivo local | Modulo | Fonte | Licenca |", "|---|---|---|---|"]
    for local, source, module, title, license_name, reading, pitfall, bridge in ITEMS:
        target = OUT / local
        if not target.exists() or not signature_ok(target):
            raise RuntimeError(f"missing or invalid downloaded file: {target}")
        raw = target.read_bytes()
        page = source_page(source)
        manifest.append({"file": local, "module": module, "title": title, "source_filename": source, "source_page": page, "download_url": commons_url(source), "license": license_name, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(), "what_to_look": reading, "pitfall": pitfall, "bridge": bridge})
        atlas.extend([f"## {module} · {title}", "", f"![{html.escape(title)}](media/{urllib.parse.quote(local)})", "", f"**O que olhar.** {reading}", "", f"**Armadilha que a figura evita.** {pitfall}", "", f"**Ponte didatica.** {bridge}", "", f"**Credito.** [{source}]({page}) · {license_name}.", ""])
        attribution.append(f"| `{local}` | {module} | [{source}]({page}) | {license_name} |")
    (OUT / "MANIFEST.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (OUT.parent / "ATLAS.md").write_text("\n".join(atlas) + "\n", encoding="utf-8")
    (OUT / "ATTRIBUTION.md").write_text("\n".join(attribution) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--index", type=int)
    parser.add_argument("--manifest-only", action="store_true")
    args = parser.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    if args.manifest_only:
        write_docs()
        return
    if args.index is None or not 0 <= args.index < len(ITEMS):
        raise SystemExit(f"--index must be between 0 and {len(ITEMS) - 1}")
    local, source, *_ = ITEMS[args.index]
    target = OUT / local
    download(fetch_url(commons_url(source)), target)
    print(f"{local}: {target.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
