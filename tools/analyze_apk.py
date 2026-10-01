#!/usr/bin/env python3
"""Deterministic APK inventory and evidence collector (stdlib only)."""
from pathlib import Path
import hashlib, json, re, subprocess, sys, zipfile

apk = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("Q07Rusifikator_v1.24.1_settings.apk")
out = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("analysis/artifacts")
out.mkdir(parents=True, exist_ok=True)
h = hashlib.sha256(); size = 0
with apk.open("rb") as f:
    for b in iter(lambda: f.read(1024*1024), b""): h.update(b); size += len(b)
items = []
with zipfile.ZipFile(apk) as z:
    for i in z.infolist():
        data = z.read(i.filename)
        items.append({"name": i.filename, "size": i.file_size, "compressed": i.compress_size,
                      "sha256": hashlib.sha256(data).hexdigest()})
        if i.filename.endswith((".dex", ".jar")):
            strings = subprocess.run(["strings", "-a", "-n", "3"], input=data,
                                     capture_output=True).stdout.decode("utf-8", "replace")
            (out / (Path(i.filename).name + ".strings.txt")).write_text(strings)
manifest = subprocess.run(["apkanalyzer", "manifest", "print", str(apk)], capture_output=True, text=True)
(out / "AndroidManifest.print.xml").write_text(manifest.stdout)
(out / "inventory.json").write_text(json.dumps({"apk": str(apk), "size": size,
    "sha256": h.hexdigest(), "entries": items}, indent=2))
print(json.dumps({"apk": str(apk), "size": size, "sha256": h.hexdigest(), "entries": len(items)}, indent=2))
