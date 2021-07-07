#/bin/bash

cd "$(dirname "$0")/../"
TEMP="$(mktemp -d)/"

inotifywait -q -m -e modify -r content |
while read -r dir event file; do
  file="${dir}${file}"
  if [ -f "$file" ]; then
    BAK="${TEMP}${file}"
    if ! cmp --silent "$BAK" "$file"; then
      mkdir -p "$(dirname "$BAK")"
      cp "$file" "$BAK"
      echo "$file HA CAMBIADO"
      make build
    fi
  fi
done
