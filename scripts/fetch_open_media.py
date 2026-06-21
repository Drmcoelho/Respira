#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import pathlib
import time
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "ventila17-26" / "media"

FILES = [
    ("ventila17-ardsgradation.jpg", "Ardsgradation.jpg"),
    ("ventila18-medical-ventilator.jpg", "Medical ventilator 001.jpg"),
    ("ventila19-right-heart-embolus.ogv", "Right-Heart-Transvalvular-Embolus-with-High-Risk-Pulmonary-Embolism-in-a-Recently-Hospitalized-481357.f1.ogv"),
    ("ventila20-icp-monitor.jpg", "JASDF Intracranial pressure monitoring system at Komaki Air Base February 23, 2014.jpg"),
    ("ventila21-prone-team.jpg", "Navy Medical Team Supports Louisiana Hospital.jpg"),
    ("ventila22-aprv-graph.png", "Airway pressure release ventilation graph.png"),
    ("ventila23-ecmo-h1n1.jpg", "ECMO in H1N1 patient in Santa Cruz Hospital - Lisbon.jpg"),
    ("ventila24-bogota-bag.png", "Bogota bag.png"),
    ("ventila25-premature-infant.jpg", "Premature infant with ventilator.jpg"),
    ("ventila25-neonate-eit.jpeg", "Neonate with electrical impedance tomography electrodes.jpeg"),
    ("ventila26-medumat.jpg", "Medumat plus Absaugeinheit.jpg"),
    ("reserve-transport-ltv1000.JPG", "Intensivrespirator LTV 1000.JPG"),
    ("reserve-right-heart-tte.ogv", "Echocardiographic-diagnosis-management-and-monitoring-of-pulmonary-embolism-with-right-heart-1476-7120-8-18-S2.ogv"),
    ("reserve-icp-waveform.ogv", "Simultaneous-monitoring-of-static-and-dynamic-intracranial-pressure-parameters-from-two-separate-1475-925X-11-66-S3.ogv"),
    ("reserve-neonate-eit-study.png", "EIT ventilation study of infants Heinrich 2006.png"),
]


def commons_url(filename: str) -> str:
    canonical = filename.replace(" ", "_")
    digest = hashlib.md5(canonical.encode("utf-8")).hexdigest()
    quoted = urllib.parse.quote(canonical, safe="()!,'-._~")
    return f"https://upload.wikimedia.org/wikipedia/commons/{digest[0]}/{digest[:2]}/{quoted}"


def signature_ok(path: pathlib.Path) -> bool:
    head = path.read_bytes()[:16]
    suffix = path.suffix.lower()
    if suffix in {".jpg", ".jpeg"}:
        return head.startswith(b"\xff\xd8\xff")
    if suffix == ".png":
        return head.startswith(b"\x89PNG\r\n\x1a\n")
    if suffix == ".ogv":
        return head.startswith(b"OggS")
    return False


def download(url: str, target: pathlib.Path) -> None:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "RespiraEducationalProject/1.0 (GitHub; open-media archival)",
            "Accept": "*/*",
        },
    )
    last_error = None
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=90) as response:
                target.write_bytes(response.read())
            if not signature_ok(target):
                raise ValueError(f"unexpected signature for {target.name}")
            return
        except Exception as exc:  # network retries are intentional here
            last_error = exc
            target.unlink(missing_ok=True)
            time.sleep(2 ** attempt)
    raise RuntimeError(f"failed to fetch {url}: {last_error}")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    manifest = []
    for local_name, source_name in FILES:
        target = OUT / local_name
        url = commons_url(source_name)
        download(url, target)
        raw = target.read_bytes()
        manifest.append(
            {
                "file": local_name,
                "source_filename": source_name,
                "source_url": url,
                "bytes": len(raw),
                "sha256": hashlib.sha256(raw).hexdigest(),
            }
        )
        print(f"{local_name}: {len(raw):,} bytes")

    (OUT / "MANIFEST.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
