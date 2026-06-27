#!/usr/bin/python

# Zadatak: Prepoznati otvoreni html tag.
# Tagovi ne treba da budu osetljivi na velicinu slova i mogu da se protezu u vise redova.

import re

test = '''<TAG
        atribut="vrednost">'''

# Navodimo zastavice re.DOTALL i re.IGNORECASE.
# Njihovu kombinaciju izvodimo bitovskom disjunkcijom (operator '|').
poklapanje = re.search(r"<tag.*>", test, re.DOTALL | re.IGNORECASE)
if poklapanje is not None:
    print(poklapanje.group())
else:
    print("Nema poklapanja.")

