#!/usr/bin/python

# Ukljucujemo modul 're'.
import re

niska = input()

# Koristimo funkciju re.search da proverimo da li data niska sadrzi 'broj' (niz cifara).
poklapanje = re.search(r"\d+", niska)
if poklapanje is not None:
    print("Poklapanje!")
    print(poklapanje.group())
else:
    print("Nema poklapanja.")

