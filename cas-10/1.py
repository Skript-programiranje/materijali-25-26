#!/usr/bin/python

# Zadatak: Ispisati sadrzaj fajla 'example_file.txt'.

# Ukljucujemo modul sys
import sys

# U 'try' bloku pokusavamo da citamo iz fajla
try:
    # Otvaramo fajl 'fajl.txt' u modu za citanje
    with open("example_file.txt", "r") as f:
        # Izdvajamo sadrzaj celog fajla
        sadrzaj = f.read()
        print(sadrzaj)
# Ukoliko smo uhvatili neku gresku...
except IOError:
    # ...ispisujemo odgovarajucu poruku
    print("Fajl ne postoji")
    # ...i prekidamo izvrsavanje skripta
    sys.exit(1)

