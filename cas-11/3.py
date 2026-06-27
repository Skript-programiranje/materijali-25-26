#!/usr/bin/python

import re

niska = input()

# Funkcijom re.match proveravamo da li niska pocinje brojem, to jest nizom cifara.
poklapanje = re.match(r"\d+", niska)
if poklapanje is not None:
    print(f"Pocinje brojem {poklapanje.group()}")
else:
    print("Ne pocinje brojem.")

