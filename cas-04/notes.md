# Četvrta nedelja vežbi

Na ovom času bilo je reči o statusnom kodu komandi i Beš skriptova, kako se tom kodu može pristupiti i kako se on može iskoristiti.
Obrađeno je kombinovanje komandi korišćenjem logičkih veznika `&&` i `||`.
Rađeno je i preusmeravanje tokova u Bešu.

## Statusni kod

U Bešu, svaka komanda vraća *izlazni status* (ili *statusni kod*).
Ovaj status je nenegativan broj u rasponu od 0 do 255.
Pri tome, vrednost 0 predstavlja uspešno izvršenu komandu, dok strogo pozitivne vrednosti predstavljaju neuspešno izvršavanje.

Statusu prethodno izvršene komande možemo pristupiti preko `$?`.
Na primer, ukoliko izvršimo komandu `ls`:
```bash
$ ls
some_file.txt  another_file.txt
```
a zatim proverimo vrednost promenljive `$?`:
```bash
$ echo "$?"
0
```
videćemo da je status komande `ls` bio 0 (prikaz sadržaja direktorijuma je bio uspešan).

Slično, ako uradimo nešto poput:
```bash
$ cat missing_file.txt
cat: missing_file.txt: No such file or directory
$ echo "$?"
1
$ echo "$?"
0
```
primetićemo da je poziv komande `cat` bio neuspešan i ona je vratila status 1.
To smo videli pozivom `echo "$?"`, dok je drugi poziv `echo "$?"` vratio status prvog poziva komande `echo`.
Dakle, prikazuje se status prethodno izvršene komande, a ne komande `echo` kojom taj status prikazujemo.

U Beš skriptovima možemo vratiti statusni kod korišćenjem komande `exit`, uz argument koji predstavlja status koji želimo da vratimo.
Komanda `exit` završava skript i vraća status koji joj je prosleđen kao prvi argument.
Na primer, ukoliko želimo da završimo izvršavanje skripta i da pri tome vratimo status 0, to radimo na sledeći način:
```bash
exit 0
```
Ovo nam je posebno korisno kada proveravamo da li je pri izvršavanju skripta došlo do nekakve greške (na primer, argumenti komandne linije nisu prosleđeni u očekivanom obliku).
Naime, u tom slučaju možemo iskoristiti komandu `exit` da završimo program uz status o grešci.

## Kombinovanje komandi

Komande se mogu kombinovati logičkim operatorima `&&` i `||`.

Operator `&&` služi kao "logička konjunkcija" komandi.
Naime, ako imamo:
```bash
command1 && command2
```
Onda se komanda `command1` izvršava, a ako je bila uspešna ("tačna"), onda se pokušava izvršavanje komande `command2`.
Ukoliko komanda `command1` ne uspe (bude "netačna"), onda se ne pokušava izvršavanje komande `command2`, jer je operator lenje prirode ("netačno" i bilo šta drugo daje "netačno", pa to drugo nije potrebno evaluirati).

Ovo nam omogućava ulančavanje naredbi.
Na primer:
```bash
mkdir backup && touch backup/log.txt
```
Na ovaj način, komandom `mkdir` se pravi direktorijum `backup`.
Ukoliko komanda `mkdir` uspe, kreira se fajl `log.txt` u direktorijumu `backup`.
Ako `mkdir` ne uspe, druga komanda se ne izvršava.

