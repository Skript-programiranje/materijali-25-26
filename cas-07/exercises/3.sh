#!/usr/bin/bash

# Zadatak: Iz fajla "people.csv" izdvojiti grad i ime osobe koja zivi u njemu.

tail -n +2 people.csv |
cut -d',' -f2,4 |
sed -E 's/(\w+),(.*)/\2 - \1/g'

