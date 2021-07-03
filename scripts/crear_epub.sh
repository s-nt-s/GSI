#!/bin/bash
cd "$(dirname "$0")"

cd ../content/posts/gsitic.wordpress.com/
rm *.epub

for md in *.md; do
    epub="${md%.*}.epub"
    miepub --trim --width 1050 --out $epub $md
    echo ""
done
