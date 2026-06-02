#!/usr/bin/bash

# Zadatak: Kao prvi i jedini argument komandne linije se unosi pozitivan ceo
# broj N. Izdvojiti N najfrekventinih validnih datuma sa njihovim brojem
# pojavljivanja iz svih txt fajlova u tekucem direktorijumu. Datum je validan
# ukoliko je u formatu DD-MM-GGGG ili DD.MM.GGGG.

if [ "$#" -ne 1 ]; then
    echo "Koriscenje: $0 BROJ"
    exit 1
fi

grep -Eho '(0[1-9]|[12][0-9]|3[01])([-.])(0[1-9]|1[0-2])\2[0-9]{4}' *.txt |
sed -E 's/-/./g' |
sort |
uniq -c |
sed -E 's/^\s+//g' |
sort -nr |
head -n "$1"

