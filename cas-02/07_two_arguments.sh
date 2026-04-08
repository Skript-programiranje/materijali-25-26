#!/bin/bash

# Proveravamo da li je broj argumenata tacno 2.
# Ukoliko nije, korisniku prikazujemo namenjeni nacin upotrebe skripta i zavrsavamo izvrsavanje, uz status 1 da bismo signalizirali da je doslo do greske.
# Broju argumenata komandne linije ($1, $2, $3, ..., bez $0) mozemo pristupiti preko promenljive $#.
if [ $# -ne 2 ]; then
	echo "Usage: $0 arg1 arg2"
	exit 1
fi

echo "First argument: $1"
echo "Second argument: $2"

