#!/usr/bin/bash

# Zadatak: Izdvojiti ektenziju fajla koji se zadaje kao prvi argument
# komandne linije.

if [ "$#" -ne 1 ]; then
	echo "Koriscenje: $0 file"
	exit 1
fi

# 1. nacin (cut)
echo "$1" | cut -d'.' -f2-

# 2. nacin (sed)
echo "$1" | sed -E 's/[^.]+\.(.*)/\1/g'

