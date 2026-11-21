#!/usr/bin/env python3
"""Regenera bancos/index.json a partir de los .txt de esta carpeta.

Uso:  python3 bancos/generar_indice.py

- Lee cada .txt (formato de Q&A Study) y toma el nombre del BLOQUE:,
  la cantidad de preguntas y los temas.
- Conserva la "descripcion" que ya tenga cada archivo en index.json
  (editala a mano en index.json si querés cambiarla).
"""
import json, os, re, datetime

DIR = os.path.dirname(os.path.abspath(__file__))
IDX = os.path.join(DIR, "index.json")

old = {}
if os.path.exists(IDX):
    with open(IDX, encoding="utf-8") as f:
        for b in json.load(f).get("bancos", []):
            old[b.get("archivo")] = b

bancos = []
for name in sorted(os.listdir(DIR)):
    if not name.lower().endswith(".txt"):
        continue
    with open(os.path.join(DIR, name), encoding="utf-8-sig") as f:
        text = f.read()
    m = re.search(r"^\s*BLOQUE\s*:\s*(.+?)\s*$", text, re.M | re.I)
    bloque = m.group(1) if m else os.path.splitext(name)[0]
    preguntas = len(re.findall(r"^\s*PREGUNTA\s*:", text, re.M | re.I))
    temas = sorted({t.strip() for t in re.findall(r"^\s*TEMA\s*:\s*(.+?)\s*$", text, re.M | re.I)})
    prev = old.get(name, {})
    bancos.append({
        "archivo": name,
        "bloque": bloque,
        "descripcion": prev.get("descripcion", ""),
        "preguntas": preguntas,
        "temas": temas,
    })

data = {
    "formato": 1,
    "actualizado": datetime.date.today().isoformat(),
    "bancos": bancos,
}
with open(IDX, "w", encoding="utf-8", newline="\n") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write("\n")
print(f"index.json: {len(bancos)} bancos")
