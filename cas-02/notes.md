# Druga nedelja vežbi
Ove nedelje, pisani su Beš skriptovi. Obrađeni su parametri i promenljive, osnovna kontrola toka i različite vrste ekspanzija u Bešu.

## Parametri i promenljive
U Bešu mozemo deklarisati promenljive na sledeći način:
```bash
promenljiva=vrednost
```
Treba imati u vidu da ovo nije ekvivalentno sa:
```bash
promenljiva = vrednost
```
jer se ovo tumači kao poziv komande `promenljiva` sa argumentima `=` i `vrednost`.

Ukoliko želimo da pristupimo vrednosti promenljive, to radimo navodjenjem specijalnog karaktera `$`. Na primer, `$promenljiva`. Ovaj koncept nazivamo *ekspanzijom promeljivih*.

Promenljive su *parametri*. Nisu svi parametri promenljive. Na primer, imamo *pozicione parametre* koji odgovaraju argumentima komandne linije: `$0, $1, $2, $3, ...`. Parametar `$0` odgovara imenu skripta, dok su `$1, $2, $3, ...` argumenti. Broj argumenata (počevši od `$1`, `$0` se ne računa) se može pristupiti parametrom `$#`. Svim argumentima zajedno se može pristupiti paramterom `$@`. Parametar `$$` sadrži identifikator trekućeg procesa.

*Napomena*: Za dobijanje argumenata komandne linije čiji redni broj sadrži više
od jedne cifre, potrebno je koristiti vitičaste zagrade.
Na primer, `${11}` predstavlja 11. argument komandne linije, dok `$11`
predstavlja prvi argument komandne linije na koji je nadovezana jedinica.

## Navodnici

Jednostruki navodnici čuvaju doslovne vrednosti karaktera u njima.
Dakle, karakteri u jednostrukim navodnicima se ne tretiraju kao specijalni.

Dvostruki navodnici takođe čuvaju doslovne vrednosti karaktera, ali ne svih.
Konkretno, samo karakteri  `$`, `` ` ``, `\` i `!` imaju posebno značenje u
dvostrukim navodnicima.

Primeri:
- Beline nemaju specijalno značenje ni u jednostrukim, ni u dvostrukim navodnicima.
Obe komande `mkdir "My Documents"` i `mkdir 'My Documents'` prave nov direktorijum 
sa nazivom `My Documents`.
- U dvostrukim navodnicima, znak `$` služi za dobijanje vrednosti promenljiva.
```bash
$ x=5
$ echo "Vrednost promenljive je $x."
Vrednost promenljive je 5.
$ echo 'Vrednost promenljive je $x.'
Vrednost promenljive je $x.
```
*Napomena*: Vrednost promenljive `promenljiva` se može dobiti i kao
`$promenljiva` i kao `"$promenljiva"`.
U većini slučajeva, drugi način je sigurniji.
Na primer:
```bash
$ ime="My Documents"
$ mkdir $ime          # pravi dva direktorijuma 'My' i 'Documents'
$ mkdir "$ime"        # pravi jedan direktorijum 'My Documents'
```

## Ekspanzije

U Bešu postoji više različitih ekspanzija:
- ekspanzija vitičastih zagrada
- tilda ekspanzija
- ekspanzija promenljivih i parametara
- supstitucija komandi
- aritmetička ekspanzija
- razdvajanje reci
- ekspanzija naziva fajlova
- uklanjanje navodnika

### Vitičaste zagrade

Vitičaste zagrade se proširuju tako što se uzimaju sve moguće opcije za vrednosti navedene unutar njih. Na primer, `directory_{1,2,3}` se proširuje do `directory_1 directory_2 directory_3`, dok se `test_file_{08..12}.txt` proširuje do:
```bash
test_file_08.txt test_file_09.txt test_file_10.txt test_file_11.txt test_file_12.txt
```
Takođe, više parova vitičastih zagrade se dekartovski kombinuje. Na primer, `{analysis, algebra}_{1,2,3}` postaje:
```bash
analysis_1, analysis_2, analysis_3, algebra_1, algebra_2, algebra_3
```

### Tilda (~) ekspanzija

Karakter `~` se proširuje do apsolutne putanje korisnikovog direktorijuma `home`.

### Supstitucija komandi

Komande se supstituišu pomoću `$(...)`. Na primer, ukoliko navedemo nisku `"current directory is $(pwd)"`, rezultat izvršavanja komande `pwd` će biti deo rezultujuće niske.

### Aritmetička ekspanzija

Sintaksom `$(( ... ))` možemo izvršavati aritmetičke operacije nad celobrojnim vrednostima. Rezultat je niska. Na primer, `$(( 3 + 19 ))` se evaluira i dobijamo (nisku) `"22"`. U izrazima je dozvoljeno navoditi promenljive, pri čemu nije obavezno navoditi ih sa `$`. Na primer `$(( x % 4 ))` će se evaluirati i dati ostatak pri celobrojnom deljenju vrednosti upisane u `x` sa 4. Ukoliko se vrednost promenljive ne može protumačiti kao ceo broj, na tom mestu se umesto toga koristi vrednost 0.

### Ostalo

Više se može pronaći na [zvaničnom prirucniku za Beš](https://www.gnu.org/software/bash/manual/html_node/Shell-Expansions.html).

## Kontrola toka - grananje

Beš podržava grananje. Sintaksa je:
```bash
if uslov
then
  uradi nešto
