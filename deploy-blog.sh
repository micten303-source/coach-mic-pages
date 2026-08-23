#!/bin/bash
set -e

echo "🚀 Coach Mic Blog Deployment"
echo "=============================="

python3 convert-to-blog.py

if ! git diff --quiet blog/; then
    echo "✓ Neue Blog-Posts gefunden"
    git add blog/
    git commit -m "🤖 Coach Mic: Blog automatisch aktualisiert"
    git push origin main
    echo "✅ Fertig!"
else
    echo "⚠️  Keine Änderungen gefunden"
fi
