#!/usr/bin/bash

# Zadatak: Za svaki fajl u tekucem direktorijumu izvojiti njegovu velicinu,
# datum i vreme poslednje modifikacije, kao i naziv. Izbrojati koliko reci ima
# izlaz

ls -l |
grep -E -o '[0-9]+\s[A-Z][a-z]{2}\s+[0-9]+\s+[0-9]{2}:[0-9]{2}.*' |
wc -w

