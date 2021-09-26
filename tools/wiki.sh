#!/bin/bash
LG="$2"
if [ -z "$LANG" ]; then
LG="es"
fi
curl -s "https://${LG}.wikipedia.org/w/api.php" -d 'action=parse' -d 'format=json' -d 'prop=wikitext' -d 'formatversion=2' -d "page=$1" | jq -r '.parse.wikitext' | /usr/bin/pandoc --markdown-headings=atx -f mediawiki -t markdown -s - -o -
