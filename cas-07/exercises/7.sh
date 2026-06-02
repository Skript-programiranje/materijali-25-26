#!/usr/bin/bash

# Zadatak: Kao jedini argument komandne linije se unosi niska koja predstavlja
# sifru. U zavisnosti od tipa sifre, napisati da li je slaba ili jaka. Jaka
# sifra ima barem jedno malo, barem jedno veliko slovo, barem jednu cifru i
# barem 8 karaktera.

if [ "$#" -ne 1 ]; then
	echo "Koriscenje: $0 sifra"
	exit 1
fi

sifra="$1"

izlaz=$(
	echo "$sifra" |
	grep -Eh '[a-z]'|
	grep -E '[A-Z]' |
	grep -E '[0-9]' |
	grep -E '.{8,}'
)

if ! [ -z "$izlaz" ]; then
	echo "Jaka sifra"
else
	echo "Slaba sifra"
fi

