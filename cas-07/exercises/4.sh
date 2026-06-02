#!/usr/bin/bash

# Zadatak: Urediti fajl "list.txt" tako da redovi budu odgovarajuce numerisani.

tr '1-6' '4-61-3' <list.txt |
sort -n

