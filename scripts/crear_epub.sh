#!/bin/bash
DR=$(realpath "$(dirname "$0")/..")

PYPANDOC_PANDOC="$HOME/bin/pandoc"

cd "$DR/content/posts/gsitic.wordpress.com/"

for md in *.md; do
    epub="${md%.*}.epub"
    if [ ! -f "$epub" ]; then
      miepub --trim --width 1050 --out $epub $md
      echo ""
    fi
done

cd "$DR/content/posts/otros/"

if [ ! -f metrica.epub ]; then
  miepub --trim --width 1050 --out metrica.epub metrica_v3.md
fi
