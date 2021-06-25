#!/bin/bash

OUTFILE="$1"
shift
echo "" > "$OUTFILE"
if [ $? -ne 0 ]; then
  echo "No hay permisos para escribir en $OUTFILE"
  exit 1
fi
OUTFILE=$(realpath "$OUTFILE")
source "$(dirname "$0")/func.sh"

if [[ $OUTFILE == *.html ]]; then
  echo '
<!DOCTYPE html>
<html>
<head>
 <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
 <title>'"$@"'</title>
</head>
<body>
' >> "$OUTFILE"
fi

for ZP in "$@";do
  if [ -z "$ZP" ] || [ ! -f "$ZP" ]; then
    echo "Ha de pasar un fichero zip/7z como parámetro" >> /dev/stderr
    exit 1
  fi
  if [[ $ZP != *.zip ]] && [[ $ZP != *.7z ]]; then
    echo "$ZP no es un tipo de fichero admitido" >> /dev/stderr
    exit 1
  fi

  ZP=$(realpath "$ZP")
  UNZP="${ZP%.*}"
  if [ -d "$UNZP" ]; then
    pushd "$UNZP" > /dev/null
  else
    pushd $(mktemp -d) > /dev/null
    lszip "$ZP" | while IFS= read FL; do
      if [[ $FL == */ ]]; then
        mkdir -p "$FL"
      else
        touch "$FL"
      fi
    done

    cln
    MAINDIR=""
    if [ $(ls -A . | wc -l) -eq 1 ]; then
      cd *
      MAINDIR="$(basename $(pwd))"
    fi
  fi
  BZP=$(basename "$ZP")
  if [[ $OUTFILE == *.txt ]]; then
    echo $BZP >> "$OUTFILE"
    tree -I '000 Resumenes' | head -n-1 | tail -n+2 >> "$OUTFILE"
  elif [[ $OUTFILE == *.html ]]; then
    #echo "<h1>$BZP</h1>" >> "$OUTFILE"
    echo "<pre><code>" >> "$OUTFILE"
    tree -I '000 Resumenes' -H . -C | grep '<a .*href="' | \
    sed "s|href=\"\.\">.</a><br>|href=\".\">$BZP</a><br>|" | \
    sed -e "s|&nbsp;| |g" -e "s|<br>||g" -e "s|^\s*||g" | \
    sed -e "s|<a |<span |g" -e "s|</a>|</span>|g" | \
    sed -E 's|href="\./?|title="|g' | \
    sed -e "s|title=\"\"|title=\"${MAINDIR}\"|g" -e 's|/"|"|g' >> "$OUTFILE"
  fi
  popd > /dev/null
done

if [[ $OUTFILE == *.html ]]; then
  echo "</code></pre></body></html>" >> "$OUTFILE"
fi

sed -i -e '/./,$!d' -e :a -e '/^\n*$/{$d;N;ba' -e '}' "$OUTFILE"
