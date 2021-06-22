#!/bin/bash

function lszip() {
  if [[ $1 == *.zip ]]; then
    unzip -O IBM860 -l "$1" | tail -n+4 | head -n-2 | \
    sed 's|^\s*[0-9][0-9]*\s\s*[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9] [0-9][0-9]:[0-9][0-9]\s\s*||'
  elif [[ $1 == *.7z ]]; then
    7z l -ba -slt "$1" | \
    awk '$1=="Path" && $2=="=" {fl=substr($0,8)} $1=="Attributes" && $2=="=" {if ($3=="D") {fl=fl "/"} print fl}' | \
    sort
  fi
}
function rnm() {
  OLD="$1"
  NEW="$2"
  find . -name "*${OLD}*" -exec rename "s|${OLD}|${NEW}|g" "{}" +
}

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
  pushd $(mktemp -d) > /dev/null
  lszip "$ZP" | while IFS= read FL; do
    if [[ $FL == */ ]]; then
      mkdir -p "$FL"
    else
      touch "$FL"
    fi
  done
  rnm "╜" "ó"
  rnm "α" "Ó"
  rnm "╡" "Á"
  rnm "╓" "Í"
  rnm $'\302\201' ""
  find . -name "*  *" -exec rename "s|\s\s\s*| |g" "{}" +
  find . -type f -name desktop.ini -delete
  find . -type d -empty -delete
  if [ $(ls -A . | wc -l) -eq 1 ]; then
    cd *
  fi
  echo $(basename "$ZP")
  tree  | head -n-1 | tail -n+2
  popd > /dev/null
done
