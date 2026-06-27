#!/usr/bin/python

# Zadatak: Pronaci sve validne datume u fajlu "datumi.txt" i ispisati ih u formatu GGGG-MM-DD.
# Validni datumi u fajlu su u formatu DD.MM.GGGG ili DD/MM/GGGG.

import sys
import re

try:
    with open("datumi.txt", "r") as f:
        sadrzaj = f.read()
except IOError:
    print("Greska prilikom citanja fajla.")
    sys.exit(1)

# Koristimo funkciju re.finditer i iteriramo po onome sto nam ona daje kao povratnu vrednost.
# Pri tome, koristimo imenovane grupe radi njihovog lakseg koriscenja.
for poklapanje in re.finditer(r"(?P<dan>\d{2})([./])(?P<mesec>\d{2})\2(?P<godina>\d{4})", sadrzaj):
    dan = poklapanje.group("dan")
    mesec = poklapanje.group("mesec")
    godina = poklapanje.group("godina")

    print(f"{godina}-{mesec}-{dan}")

# Mogli smo koristiti i funkciju re.findall:
# print(re.findall(r"(?P<dan>\d{2})([./])(?P<mesec>\d{2})\2(?P<godina>\d{4})", sadrzaj))
