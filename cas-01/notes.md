# Prva nedelja vežbi
Ove nedelje upoznali smo se sa osnovnim komandama za navigaciju Linux fajl sistemom, baratanje fajlovima i direktorijumima, kao i manipulaciju prava pristupa fajlovima. Takođe smo napravili uvod u Beš i pisanje Beš skripta.

## Navigacija fajl sistemom

Trenutni radni direktorijum može se videti komandom `pwd`.

```bash
$ pwd
/home/sp/
```

Trenutni radni direktorijum se može promeniti komandom `cd`.

```bash
$ ls
predavanja vezbe
$ cd vezbe
$ pwd
/home/sp/vezbe
```

Ukoliko imamo potrebu da se često prebacujemo između više direktorijuma, korisne su komande `pushd` i `popd`.

```bash
$ pwd
/home/sp/vezbe
$ dirs
/home/sp/vezbe
$ pushd /home/os
/home/os /home/sp/vezbe
$ pwd
/home/os
```

```bash
$ dirs
/home/os /home/sp/vezbe
$ pushd
/home/sp/vezbe /home/os
$ pwd
/home/sp/vezbe
```

```bash
$ dirs
/home/sp/vezbe /home/os
$ popd
/home/os
$ pwd
/home/os
```

---

## Komanda `ls`

Listanje direktorijuma može se uraditi komandom `ls`. Komanda `ls` prikazuje sadržaj tekućeg direktorijuma: fajlove, direktorijume i sve ostalo. Izuzetak su, recimo, skriveni fajlovi, čija imena počinju tačkom (na primer, tekući direktorijum `.` i roditeljski direktorijum `..`). Ukoliko želimo da vidimo skrivene fajlove, možemo navesti opciju `-a`:

```bash
$ ls -a
```

Takođe korisna opcija je `-l` za ispis u dugom formatu (eng. *long format*).

```bash
$ ls -l
```

Ukoliko ne želimo da prikažemo sadržaj tekućeg direktorijuma, već želimo da preciziramo direktorijum čiji sadržaj želimo da prikažemo, to možemo uraditi tako što naziv tog direktorijuma damo kao argument komandi `ls`. Na primer:

```bash
$ ls my_directory
```

Na Linux sistemima često postoji "komanda" `ll`, koja je zapravo *alijas* za komandu `ls` sa određenim opcijama (na primer, `-a`, `-l`, `-F`).

```bash
$ ll
```

Alijas je, kao što ime kaže, drugo ime za neku komandu (obično sa nekim specifičnim opcijama). Ako želimo da vidimo postavljene alijase, možemo to uraditi komandom `alias`:

```bash
$ alias
```

Specifično, možemo da vidimo šta predstavlja neki konkretan alijas putem `alias [naziv_alijasa]`, na primer:

```bash
$ alias ll
alias ll='ls -l'
```

Takođe, infomaciju o tipu komande ili alijasa možemo dobiti komandom `type`:

```bash
$ type ll
ll is aliased to `ls -l'
$ type cat
cat is /usr/bin/cat
```

---

## Pravljenje i brisanje fajlova i direktorijuma

Fajl se može napraviti komandom `touch`:

```bash
$ touch file.txt
$ ls
file.txt
```

Fajlove možemo obrisati komandom `rm`:

```bash
$ ls
file.txt another.txt
$ rm file.txt
$ ls
another.txt
```

Komandu `rm` treba koristiti *veoma* pažljivo, jer je brisanje koje ona vrši neopovratno!

Ukoliko želimo da napravimo direktorijum, to možemo uraditi komandom `mkdir`:

```bash
$ ls
01_prvi.txt 02_drugi.txt
$ mkdir zadaci
$ ls
01_prvi.txt 02_drugi.txt zadaci
```

Komandom `rmdir` možemo obrisati prazne direktorijume.

```bash
$ ls
01_prvi.txt 02_drugi.txt zadaci
$ rmdir zadaci
$ ls
01_prvi.txt 02_drugi.txt
```

Fajl možemo kopirati komandom `cp`.

```bash
$ ls
file.txt
$ cat file.txt
some
content
$ cp file.txt copy.txt
$ ls
$ cat file.txt
some
content
$ cat copy.txt
some
content
```

Komandom `mv` možemo pomeriti ili preimenovati fajl. Osnovni oblik korišćenja ove komande je `mv <source> <destination>`. Ukoliko `source` i `destination` imaju isti roditeljski direktorijum, onda se vrši preimenovanje `source` u `destination`. U suprotnom se `source` pomera u roditeljski direktorijum fajla `destination`.

```bash
$ ls -R
.:
alice.txt  bob.txt  others

./others:
caitlyn.txt

$ mv bob.txt others/david.txt

$ ls -R
.:
alice.txt  others

./others:
caitlyn.txt  david.txt
```

---

## Izmene dozvola nad fajlovima

```bash
$ ls -l
-rw-r-x-w- 1 sp sp   146 Mar 18 09:50 1.sh
```

Prva kolona se sastoji od 10 karaktera i nosi informacije o dozvolama.

| Tip | Vlasnik | Grupa | Ostali |
|-----|--------|-------|--------|
| `-` | `rw-`  | `r-x` | `-w-`  |

Karakter `r` označava čitanje, `w` pisanje, `x` izvršavanje, a `-` nedostatak dozvole.

### Tekstualni način

```bash
$ chmod u+x 1.sh
$ ls -l
-rwxr-x-w- 1 sp sp   146 Mar 18 09:50 1.sh
```

```bash
$ chmod g-x,o+r 1.sh
$ ls -l
-rwxr--rw- 1 sp sp   146 Mar 18 09:50 1.sh
```

### Numerički način

`rwxr--rw-` → `111100110` → `745`

```bash
$ chmod 745 1.sh
$ ls -l
-rwxr--rw- 1 sp sp   146 Mar 18 09:50 1.sh
```

---

## Promenljive okruženja

```bash
$ x=10
$ echo $x
10
```

```bash
$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/bin
```

```bash
$ printenv
PWD=/home/sp
SHELL=/bin/bash
USER=korisnik
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/bin
...
```

## Pokretanje skripti

Jedna od glavnih prednosti interakcije sa računarom pomoću komandne linije jeste
automatizacija pomoću šel (shell) skripti.
Komande se mogu napisati u tekstualnom fajlu, a taj fajl se zatim može dati šelu
da ga izvrši.

Na primer, ako napravimo fajl `zdravo.sh` sa sledećim sadržajem:
```bash
echo "Zdravo, svete!"
```

Možemo da je pokrenemo na sledeći način:
```bash
$ bash zdravo.sh
Zdravo, svete!
```

Drugi, češći, način je da skripte pokrećemo tako što:
1. skripti dodelimo pravo izvršavanja:
```bash
$ chmod +x zdravo.sh
```
2. pokrenemo skriptu kao izvršivi fajl:
```bash
$ ./zdravo.sh
Zdravo, svete!
```

Međutim, da bismo to radili, potrebno je da u skripti zadamo koji program treba
da je izvršava.
U ovom slučaju, to će biti `bash`, pa je potrebno da to dodamo.
To se radi tako što se na početku skripte postavi linija koja počinje `#!` (engl.
*shebang*) koju prati putanja do programa.

Na primer, ako komanda `which bash` vraća `/usr/bin/bash`, onda se skripta može
izmeniti na sledeći način:
```bash
#!/usr/bin/bash

echo "Zdravo, svete!"
```
