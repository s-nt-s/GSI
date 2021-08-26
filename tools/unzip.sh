#!/bin/bash

source "$(dirname "$0")/func.sh"

if [ -z "$1" ] || [ ! -f "$1" ]; then
  echo "$ZP no existe"
  exit 1
fi
ZP="$(realpath "$1")"
TARGET=$(zip_to_target "$ZP")

if [ -e "$TARGET" ]; then
  echo "$TARGET ya existe, eliminelo antes de continuar"
  echo "rm -R \"$TARGET\""
  exit 1
fi

pushd $(mktemp -d)
uzip "$ZP"
cln "HARD"

if [ $(ls -A . | wc -l) -eq 1 ]; then
  cd *
fi
UNZIPPED="$(pwd)"
popd > /dev/null

D_TARGET=$(dirname "$TARGET")
if [ ! -d "$D_TARGET" ]; then
  mkdir -p "$D_TARGET"
fi
mv "$UNZIPPED" "$TARGET"

function mklink() {
  file="$1"
  tail="$2"
  ext="${file##*.}"
  fld="$(echo $file | cut -d'/' -f2)"
  trg="${fld}${tail}.${ext}"
  if [ -e "$trg" ]; then
    trg="${fld}${tail}_bis.${ext}"
  fi
  ln -s "$file" "$trg"
}

cd "$TARGET"
ZP=$(basename "$ZP")
if [ "$ZP" == "Pack_1_PreparaTIC27.zip" ]; then
  mkdir '000 Resumenes'
  cd '000 Resumenes'
  find .. -ipath "*/contenidos/*resumen*" -iname "*amplio*" -print0 |
  while IFS= read -r -d '' file; do
    mklink "$file" "_amplio"
  done
  find .. -ipath "*/contenidos/*resumen*" -iname "*express*" -print0 |
  while IFS= read -r -d '' file; do
    mklink "$file" "_express"
  done
  find .. -ipath "*/contenidos/*resumen*" ! -iname "*amplio*" ! -iname "*express*" -print0 |
  while IFS= read -r -d '' file; do
    mklink "$file" ""
  done
fi

echo ""
echo "SALIDA en: $TARGET"
