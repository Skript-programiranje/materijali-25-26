#!/usr/bin/bash

# Zadatak: Kao jedini argument komande linije se zadaje putanja do html fajla
# koji predstavlja rezultate sa ispita. Naziv fajla mora da pocinje recju
# "exam" (primeri: "exam_01.html" i "exam_02.html").
# Ispisati na standardni izlaz rezultate ispita sortirane po broju poena
# opadajuce tako da svaka linija bude u formatu: IME PREZIME ALAS BR_POENA.

if [ "$#" -ne 1 ]; then
	echo "Koriscenje: $0 putanja"
	exit 1
fi

if ! [[ "$1" =~ ^exam.*\.html$ ]]; then
	echo "Pogresno ime fajla"
	exit 1
fi

# 1. nacin
grep -Eo '<td>\s*\w+\s+\w+\s*</td>\s*<td>\s*[0-9]+\s*/\s*20[0-9]{2}\s*</td>\s*<td>\s*[0-9]+\s*</td>' "$1" |
sed -E 's/<td>/ /g' |
sed -E 's/<\/td>/ /g' |
sed -E 's/\s+/ /g' |
sed -E 's/^\s+//g' |
sed -E 's/([0-9]{3})\s*\/\s*20([0-9]{2})/mi\2\1/g' |
sed -E 's/([0-9]{2})\s*\/\s*20([0-9]{2})/mi\20\1/g' |
sed -E 's/([0-9])\s*\/\s*20([0-9]{2})/mi\200\1/g' |
sort -nr -k 4

# 2. nacin
grep -Eho '<td>.*' "$1" |
sed -E 's/<td>/ /g' |
sed -E 's/<\/td>/ /g' |
tr -s ' ' |
sed -E 's/^\s//g' |
sed -E 's/\// /g' |
sed -E 's/20([0-9]{2})/\1/g' |
while read ime prezime br godina poeni; do
	if [[ "$br" =~ ^[0-9]$ ]]; then
		br="00$br"
	elif [[ "$br" =~ ^[0-9]{2}$ ]]; then
		br="0$br"
	fi

	# Moze i koriscenjem shel aritmetike.
	# if (( $br < 10 )); then
	# 	br="00$br"
	# elif (( $br < 100 )); then
	# 	br="0$br"
	# fi

	echo "$ime $prezime mi$godina$br $poeni"
done |
sort -k 4 -n -r
