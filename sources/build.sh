#!/usr/bin/env bash
# Single-command editable UFO build (development reproducibility check).
set -euo pipefail
cd "$(dirname "$0")/.."
python3 sources/build_from_ufo.py
echo "Development build written to build/Tekryno-Regular.ttf"
echo "Compare built font with approved fonts/ttf/Tekryno-Regular.ttf before release."
