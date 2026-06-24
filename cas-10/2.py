#!/usr/bin/python

# Zadatak: Ispisati broj linija fajla koji se unosi kao prvi argument komandne linije.

import sys

if len(sys.argv) != 2:
    print(f"Koriscenje: {sys.argv[0]} <naziv fajla>")
    sys.exit(1)

filepath = sys.argv[1]

try:
    with open(filepath, "r") as file:
        print(len(file.readlines()))
except IOError:
    print("Greska prilikom otvaranja fajla")
    sys.exit(1)

