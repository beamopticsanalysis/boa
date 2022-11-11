#!/bin/bash
set -euo pipefail; IFS=$'\n\t'

NAME="boa"
VER=$( python -c "from pathlib import Path; dd={}; f=open('boa/_version.py', 'r'); exec(f.read(), dd); f.close(); print(dd['__version__'])" )

echo "========================================================================"
echo "Tagging $NAME v$VER"
echo "========================================================================"

git tag v$VER
git push origin v$VER

echo "========================================================================"
echo "Releasing $NAME v$VER on PyPI"
echo "========================================================================"

python -m pip wheel boa
twine check dist/*
twine upload dist/*
rm -r dist/ *.egg-info
