#!/usr/bin/python

# Zadatak: Ukloniti visestruko ponavljanje belina u fajlu koji se navodi kao prvi argument komandne linije.
# Koristiti fajl 'spaces.txt' kao primer.

import sys

if len(sys.argv) != 2:
    print(f"Koriscenje: {sys.argv[0]} <naziv_fajla>")
    sys.exit(1)

filepath = sys.argv[1]

try:
    with open(filepath, "r") as file_in:
        lines = file_in.readlines()
    with open(filepath, "w") as file_out:
        for line in lines:
            words = line.split()
            new_line = " ".join(words)

            # Funkcijom write upisujemo u fajl
            file_out.write(new_line + "\n")
except IOError:
    print("Greska prilikom otvaranja fajla.")
    sys.exit(1)
