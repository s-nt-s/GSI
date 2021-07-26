#!/bin/bash
cd "$(dirname "$0")/.."
rm -f config/dates.txt
find content/ -name '*.md' -print0 | while IFS= read -r -d '' file; do
    UP=$(git log -1 --format=%ai "$file")
    CR=$(git log --format=%ai "$file" | tail -n 1)
    echo "$file" >> config/dates.txt
    echo "$UP" >> config/dates.txt
    echo "$CR" >> config/dates.txt
    let DIFF=($(date +%s -d "$UP")-$(date +%s -d "$CR"))/86400
    echo $DIFF >> config/dates.txt
    echo "" >> config/dates.txt
done
