# Prvi domaći zadatak

Ovde će biti opisan prvi domaći zadatak na kursu Skript programiranje.
Zadatak služi kao provera razumevanja gradiva obrađenog tokom prve dve nedelje vežbi.
Zadatak treba raditi isključivo samostalno, to jest, nije dozvoljeno raditi u paru, grupi i slično.
Takođe, nije dozvoljeno korišćenje pomoćnih (generativnih) sredstava.

Zadatak treba da se uradi u vidu jednog skripta (videti detalje u nastavku).
Svaki student svoj domaći predaje tako što šalje mejl svom (na Hipatiji dodeljenom) asistentu, na odgovarajuću adresu:
- Stefan Milenković - stefan.milenkovic@matf.bg.ac.rs;
- Robert Doža - robert.doza@matf.bg.ac.rs.

Pri predaji domaćeg, skript treba zapakovati u zip arhivu sa imenom *sp_domaci_1.zip* i tu
arhivu predati kao prilog u mejlu.
Neophodno je da naslov (*Subject*) mejla bude ***[SP] Domaci 1***.

Rok za izradu domaćeg je **26.04.2026 u 23.59**.

Oko nedoumica, slobodno nas kontaktirajte.

## Postavka - pomoćni skript

Neka je dat skript po imenu `test_type.sh` (može mu se pristupiti ovde: [`test_type.sh`](./test_type.sh)).
Ovaj skript biće korišćen za realizaciju zadatka.
Nije neophodno zalaziti u detalje kako funkcioniše, samo ga treba koristiti kao "crnu kutiju", a njegovo ponašanje je dato u nastavku.

Skript `test_type.sh` očekuje tačno jedan argument, ime test primera.
Skript određuje da li je test primer javni ili privatni, tako što ispisuje na
standardni izlaz "public" ili "private" u zavisnosti od prosleđenog argumenta.
Na primer,
```bash
$ ./test_type.sh test_example
public
$ ./test_type.sh my_test
private
```

## Zadatak

Napisati skript `initialize_repository.sh`.
Skript treba da ima sledeće ponašanje:
- Prvo se ispisuje tekući direktorijum (njegova apsolutna putanja).
  - Primer izvršavanja zadatka, zajedno sa primerom ispisa, može se videti nakon opisa zadatka.
- Zatim se pravi direktorijum `repository`.
Ukoliko ovaj direktorijum već postoji, skript ne prijavljuje nikakvu grešku niti ispisuje bilo kakvu poruku.
- Pozicionira se (menja se tekući direktorijum) u direktorijum `repository`.
- U tekućem direktorijumu, prave se tri poddirektorijuma: `src`, `include` i `test`.
Ponovo, ukoliko ovi direktorijumi već postoje, skript ne prijavljuje nikakvu gresku, niti ispisuje bilo kakvu poruku.
- U direktorijumu `src`, prave se (prazni) fajlovi `main.cpp` i `list.cpp`.
- U direktorijumu `include`, pravi se (prazan) fajl `list.hpp`.
- U direktorijumu `test` se (možda) prave test primeri.
To treba uraditi na sledeći način:
  - potrebno je utvrditi da li je ime test primera javno ili privatno;
    - ukoliko je javno, treba napraviti 15 test primera;
    - ukoliko je privatno, ne treba praviti test primere;
  - test primeri su fajlovi, čija imena treba da budu `<ime>_01.txt`, `<ime>_02.txt`, ..., `<ime>_15.txt`, gde je `<ime>` zadato kao prvi argument skripta;
    - može se pretpostaviti da je `<ime>` jedna niska bez belina;
  - kreiranje ovih fajlova je neophodno uraditi jednom komandom, i potrebno je imena svih fajlova opisati jednim izrazom (ne navoditi "ručno" imena svih 15 fajlova).
- Akcije u prethodnim stavkama bivaju praćene odgovarajućim porukama o njihovom uspehu (pogledati format ispisa u nastavku).
- Zatim, prikazuje se sadržaj direktorijuma `repository/test`

Ukoliko skriptu `initialize_repository.sh` nije prosleđeno tačno 2 argumenta, ispisuje se poruka o namenjenoj upotrebi i skript se završava sa statusom o grešci i ne izvršava se nijedna od prethodno navedenih stavki. Ukoliko skriptu jeste prosleđen adekvatan broj argumenata i sve stavke se izvrše bez problema, skript ispisuje poruku kojom opisuje da je završio posao i završava se vraćajući status o uspehu.

## Primeri izvršavanja

- Primer pogrešnog pokretanja:
```bash
$ ./initialize_repository.sh
```
```text
Usage: ./initialize_repository.sh <test_file_name>
```

- Primer ispravnog i uspešnog pokretanja:
```bash
$ ./initialize_repository.sh test_example
```
```text
Working directory: /home/student/
Created repository.
Moved into repository.
Created directories src, include & test.
Created source files main.cpp & list.cpp in src.
Created header list.hpp in include.
Created test files in test directory.
Repository contents:
********************
.:
include
src
test

./include:
list.hpp

./src:
list.cpp
main.cpp

./test:
test_example_01.txt
test_example_02.txt
test_example_03.txt
test_example_04.txt
test_example_05.txt
test_example_06.txt
test_example_07.txt
test_example_08.txt
test_example_09.txt
test_example_10.txt
test_example_11.txt
test_example_12.txt
test_example_13.txt
test_example_14.txt
test_example_15.txt
********************
Done!
```

- Primer #2 ispravnog i uspešnog pokretanja:
```bash
./initialize_repository.sh my_test
```
```text
Working directory: /home/student/
Created repository.
Moved into repository.
Created directories src, include & test.
Created source files main.cpp & list.cpp in src.
Created header list.hpp in include.
Repository contents:
********************
.:
include
src
test

./include:
list.hpp

./src:
list.cpp
main.cpp

./test:
********************
Done!
```

