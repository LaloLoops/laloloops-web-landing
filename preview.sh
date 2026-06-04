#!/usr/bin/env bash
# Build local preview content and serve the site over HTTP.
#
# The site's loop/article detail pages and manifest-driven listings are normally
# produced by the GitHub Actions deploy pipeline from the `content` branch, so
# they don't exist when you open files locally. This script reproduces them
# locally (preview/build.py) and serves over HTTP so the runtime manifest
# fetches and root-relative links work.
#
# Usage:  ./preview.sh [PORT]      (default port: 8000)
# Then open http://localhost:PORT/  (try /loops/ and, once it exists, /articles/)
set -euo pipefail

PORT="${1:-8000}"
cd "$(dirname "$0")"

echo "Building local preview content..."
python3 preview/build.py

echo
echo "Serving http://localhost:${PORT}/  (Ctrl+C to stop)"
exec python3 -m http.server "${PORT}"
