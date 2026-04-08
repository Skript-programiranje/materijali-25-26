# Ukoliko skript pozovemo sa:
# ./script.sh
# ili
# bash script.sh
# onda se kreira novi proces. Zato se iz terminala ne vidi promena direktorijuma.
# Ukoliko zelimo da se skript izvrsi u tekucoj sesiji u terminalu, mozemo uraditi sledece:
# source script.sh
# ili skraceno
# . script.sh

#!/bin/bash

echo "[Before] Current directory is: $(pwd)"

mkdir -p tmp

cd tmp

echo "[After] Current directory is: $(pwd)"

