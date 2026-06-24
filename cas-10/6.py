#!/usr/bin/python

# Ispisati sve regularne fajlove pracene brojem linija u njima za sve fajlove koji se nalaze u direktorijumu koji se navodi kao prvi argument komandne linije.
# Treba obici sve podfajlove zadatog direktorijuma, ne samo neposrednu decu.

import os
import sys

if len(sys.argv) != 2:
    print(f"Koriscenje: {sys.argv[0]} direktorijum")
    sys.exit(1)

directory = sys.argv[1]

if not os.path.isdir(directory):
    print("Nije zadata putanja do direktorijuma.")
    sys.exit(1)

# Kako je potrebno rekurzivno obici fajlove i poddirektorijume, koristimo funkciju os.walk.
for dirpath, dirnames, filenames in os.walk(directory):
    for filename in filenames:
        try:
            path = os.path.join(dirpath, filename)
            with open(path, "r") as f:
                print(f"{path}: {len(f.readlines())}")
        except IOError:
            print(f"Greska prilikom otvaranja fajla {fajl}")
            sys.exit(1)

