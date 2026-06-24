#!/usr/bin/python

# Kao prvi argument komandne linije se unosi putanja do CSV fajla sa rezultatima ispita (kao primer koristiti fajl 'rezultati.csv').
# Ispisati ime i prezime studenta, praceno brojem poena koji su osvojili, sortirane po broju poena, rastuce.

import sys

if len(sys.argv) != 2:
    print(f"Koriscenje: {sys.argv[0]} <naziv_fajla>")
    sys.exit(1)

file_name = sys.argv[1]
if not file_name.endswith(".csv"):
    print("Nije zadat CSV fajl.")
    sys.exit(1)

try:
    with open(file_name, "r") as file_input:
        students = []
        for line in file_input.readlines():
            info = line.split(",")
            name, surname, points = [e.strip() for e in info]
            students.append( (f"{name} {surname}", int(points)) )
except IOError:
    print("Greska prilikom citanja fajla.")
    sys.exit(1)

students.sort(key=lambda p: p[1], reverse=True)
for name, points in students:
    print(f"{name}: {points}")

