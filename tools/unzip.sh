#!/bin/bash

if [ -z "$1" ] || [ ! -f "$1" ]; then
  echo "$ZP no existe"
  exit 1
fi
ZP="$(realpath "$1")"
TARGET="${ZP%.*}"
if [ -e "$TARGET" ]; then
  echo "$TARGET ya existe, eliminelo antes de continuar"
  echo "rm -R \"$TARGET\""
  exit 1
fi

source "$(dirname "$0")/func.sh"

pushd $(mktemp -d)
uzip "$ZP"
cln

if [ $(ls -A . | wc -l) -eq 1 ]; then
  cd *
fi
UNZIPPED="$(pwd)"
popd > /dev/null

mv "$UNZIPPED" "$TARGET"
