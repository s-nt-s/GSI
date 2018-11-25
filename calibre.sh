#!/bin/bash

IDS=$(calibredb search author:gsitic.wordpress.com)
if [ ! -z "$IDS" ]; then
	calibredb remove $IDS
fi

cd docs/gsitic.wordpress.com/
calibredb add *.epub
IDS=$(calibredb search author:gsitic.wordpress.com)

while IFS=',' read -ra ADDR; do
	for i in "${ADDR[@]}"; do
		calibredb set_custom myshelves "$i" "Oposiciones"
	done
done <<< "$IDS"
