#!/usr/bin/bash

# Zadatak: Izdvojiti imena korisnika i podrazumevane selove koje koriste iz
# fajla "/etc/passwd"

cut -d':' -f1,7 /etc/passwd | sed -E 's/:/ /g'

