#!/usr/bin/python

# Zadatak:
# Prvi argument komandne linije predstavlja fajl u formatu JSON koji sadrzi informacijame o studentima (kao primer, koristiti 'ocene.json').
# Drugi argument komandne linije predstavlja fajl koji treba napraviti.
# U taj izlazni fajl treba (takodje u formatu JSON) upisati indekse studenata, zajedno sa njihovim prosecnim ocenama.

import sys
import json

if len(sys.argv) != 3:
    print(f"Koriscenje: {sys.argv[0]} ulaz izlaz")
    sys.exit(1)

file_input = sys.argv[1]
file_output = sys.argv[2]

# Proveravamo da li su ulazni i izlazni fajl zadati za ekstenzijom '.json'.
if not file_input.endswith(".json") or not file_output.endswith(".json"):
    print(f"Nisu uneti json fajlovi.")
    sys.exit(1)

# Citamo podatke u formatu JSON.
try:
    with open(file_input, "r") as f:
        grades = json.load(f)
except IOError:
    print("Greska prilikom otvaranja fajla za citanje.")
    sys.exit(1)

# Obradjujemo procitane podatke.
average_grades = {}
for student in grades:
    student_index = student["indeks"]
    student_grades = student["ocene"]

    average_grades[student_index] = sum(student_grades) / len(student_grades)

# Obradjene podatke upisujemo u fajl, takodje u formatu JSON.
try:
    with open(file_output, "w") as f:
        json.dump(average_grades, f, indent=4)
except IOError:
    print("Greska prilikom otvaranja fajla za pisanje.")
    sys.exit(1)
