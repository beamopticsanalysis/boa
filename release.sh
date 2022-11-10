#!/bin/bash
set -euo pipefail; IFS=$'\n\t'

NAME="boac"
VER=$( python -c "from pathlib import Path; dd={}; f=open('boac/_version.py', 'r'); exec(f.read(), dd); f.close(); print(dd['__version__'])" )

echo "========================================================================"
echo "Tagging $NAME v$VER"
echo "========================================================================"

git tag v$VER
git push origin v$VER

echo "========================================================================"
echo "Releasing $NAME v$VER on PyPI"
echo "========================================================================"

python -m build
twine check dist/*
twine upload dist/*
rm -r dist/ *.egg-info
