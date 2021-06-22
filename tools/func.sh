function rnm() {
  OLD="$1"
  NEW="$2"
  find . -name "*${OLD}*" -execdir rename "s|${OLD}|${NEW}|g" "{}" +
}

function cln() {
  find . -type f -iname "*cambios*.txt" -delete
  find . -type f -name desktop.ini -delete
  find . -type d -empty -delete
  if [ -d Pack_1_PreparaTIC27/Pack_1_PreparaTIC27 ]; then
    rm -R Pack_1_PreparaTIC27/Pack_1_PreparaTIC27
  fi
  find . -type d -regextype posix-egrep -regex '.*/[0-9]+\s*[\.\-]+\s*[^/0-9][^/]*' -execdir rename 's/([0-9][0-9]*)([ \.\-][ \.\-]*)(.*)/$1 $3/' "{}" +

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
    7z e "$1"
  fi
}
