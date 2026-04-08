#!/bin/bash

# Osiguravamo da je broj argumenata komandne linije 1, 2 ili 3.
if [ $# -lt 1 ] || [ $# -gt 3 ]; then
	echo "The number of command-line arguments must be exactly 1, 2 or 3."
	exit 1
fi

# Petljom tipa "for each" pristupamo svakom od argumenata.
# Argumenti komandne linije su skladisteni u promenljivoj $@.
echo "Command-line arguments:"
for arg in $@; do
	echo "- $arg"
done

