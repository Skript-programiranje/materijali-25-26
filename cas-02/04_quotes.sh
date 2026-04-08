#!/bin/bash

name=Trebor

# Razlika u naredna dva ispisa je sto se u drugom ispisu nece prikazati vrednost promenljive "name".
# Razlog za to je sto jednostruki navodnici sprecavaju ekspanziju promenljive.
echo "Hello, $name!"
echo 'Hello, $name!'

