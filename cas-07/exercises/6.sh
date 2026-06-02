#!/usr/bin/bash

# Zadatak: Za svaku liniju fajla "todo.txt" formirati nazive fajlova spajanjem
# reci u njoj donjim crtama i nadovezivanjem ekstenzije txt.

# 1. nacin
tr -s ' ' '_' <todo.txt |
while read linija; do
	echo "$linija.txt"
done

# 2. nacin
while read linija; do
	echo "$linija.txt" | tr -s ' ' '_'
done <todo.txt

