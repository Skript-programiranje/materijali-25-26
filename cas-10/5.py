#!/usr/bin/python

# Ispisati sve regularne fajlove koji se nalaze u direktorijumu koji se navodi kao prvi argument komandne linije.

import sys
# Ukljucujemo modul 'os' koji ce nam biti potreban za funkcije za rad sa fajlovima i direktorijumima.
import os

if len(sys.argv) != 2:
    print(f"Koriscenje: {sys.argv[0]} <ime_direktorijuma>")
    sys.exit(1)

directory = sys.argv[1]

# Proveravamo da li je prosledjeni argument komandne linije zapravo direktorijum.
if not os.path.isdir(directory):
    print("Nije zadata putanja do direktorijuma.")
    sys.exit(1)

# Listamo direktorijum.
for file in os.listdir(directory):
    path = os.path.join(directory, file)
    # Ispisujemo ime fajla samo ukoliko je zaista regularan fajl.
    if os.path.isfile(path):
        print(path)
