#!/usr/bin/env bash
# Build a clean public bundle in dist/ — only files safe to put on the web.
# Excludes Assets/, tools/, content/, editor config, and notes.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DIST="$ROOT/dist"

rm -rf "$DIST"
mkdir -p "$DIST"

cp "$ROOT"/*.html "$DIST/"
cp -R "$ROOT/css" "$ROOT/js" "$ROOT/images" "$DIST/"

for f in robots.txt sitemap.xml _headers _redirects favicon.ico; do
  if [[ -f "$ROOT/$f" ]]; then
    cp "$ROOT/$f" "$DIST/"
  fi
done

# Never ship source-only or private material
rm -rf "$DIST/Assets" "$DIST/tools" "$DIST/content" "$DIST/.claude" 2>/dev/null || true

echo "Deploy bundle ready: $DIST"
du -sh "$DIST" | awk '{print "  size:", $1}'
echo "  html:" $(find "$DIST" -name '*.html' | wc -l)
echo "  images:" $(find "$DIST/images" -type f 2>/dev/null | wc -l)
