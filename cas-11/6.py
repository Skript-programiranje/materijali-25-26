#!/usr/bin/python

# Zadatak: Prepoznati sve reci koje pocinju velikim slovom u fajlu koji se unosi kao jedini argument komandne linije (za testiranje se moze uzeti fajl primer.txt).

# Ideja zadatka da se demonstriraju funkcije re.split i re.compile.

# Prvo su prepoznate sve reci iz fajla pomocu re.split.
# Zatim je za svaku rec pozivana funkcija re.search koja proverava da li rec pocinje velikim slovom.
# Kako re.search u pozadini pravi isti konacni automat u petlji za svaku rec, mozemo to pravljenje automata da uradimo na pocetku pomocu re.compile i onda samo nad dobijenim objektom mozemo da pozivamo sve vec vidjene funkcije.
# Nama na ovom kursu efikasnost nije preterano vazna, ali je korisno videti i ovu funkciju. :)

import sys
import re

if len(sys.argv) != 2:
    print(f"Koriscenje: {sys.argv[0]} fajl")
    sys.exit(1)

fajl = sys.argv[1]

try:
    with open(fajl, "r") as f:
        sadrzaj = f.read()
except IOError:
    print("Greska prilikom citanja.")
    sys.exit(1)

# Obradjujemo regularni izraz i "cuvamo ga" kao sablon.
automat = re.compile(r"^[A-Z][a-z]*")

for rec in re.split(r"\s+", sadrzaj):
    # Nad unapred pripremljenim sablonom proveravamo da li mu data niska odgovara.
    poklapanje = automat.search(rec)
    if poklapanje is not None:
        print(rec)

