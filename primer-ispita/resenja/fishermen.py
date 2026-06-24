#!/usr/bin/python

import sys
import os
import re
import json

if len(sys.argv) != 2:
    print(f"Koriscenje: {sys.argv[0]} <dir>")
    sys.exit(1)

direktorijum = sys.argv[1]

if not os.path.isdir(direktorijum):
    print("Nije zadat validan direktorijum.")
    sys.exit(1)

market_fajl = os.path.join(direktorijum,  "market.csv")
market_data = {}
try:
    with open(market_fajl, "r") as f:
        for linija in f.readlines():
            riba, cena = [v.strip() for v in linija.split(",")]
            market_data[riba] = int(cena)
except IOError:
    print("Greska prilikom otvaranja fajla market.csv.")
    sys.exit(1)

pecarosi_json = re.compile(r"(?P<ime>[a-zA-Z]+)_\d+.json")
pecarosi_data = {}
for fajl in os.listdir(direktorijum):
    poklapanje = pecarosi_json.fullmatch(fajl)
    if poklapanje is None:
        continue

    ime = poklapanje.group("ime")
    putanja = os.path.join(direktorijum, fajl)
    try:
        with open(putanja, "r") as f:
            for d in json.load(f):
                riba = d["fishType"]
                kolicina = d["number"]

                if ime in pecarosi_data:
                    pecarosi_data[ime] += kolicina * market_data[riba]
                else:
                    pecarosi_data[ime] = kolicina * market_data[riba]
    except IOError:
        print(f"Greska prilikom otvaranja fajla {putanja}.")
        sys.exit(1)

zarade = [(ime, zarada) for ime, zarada in pecarosi_data.items()]
zarade.sort(key=lambda t: t[1], reverse=True)

for ime, zarada in zarade:
    print(f"{ime.capitalize():>15} {zarada:>7}")
