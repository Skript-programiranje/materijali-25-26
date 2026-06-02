#!/usr/bin/bash

# Zadatak: Izbrojati koliko se razlicitih reci pojavljuje u svim txt fajlovim
# u tekucem direktorijuu koji pocinju sa "primer".

grep -E -h -o '\w+' primer*.txt |
sort |
uniq |
wc -l

