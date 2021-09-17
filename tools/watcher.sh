#/bin/bash

cd "$(dirname "$0")/../"
make build

TEMP="$(mktemp -d)/"

LAST_BUILD=99999999999999999999999999

inotifywait -q -m -e modify -r content config themes/mini myplugins |
while read -r dir event file; do
  file="${dir}${file}"
  if [ -f "$file" ]; then
    BAK="${TEMP}${file}"
    if ! cmp --silent "$BAK" "$file"; then
      SC="$((SECONDS-LAST_BUILD))"
      if [ $SC -gt 5 ]; then
        sleep 2
        mkdir -p "$(dirname "$BAK")"
        cp "$file" "$BAK"
        echo "$file HA CAMBIADO"
        make build
        LAST_BUILD="$SECONDS"
        echo "DONE"
      fi
    fi
  fi
done
