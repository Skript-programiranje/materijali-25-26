# Sedma nedelja vežbi

Ove nedelje obrađene su komande `cut` i `tr`. Vežbani su zadaci sa ovim komandama, kao i zadaci sa text wrangling-om.

## Regularni izrazi u Bešu

Beš podržava proveru poklapanja sa regularnim izrazom pomoću operatora `=~`,
koji se koristi unutar konstrukcije `[[ ... ]]`. Desna strana operatora je
prošireni regularni izraz, dok je leva strana string koji se proverava.

Konstrukcija `[[ ... ]]` predstavlja jednu vrstu uopštenja opratora `[` i je
specifična za Beš, tj. nije POSIX saglasna. Ako je potrebno da skripta radi u
različitim POSIX šelovima, bolje je koristiti operator `[`.

Primer: Sledeća skripta proverava da li prvi argument komandne linije sadrži
broj ili ne.

*regex.sh*:
```bash
#!/usr/bin/bash

if [[ "$1" =~ [0-9]+ ]]; then
    echo "Sadrzi broj."
else
    echo "Ne sadrzi broj."
fi
```
```bash
$ ./regex.sh 123
Sadrzi broj.

$ ./regex.sh abs
Ne sadrzi broj.
```

Medjutim, i za sledeći poziv se ispisuje da ulaz sadrži broj.
```bash
$ ./regex.sh ab12cd
Sadrzi broj.
```
Naime, operator `=~` proverava da li u izrazu sa leve strane postoji poklapanje
regularnog izraza sa desne strane. Poklapanje može biti bilo gde, tako da
prethodna skripta ispituje da li prvi argument komandne linije sadrži broj
negde u sebi.

Ako želimo da proverimo da li je prvi argument komandne linije broj ili ne,
potrebno je da ograničimo poklapanje sidrima `^` i `$`.

*regex.sh*:
```bash
#!/usr/bin/bash

if [[ "$1" =~ ^[0-9]+$ ]]; then
    echo "Jeste broj."
else
    echo "Nije broj."
fi
```
```bash
$ ./regex.sh 123
Jeste broj.

$ ./regex.sh abs
Nije broj.

$ ./regex.sh ab12cd
Nije broj.
```

Desna strana operatora `=~` se obično ne stavlja pod navodnike, zato što
navodnici mogu da promene značenje specijalnih karaktera u regularnom izrazu.

## Komanda `cut`

Komanda `cut` služi za „seckanje“ (eng. cutting), to jest izdvajanje, delova teksta. Seckanje se može raditi po karakterima, bajtovima, ili poljima.
U nastavku ćemo bliže opisati o čemu je reč.
Uzmimo kao primer fajl `/etc/passwd`. Ovaj fajl sadrži informacije o korisnicima sistema, i to:
- naziv korisnika;
- korisnikovu šifra (često kritovanu i prikazanu kao `x`);
- identifikator korisnika;
- identifikator primarne grupe korisnika;
- deskriptivne informacije o korisniku (puno ime, telefon i drugo);
- `home` direktorijum korisnika;
- `login shell` - putanja do podrazumevanog interpretatora komandne linije korisnika (na primer, `/bin/bash`.

Ovih sedam podataka (kolona) su razdvojeni dvotačkom (`:`).
Primer stavki iz ovog fajla (na nekom konkretnom sistemu):
```bash
$ cat /etc/passwd
```
```
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
...
```
Recimo da nas zanimaju ime korisnika (prva kolona) i njegov podrazumevani šel (sedma kolona).
Ove informacije možemo lako dohvatiti komandom `cut`:
```bash
$ cut -f 1,7 -d : /etc/passwd
```
```
root:/bin/bash
daemon:/usr/sbin/nologin
bin:/usr/sbin/nologin
sys:/usr/sbin/nologin
sync:/bin/sync
...
```
Prvom opcijom, opcijom `-f`, smo naglasili da želimo da sečemo po poljima.
Drugom opcijom, opcijom `-d`, smo naveli koji simbol predstavlja delimiter (to je kod nas dvotačka).
U ovom primeru je to bilo neophodno, jer, podrazumevano, komanda `cut` za delimiter smatra tab.
Primetimo da je rezultat dat spojen preciziranim delimiterom (dvotačkom).
Pri izdvajanju samo jedne kolone (recimo, prve), delimiter se ne javlja u rezultatu:
```bash
$ cut -f 1 -d : /etc/passwd
```
```
root
daemon
bin
sys
sync
...
```

Ako želimo da sečemo po karakterima, to možemo da uradimo navođenjem opcije `-c`.
Na primer, izdvajanje prva četiri karaktera svake linije, može se uraditi na sledeći način:
```bash
$ cut /etc/passwd -c 1-4
```
```
root
daem
bin:
sys:
sync
...
```

## Komanda `tr`

Naziv komande `tr` je skraćeno za `translate` ili `transliterate`.
Osnovna primena je u transformaciji teksta.
Primer:
```bash
$ tr ',' ' '
this line has no commas
this line has no commas
however, this line, certainly, has.
however  this line  certainly  has.
^C
```
Primer:
```bash
$ cut -f 1-4 -d : /etc/passwd | head -n 5 | tr : '\t'
```
```
root	x	0	0
daemon	x	1	1
bin	x	2	2
sys	x	3	3
sync	x	4	65534
...
```

