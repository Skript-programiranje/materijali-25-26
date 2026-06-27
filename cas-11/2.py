#!/usr/bin/python

import re

niska = input()

# Funkcijom re.fullmatch proveravamo da li data niska u celosti predstavlja broj, to jest niz cifara.
poklapanje = re.fullmatch(r"\d+", niska)
if poklapanje is not None:
    print("Jeste broj!")
else:
    print("Nije broj.")

