# Drugi domaći zadatak

Ovde će biti opisan drugi domaći zadatak na kursu Skript programiranje.
Zadatak služi kao provera razumevanja gradiva obrađenog tokom treće, četvrte, pete, šeste i sedme nedelje vežbi (ali se, naravno, mogu koristiti i koncepti obrađeni tokom prve dve nedelje semestra).
Zadatak treba raditi isključivo samostalno, to jest, nije dozvoljeno raditi u paru, grupi i slično.
Takođe, nije dozvoljeno korišćenje pomoćnih (generativnih) sredstava.

Zadatak treba da se uradi u vidu jednog skripta (videti detalje u nastavku).
Svaki student svoj domaći predaje tako što šalje mejl svom (na Hipatiji dodeljenom) asistentu, na odgovarajuću adresu:
- Stefan Milenković - stefan.milenkovic@matf.bg.ac.rs;
- Robert Doža - robert.doza@matf.bg.ac.rs.

Pri predaji domaćeg, skript treba zapakovati u zip arhivu sa imenom *sp_domaci_2.zip* i tu
arhivu predati kao prilog u mejlu.
Neophodno je da naslov (*Subject*) mejla bude ***[SP] Domaci 2***.

Rok za izradu domaćeg je **23.06.2026 u 23.59**.

Oko nedoumica, slobodno nas kontaktirajte.

## Zadatak

Napisati skriptu `tester.sh`.
Ova skripta služi da automatski ocenjuje ispitne zadatke.

Skripta treba da ima sledeće ponašanje:

Kao argument komandne linije se zadaje obavezni argument `--dir` ili `-d` koga
prati putanja do direktorijuma sa ispitnim zadacima.
Obići sve poddirektorijume zadatog direktorijuma sa nazivom u formatu `miXXYYY`
gde je `XX` broj između 10 i 25, a `YYY` broj između 1 i 500 dopunjen nulama do
3 cifre.
Jedan takav direktorijum predstavlja rešenje ispita jednog studenta.
Za svaki fajl sa ekstenzijom `.c` u svakom od tih direktorijuma treba uraditi
sledeće:
1. Prevesti fajl komandom `gcc -Wall -Wextra`
2. Pokrenuti prevedeni program i izmeriti vreme izvršavanja
3. Ukoliko je vreme kraće od 0.2 sekunde, dodeliti 10 poena.
Ukoliko je između 0.2 i 1 sekunde, dodeliti 5 poena.
Ukoliko je između 1 i 2 sekunde, dodeliti 1 poen, a inače dodeliti 0 poena.

Za svakog studenta ispisati njegov indeks i ukupan broj poena koje je ostvario
na ispitu.
Indeks treba da bude u formatu `X/YYYY` gde je `X` broj indeksa (koji nije
dopunjen vodećim nulama), a `YYYY` odgovarajuća godina upisa.
Izdvojiti one studente koji su, po broju poena, bili među prvih 5 i ispisati ih
po broju poena opadajuće.

Prilikom obrade svakog studenta potrebno je na **standardni izlaz za greške**
ispisati `Processing miXXYYY...`, gde je `miXXYYY` alas nalog studenta koji se
obrađuje.

### *Pomoć*

1) Broj milisekundi proteklih od *Unix* epohe se može dobiti komandom:
```bash
$ date +%s%3N
```
```
1778533214029
```
Vreme trajanja komande u milisekundama dobija se kao razlika između broja
milisekundi proteklih od Unix epohe nakon i pre njenog izvršavanja.

2) Naziv fajla (bez roditeljskih direktorijuma) se može dobiti komandom
`basename`.
Primer:
```bash
$ basename putanja/do/fajla/fajl.txt
```
```
fajl.txt
```

### *Napomene*

1) Pretpostaviti da neće biti grešaka prilikom prevođenja C programa.
2) Pretpostaviti da se prevedeni C programi neće izvršavati duže od 3 sekunde
i time blokirati izvršavanje skripte.
3) Izvršivi programi nastali kompilacijom ne treba da ostanu u fajl sistemu
nakon završetka rada skripte.

## Primer izvršavanja

Direktorijum *primeri* sadrži primere direktorijuma sa ispitnim zadacima.

```bash
$ ./tester.sh --dir primeri/ispitni_rok
```
```
Processing mi10021...
Processing mi10022...
Processing mi10023...
Processing mi10026...
Processing mi10027...
Processing mi10028...
Processing mi10029...
Processing mi10030...
Processing mi10031...
Processing mi10032...
Processing mi10033...
Processing mi11034...
Processing mi12035...
Processing mi13136...
Processing mi14037...
Processing mi15038...
Processing mi23006...
Processing mi24123...
34/2011 40
21/2010 30
35/2012 25
22/2010 25
136/2013 21
```

