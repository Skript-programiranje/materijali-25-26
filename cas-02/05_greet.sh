#!/bin/bash

# Promenljivom $0 pristupamo imenu komande, to jest skripta.
# Promenljivama $1, $2, $3, ... pristupamo argumentima komandne linije.
# Promenljiva $$ sadrzi identifikator tekuceg procesa.
echo "Hello, $1! My name is $0. My process ID is: $$"

