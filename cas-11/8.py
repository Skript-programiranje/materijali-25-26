#!/usr/bin/python

# Zadatak:
# Kao argument komandne linije se unose putanje:
# 1) do html fajla koji sadrzi tabelu sa rezultatima ispita (primer rezultati.html) i 
# 2) izlaznog fajla koji treba napraviti, u formatu JSON.
# Izlazni fajl treba da sadrzi podatke o studentima u sledecem formatu:
# "alas": {
#     "ime": "Ime i prezime",
#     "poeni": POENI
# }
# gde "alas" predstavlja alas nalog odgovarajuceg studenta u formatu miXXYYY.

import sys
import re
import json

if len(sys.argv) != 3:
    print(f"Koriscenje: {sys.argv[0]} ulaz izlaz")
    sys.exit(1)

ulaz = sys.argv[1]
izlaz = sys.argv[2]

if re.search(r".*\.html$", ulaz, re.IGNORECASE) is None:
    print("Ulaz nije html.")
    sys.exit(1)

if re.search(r".*\.json$", izlaz, re.IGNORECASE) is None:
    print("Izlaz nije json.")
    sys.exit(1)

try:
    with open(ulaz, "r") as f:
        sadrzaj = f.read()
except IOError:
    print("Greska prilikom citanja fajla.")
    sys.exit(1)

regex = r"<td>\s*(?P<ime>\w+)\s+(?P<prezime>\w+)\s*</td>\s*"
regex += r"<td>\s*(?P<broj>\d+)\s*/\s*(?P<godina>\d+)\s*</td>\s*"
regex += r"<td>\s*(?P<poeni>\d+)\s*</td>"

studenti = {}
for poklapanje in re.finditer(regex, sadrzaj):
    ime = poklapanje.group("ime")
    prezime = poklapanje.group("prezime")
    broj = int(poklapanje.group("broj"))
    godina = int(poklapanje.group("godina"))
    poeni = int(poklapanje.group("poeni"))

    # Naredne provere su se mogle izvesti i koriscenjem regularnih izraza (probati to, za vezbu).
    if broj < 10:
        alas = f"mi{godina % 100}00{broj}"
    elif broj < 100:
        alas = f"mi{godina % 100}0{broj}"
    else:
        alas = f"mi{godina % 100}{broj}"

    studenti[alas] = {
        "ime": ime + " " + prezime,
        "poeni": poeni
    }

try:
    with open(izlaz, "w") as f:
        json.dump(studenti, f, indent=4)
except IOError:
    print("Greska prilikom pisanja.")
    sys.exit(1)

