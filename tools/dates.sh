#!/bin/bash
cd "$(dirname "$0")/.."
rm -f config/dates.txt
find content/ -name '*.md' -print0 | while IFS= read -r -d '' file; do
    CR=$(git log --format=%ai "$file" | head -n 1)
    UP=$(git log -1 --format=%ai "$file")
    echo "$file" >> config/dates.txt
    echo "$CR" >> config/dates.txt
    echo "$UP" >> config/dates.txt
    let DIFF=($(date +%s -d "$CR")-$(date +%s -d "$UP"))/86400
    echo $DIFF >> config/dates.txt
    echo "" >> config/dates.txt
done