fi
```
Kako se karakter `;` koristi za naglašavanje kraja komande, `then` možemo staviti i u prvu liniju:
```bash
if uslov; then
  uradi nešto
fi
```
Možemo imati i `else` granu:
```bash
if uslov
then
  uradi nešto
else
  uradi nešto drugo
fi
```
Ukoliko imamo dodatne uslove, koristimo `elif`:
```bash
if neki uslov
then
  uradi nešto
elif neki drugi uslov then
  uradi nešto drugo
elif neki treći uslov then
  uradi nešto treće
...
fi
```

### Primer grananja - provera korektnosti argumenata

Grananje možemo da iskoristimo da bismo proverili korektnost poziva Beš skripta. Recimo, ukoliko je potrebno osigurati da se skript `script.sh` poziva sa tačno dva argumenta, to možemo uraditi na sledeći način:
```
if test $# -ne 2
then
  echo "Usage: $0 arg1 arg2"
  exit 1
fi
```

## Kontrola toka - "for each" petlja

Beš podržava iteriranje for petljom sa `for ... in ...` sintaksom:
```bash
for variable in items
do
    # do something
done
```
pri čemu su `items` niske razdvojene belinama, a u svakoj iteraciji se u promenljivu `variable` smešta sledeća niska iz `items`. Niske `items` mogu biti navedene bukvalno, na primer:
```bash
for fruit in apples oranges strawberries
do
    echo "I like $fruit"
done
```
Takođe, `items` može biti dobijeno ekspanzijom:
```bash
for number in {1..5}
do
    echo "Iteration: $number"
done
```

### Primer "for each" petlje - iteriranje kroz argumente

Ukoliko recimo, želimo da iteriramo kroz argumente, to možemo uraditi na sledeći način:
```bash
echo "Arguments:"
for arg in $@
do
  echo "- $arg"
done
```

Komandom `test` proveravamo da li je ispunjen uslov. `-ne` je poređenje na različitost vrednosti (`-ne` - not equal). Pored tog, imamo i naredne načine poređenja brojevnih vrednosti:

| opcija | skraćeno od | značenje |
|--|--|--|
| `-eq` | equal             | vrednosti jednake                         |
| `-ne` | not equal         | vrednosti različite                       |
| `-gt` | greater than      | prva vrednost veća od druge               |
| `-lt` | less than         | prva vrednost manja od druge              |
| `-ge` | greater or equal  | prva vrednost veća od ili jednaka drugoj  |
| `-le` | less or equal     | prva vrednost manja od ili jednaka drugoj |

Za poređenje niski, imamo sledeće opcije:
| opcija | značenje |
|--|--|
| `=`  | niske jednake     |
| `!=` | niske različite   |
| `-z` | niska prazna      |
| `-n` | niska nije prazna |

Umesto komande `test` mogli smo da koristimo i uglaste zagrade:
```bash
if [ $# -ne 2 ]
then
  echo "Usage: $0 arg1 arg2"
  exit 1
fi
```

*Napomena*: Kako je `[` komanda, beline u prethodnom zapisu su neophodne.
Na primer, sledeći kod izbacuje grešku:
```bash
if [$# -ne 2]
then
  echo "Usage: $0 arg1 arg2"
  exit 1
fi
```
