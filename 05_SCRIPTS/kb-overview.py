#!/usr/bin/env python3
"""
kb-overview.py — read-only overzicht van de AI Capability KB (laag 1).
Leest alleen. Schrijft niets, commit niets, raakt de harde grens niet.

Toont per kaart: titel, type, status, completeness, trust level.
Daarna: git working tree per project.

Gebruik:  python3 kb-overview.py [pad-naar-kb]
Default pad: de map waarin dit script staat, twee niveaus omhoog (de KB-root).
"""

import os
import re
import sys
import subprocess
from pathlib import Path

# --- Configuratie ----------------------------------------------------------
# Mappen die echte kaarten bevatten.
KAART_MAPPEN = ["01_CAPABILITIES", "02_KNOWLEDGE"]
# Bestandsnamen/mappen die geen kaart zijn en overgeslagen worden.
SKIP_NAMEN = {"README.md"}
SKIP_MAPPEN = {"06_EXAMPLES", ".git", ".obsidian", "node_modules"}

VELDEN = {
    "type": re.compile(r"^\s*-\s*\*\*Type:\*\*\s*(.*)$", re.IGNORECASE),
    "status": re.compile(r"^\s*-\s*\*\*Status:\*\*\s*(.*)$", re.IGNORECASE),
    "completeness": re.compile(r"^\s*-\s*\*\*Completeness-status:\*\*\s*(.*)$", re.IGNORECASE),
    "trust": re.compile(r"^\s*-\s*\*\*Trust level:\*\*\s*(.*)$", re.IGNORECASE),
}

# --- Helpers ---------------------------------------------------------------
def lees_kaart(pad):
    velden = {k: "" for k in VELDEN}
    titel = pad.stem
    try:
        with open(pad, encoding="utf-8") as f:
            for regel in f:
                # eerste # kop = titel
                if titel == pad.stem and regel.startswith("# "):
                    titel = regel[2:].strip()
                for naam, patroon in VELDEN.items():
                    if not velden[naam]:
                        m = patroon.match(regel)
                        if m:
                            velden[naam] = m.group(1).strip()
    except Exception as e:
        return titel, velden, f"(leesfout: {e})"
    return titel, velden, None


def verzamel_kaarten(kb_root):
    kaarten = []
    for mapnaam in KAART_MAPPEN:
        basis = kb_root / mapnaam
        if not basis.is_dir():
            continue
        for pad in sorted(basis.rglob("*.md")):
            if any(deel in SKIP_MAPPEN for deel in pad.parts):
                continue
            if pad.name in SKIP_NAMEN:
                continue
            titel, velden, fout = lees_kaart(pad)
            rel = pad.relative_to(kb_root)
            kaarten.append((rel, titel, velden, fout))
    return kaarten


def git_status_kort(pad):
    if not (pad / ".git").is_dir():
        return f"  {pad.name}: (geen git-repo)"
    try:
        tak = subprocess.run(
            ["git", "-C", str(pad), "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True, text=True, timeout=10
        ).stdout.strip()
        uit = subprocess.run(
            ["git", "-C", str(pad), "status", "--porcelain"],
            capture_output=True, text=True, timeout=10
        ).stdout.strip()
        if not uit:
            return f"  {pad.name} [{tak}]: schoon"
        n = len(uit.splitlines())
        return f"  {pad.name} [{tak}]: {n} gewijzigd/ongetrackt bestand(en)"
    except Exception as e:
        return f"  {pad.name}: (git-fout: {e})"


# --- Hoofd -----------------------------------------------------------------
def main():
    if len(sys.argv) > 1:
        kb_root = Path(sys.argv[1]).expanduser().resolve()
    else:
        kb_root = Path(__file__).resolve().parent.parent

    if not kb_root.is_dir():
        print(f"KB-map niet gevonden: {kb_root}")
        sys.exit(1)

    kaarten = verzamel_kaarten(kb_root)

    print("=" * 64)
    print(f"  KB-OVERZICHT  ·  {kb_root}")
    print("=" * 64)
    print(f"  Kaarten gevonden: {len(kaarten)}")
    print()

    # Groepeer op status (lege status apart bovenaan zodat gaten opvallen)
    def status_sleutel(k):
        s = k[2]["status"].lower()
        return (s == "", s)  # lege status eerst

    for rel, titel, velden, fout in sorted(kaarten, key=status_sleutel):
        status = velden["status"] or "— leeg —"
        regel = f"  [{status:<10}] {titel}"
        extra = []
        if velden["type"]:
            extra.append(velden["type"])
        if velden["completeness"]:
            extra.append(f"compl: {velden['completeness']}")
        if velden["trust"]:
            extra.append(f"trust: {velden['trust']}")
        if extra:
            regel += "  ·  " + " · ".join(extra)
        print(regel)
        print(f"               {rel}")
        if fout:
            print(f"               {fout}")
    print()

    # Working tree per project
    print("-" * 64)
    print("  WORKING TREE PER PROJECT")
    print("-" * 64)
    dev = kb_root.parent  # ~/dev
    for naam in ["kb", "allure", "operator-one"]:
        projpad = dev / naam
        if projpad.is_dir():
            print(git_status_kort(projpad))
        else:
            print(f"  {naam}: (map bestaat niet op {projpad})")
    print()


if __name__ == "__main__":
    main()
