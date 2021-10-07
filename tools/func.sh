function zip_to_target() {
  DR=$(dirname "$1")
  ZP=$(basename "$1")
  if [ "$ZP" == "Pack_1_PreparaTIC27.zip" ]; then
    echo "$DR/27.1-Temario"
  elif [ "$ZP" == "Audioapuntes_Pack1_01.7z" ]; then
    echo "$DR/26.1-Audio/01"
  elif [ "$ZP" == "Audioapuntes_Pack1_02.7z" ]; then
    echo "$DR/26.1-Audio/02"
  elif [ "$ZP" == "Audioapuntes_Pack1_03.7z" ]; then
    echo "$DR/26.1-Audio/03"
  elif [ "$ZP" == "Pack3 casos practicos.zip" ]; then
    echo "$DR/27.3-Volcados"
  elif [ "$ZP" == "Pack3_Material.zip" ]; then
    echo "$DR/27.3-Material"
  else
    echo "$DR/${ZP%.*}"
  fi
}

function rnm() {
  OLD="$1"
  NEW="$2"
  find . -name "*${OLD}*" -execdir rename "s|${OLD}|${NEW}|g" "{}" +
}

function cln() {
  if [ -d Pack_1_PreparaTIC27/Pack_1_PreparaTIC27 ]; then
    rm -R Pack_1_PreparaTIC27/Pack_1_PreparaTIC27
  fi
  find . -type f -iname "*preparatic*cambios*" -delete
  find . -type f -iname "*cambios*.txt" -delete
  find . -type f -name desktop.ini -delete
  find . -regextype posix-egrep -regex ".*/desktop\s*\([0-9]*\)\s*\.ini" -delete
  if [ "$1" == "HARD" ]; then
    find . -type d -execdir fdupes -dN "{}" \;
  fi
  find . -type d -empty -delete
  find . -type d -regextype posix-egrep -regex '.*/[0-9]+\s*[\.\-]+\s*[^/0-9][^/]*' \
         -execdir rename 's/([0-9][0-9]*)([ \.\-][ \.\-]*)(.*)/$1 $3/' "{}" +

  rnm "╜" "ó"
  rnm "α" "Ó"
  rnm "╡" "Á"
  rnm "╓" "Í"
  rnm "ñ" "ñ"
  rnm "é" "é"
  rnm "í" "í"
  rnm "ó" "ó"

  rnm $'\302\201' ""
  find . -name "*  *" -execdir rename "s|\s\s\s*| |g" "{}" +
  find . -type d -name "*_" -execdir rename "s|__*$||g" "{}" +
  find . -type d -name "*An func de sist, CU e HU. Met de desrrll de sist. Met. agiles_ Scrum y Kanban*" -execdir rename "s|An func de sist, CU e HU. Met de desrrll de sist. Met. agiles_ Scrum y Kanban|Análisis funcional de sistemas, CU e HU. Metodologías de desarrollo de sistemas. Metodologías ágiles, Scrum y Kanban|g" "{}" +

  if [ "$2" == "Pack3 casos practicos.zip" ] || [ "$2" == "Audioapuntes_Pack1_01.7z" ]; then
  find . -type f -regextype posix-egrep -regex ".*/[^/]+\S\([0-9]*\)\.[^\.]+" \
         -execdir rename s'|(\S)\([0-9][0-9]*\)(.[^\.]*)$|$1$2|g' "{}" +
  fi
}

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

function uzip() {
  if [[ $1 == *.zip ]]; then
    unzip -qq -O IBM860 "$1"
  elif [[ $1 == *.7z ]]; then
    7z x "$1"
  fi
}
