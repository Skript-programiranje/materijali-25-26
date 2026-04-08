# Shebang
#!/bin/bash

# Promenljive mogu sadrzati vrednosti za kasniju upotrebu.
# Napomena: sintaksa "name = Robert" nije ispravna, jer se tumaci kao poziv komande "name" sa argumentima = i Robert
name=Robert

# Komandom "echo" ispisujemo poruku na standardni izlaz. Vrsi se ekspanzija promenljive name, pa se prikazuje vrednost koju ona sadrzi.
echo "Hello, $name!"