Operatorom `&&` možemo ulančati i više naredbi:
```bash
mkdir -p backup && \
cp -r ./data ./backup && \
tar -czf backup.tar.gz ./backup && \
rm -rf ./backup
```
(ovde je korišćen `\` da bi kod čitljivije bio prikazan u više linija).

Operator `||` je sličan, samo što funkcioniše kao logička *disjunkcija*.
Naime, u komandi `command1 || command2` prva komanda (`command1`) se uvek izvršava, a komanda `command2` se izvršava jedino ako je prva neuspešno izvršena.
Na primer:
```bash
mkdir backup_folder || echo "Failed to create folder!"
```

Pored logičkih operatora `&&` i `||` imamo i *kontrolni separator* `;`. On je sličan, u smislu da možemo imati nešto poput:
```bash
command1 ; command2
```
pri čemu se obe komande (i `command1` i `command2`) izvršavaju, bez obzira na njihovu "tačnost" (to jest, statusne kodove koje vrate).

## Tokovi podataka i preusmeravanje

Procesi koriste tri toka podataka:
- standardni ulaz;
- standardni izlaz;
- standardni izlaz za greške.

Ovi tokovi (kao i maltene sve na Linux sistemima) su predstavljeni fajlovima i imaju svoje numeričke deskriptore:
- `0` za standardni ulaz;
- `1` za standardni izlaz;
- `2` za standardni izlaz za greške.

Standardni ulaz (koji ćemo često kraće označavati i sa `stdin`) je uobičajeno vezan za tastaturu.
Standardni izlaz i standardni izlaz za greške (koje ćemo kraćeiy označavati sa `stdout` i `stderr`, redom) su vezani za terminal.
Ovo se može promeniti *preusmeravanjem* tokova podataka.

### Preusmeravanje standardnog izlaza

Preusmeravanje standardnog izlaza se vrši operatorom `>`.

Na primer, ukoliko nam neka komanda u komandnoj liniji daje ispis koji je veliki i ne želimo da nam opterećuje terminal, taj ispis možemo preusmeriti u neki fajl.
```bash
$ ls -R /home/student
```
```
(veliki ispis)
```
Preusmeravanje standardnog izlaza:
```bash
$ ls -R /home/student > my_files.log
```
```
(ispisa nema, sve je upisano u `my_files.log`)
```

Ukoliko pokušamo:
```bash
$ ls -R /student > my_files.log
```
dobijamo:
```bash
ls: cannot access '/student': No such file or directory
```
i, uz to, fajl `my_files.log` je prazan.
Naime, desila se greška, pa je poruka o istoj ispisana na standardni izlaz *za greške*.
S druge strane, ispis na standardni izlaz je uspešno preusmeren u fajl `my_files.log` (samo što ispisa nije bilo, pa je fajl prazan).

### Preusmeravanje standardnog izlaza za greške

Preusmeravanje standardnog izlaza za greške se vrši operatorom `2>`.
Ukombinujmo to sa preusmeravanjem standardnog izlaza iz prethodnog primera:
```bash
$ ls -R /student > my_files.log 2> errors.log
```
Proverimo sadržaj fajla `errors.log`:
```bash
$ cat errors.log
```
```
ls: cannot access '/student': No such file or directory
```

### Dopisivanje, umesto prepisivanja

Operatori `>` i `2>` preusmeravaju standardne izlaze *prepisivanjem* preko postojećeg sadržaja u fajlu u koji se preusmerava.
Ukoliko želimo da *dopisujemo*, ne menjajući postojeći sadržaj, to postižemo operatorima `>>` i `2>>`.
Pokažimo to na primeru operatora `>>`:
```bash
$ echo "hi!" >> messages.txt
$ echo "here's a message" >> messages.txt
$ echo "and here's another one!" >> messages.txt
$ cat messages.txt
```
```
hi!
here's a message
and here's another one!
```
Analogno važi i za operator `2>>`.

### Operator `&>`

Operator `&>` skraćeno označava da preusmeravamo i standardni izlaz i standardni izlaz za greške na istu lokaciju.

```bash
$ ls exists.txt does_not_exist.txt &> ls_output.log
$ cat ls_output.log
```
```
ls: cannot access 'does_not_exist.txt': No such file or directory
exists.txt
```
Primetimo da su i standardni ispis i ispis o grešci upisani u fajl.

### Pajpovanje

U duhu ulančavanja naredbi o kojem je bilo reči ranije, veoma koristan operator je `|`, odnosno operator cevi ili pajp operator (eng. *pipe operator*).
Ideja je da, ukoliko želimo da izlaz jedne komande prosledimo drugoj, to možemo uraditi direktno, bez posrednog čuvanja međurezultata u fajlu.
Na primer, ukoliko želimo da vidimo koliko fajlova imamo u tekućem direktorijumu (a ne bismo da brojimo fizički izlaz koji nam komanda `ls` ispiše na terminal), možemo uraditi sledeće:
```bash
$ ls -1 | wc -l
```
```
14
```
Komanda `wc` (eng. *word count*) sa opcijom `-l` broji linije na ulazu.

Ovaj operator je izuzetno koristan i koristićemo ga (između ostalog) za manipulaciju tekstom (eng. (*text wrangling*) naredne nedelje.

### Pregled operatora za preusmeravanje

U narednoj tabeli, mogu se videti neki osnovni operatori preusmeravanja i njihov opis.

| operator | značenje |
| --- | --- |
| `<` | preusmeravanje standardnog ulaza |
| `>` | preusmeravanje standardnog izlaza |
| `>>` | preusmeravanje standardnog izlaza, (dopisivanjem umesto prepisivanjem)  |
| `2>` | preusmeravanje standardnog izlaza za greške |
| `2>>` | preusmeravanje standardnog izlaza za greške (dopisivanjem umesto prepisivanjem) |
| `&>` | preusmeravanje standardnog izlaza i standardnog izlaza za greške |
| `\|` | prosleđivanje sadržaja sa standardnog izlaza jedne komande na standardni ulaz druge komande |

