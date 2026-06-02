#!/usr/bin/bash

# Zadatak: Kao jedini argument komandne linije se unosi putanja do fajla koji
# treba ocistiti. Treba ukloniti visestruko ponavljanje belinai i prebaciti sva
# slova u mala.

if [ "$#" -ne 1 ]; then
	echo "Koriscenje: $0 file"
	exit 1
fi

cat "$1" |
tr -s ' ' |
tr '[:upper:]' '[:lower:]'

