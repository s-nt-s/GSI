#!/bin/bash

URL="http://regis.cosnier.free.fr/?page=XSDDiagram"
CMD="$(dirname "$0")/xsddiagram/XSDDiagramConsole.exe"
DRY=0

run_xsddiagram() {
  echo "\$ xsddiagram $@"
  if [ $DRY -eq 0 ]; then
    /usr/bin/cli "$CMD" "$@"
  fi
}
get_paths() {
  /usr/bin/cli "$CMD" -f PATH,NAME -os "txt"  "$@" | grep "^/"
}

if [ ! -f "$CMD" ]; then
  DWN=$(lynx -dump -listonly "$URL" | rev | cut -d' ' -f1 | rev | grep -E "^https?://.*/XSDDiagram-.*-Binary.zip" | head -n 1)
  TRG=$(dirname "$CMD")
  mkdir -p "$TRG"
  wget -q -O "$TRG/XSDDiagram.zip" "$DWN"
  unzip -qq "$TRG/XSDDiagram.zip" -d "$TRG/"
  rm "$TRG/XSDDiagram.zip"
fi

if [ ! -f "$CMD" ]; then
  echo "No existe $CMD y no se ha podido descargar de $URL"
  exit 1
fi

if [ $# -eq 0 ]; then
  exec /usr/bin/cli "$CMD"
fi

XSD=""
ROT=""
OSS=0
LVL=""
ARG=(-no-gui -y)
declare -a TYP
FULL_TYP=(csv txt png svg)
re_num='^[0-9]+$'
while (( "$#" )); do
  if [ "$1" == "--dry" ]; then
    DRY=1
  elif [ "$1" == "os" ]; then
    OSS=1
  elif [[ "$1" == http* ]] || [[ "$1" == *.xsd ]]; then
    XSD="$1"
  elif [[ $1 =~ $re_num ]] ; then
    LVL="$1"
    ARG+=('-e')
    ARG+=("$1")
  elif [ -d "$1" ]; then
    TRG="$1"
  elif [[ " ${FULL_TYP[@]} " =~ " $1 " ]]; then
    TYP+=("$1")
  else
    ROT="$1"
    ARG+=('-r')
    ARG+=("$1")
  fi
  shift
done
if [ -z "$XSD" ]; then
  echo "No se ha pasado un .xsd como parametro"
  exit 1
fi
if [ -z "$ROT" ]; then
  echo "No se ha pasado un elemento ROOT"
  exit 1
fi
if [ -z "$TRG" ]; then
  TRG="$(dirname "$0")/../content/posts/xsd/$(basename "$XSD" .xsd)"
fi
if [ ${#TYP[@]} -eq 0 ]; then
  TYP=("${FULL_TYP[@]}")
fi
ABS=$(realpath "$TRG")
TRG=$(realpath --relative-to="$(pwd)" "$ABS")
if [ ${#TRG} -ge ${#ABS} ]; then
  TRG="$ABS"
fi
if [ -z "$LVL" ]; then
  IFS=$'\n' ARR=($(get_paths -e 6 "${ARG[@]}" "$XSD"))
  ELM=$(printf "%s\n" "${ARR[@]}" | awk '{print $1}' | sort | uniq | wc -l)
  LVL=$(printf "%s\n" "${ARR[@]}" | awk '!seen[$2]++ {print gsub(/\//,"", $1)-1}' | sort | tail -n 1)
  while true; do
    CUR=$(get_paths -e "$LVL" "${ARG[@]}" "$XSD" | awk '{print $1}' | sort | uniq | wc -l)
    if [[ $ELM -le $CUR ]]; then
      break
    fi
    LVL=$(($LVL + 1))
  done
  ARG+=('-e')
  ARG+=("$LVL")
fi
for i in "${TYP[@]}"; do
  if [ $OSS -eq 1 ]; then
    run_xsddiagram "${ARG[@]}" -os "$i" "$XSD"
  else
    run_xsddiagram "${ARG[@]}" -o "$TRG/$ROT.$i" "$XSD"
  fi
done
