#!/usr/bin/env python3
import os
import json
from datetime import datetime

COACH_MIC_EXPORTS_DIR = os.path.expanduser("~/Coach_Mic_Agent/exports")
BLOG_OUTPUT_DIR = "blog/posts"

def read_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return None

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

if not os.path.exists(COACH_MIC_EXPORTS_DIR):
    print(f"❌ Export-Verzeichnis nicht gefunden: {COACH_MIC_EXPORTS_DIR}")
    exit(1)

projects = [d for d in os.listdir(COACH_MIC_EXPORTS_DIR) if os.path.isdir(os.path.join(COACH_MIC_EXPORTS_DIR, d))]

if not projects:
    print("⚠️  Keine Coach Mic Projekte gefunden")
    exit(0)

print(f"📁 Gefundene Projekte: {len(projects)}")
print("✅ Converter bereit!")
