#!/bin/bash
cd docs/gsitic.wordpress.com/

for html in *.html; do
    epub="${html%.*}.epub"
    sed -E 's/^  (<\/div>|<div class="content">)$//'  $html > tmp.html
    miepub --chapter-level 2 --css ../rec/gsitic_epub.css --trim --width 780 --out $epub tmp.html
    rm tmp.html
    echo ""
done
