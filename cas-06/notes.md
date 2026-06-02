# Šesta nedelja vežbi

Ove nedelje obrađene su komande `grep`, `sed`, `sort` i `uniq`. Primenjeno je znanje regularnih izraza na rešavanje zadataka koji zahtevaju manipulaciju tekstom.

## Komanda `grep`

Alat *grep* je alat komandne linije koji omogućava pretragu teksta pomoću
regularnih izraza.
Opšti poziv komande je
```bash
grep [opcije] REGEX ulaz
```
gde je `REGEX` regularni izraz kojim pretražujemo, dok `ulaz` predstavlja jedan
ili više fajlova.
Ukoliko se argument `ulaz` izostavi, grep čita podatke sa standardnog ulaza.

koji predstavlja
niz fajlova, a ukoliko se izostavi, predstavlja standardni ulaz.
*grep* podrazumevano ispisuje **sve linije** ulaza koje imaju poklapanje sa
regularnim izrazom u sebi.

Na primer, neka je sadržaj fajla *ulaz.txt* sledeći:
```
macka spava mirno
Adresa je Kralja 5
Video sam macka
Bus 23 stize rano
macka ceka veceru
Termin je u 14:30
Pada slaba kisa
```
Tada komanda
```bash
grep 'macka' ulaz.txt
```
ispisuje
```
macka spava mirno
Video sam macka
macka ceka veceru
```
odnosno sve linije fajla *ulaz.txt* koje sadrže reč *macka*.

*Napomena*: Opcija `--color` boji tekst koji je poklopljen regularnim izrazom,
čime možemo da vidimo šta je tačno poklopljeno na svakoj liniji.
Ova opcija može biti korisna prilikom otkrivanja grešaka u regularnom izrazu.

Podrazumevano *grep* koristi osnovne regularne izraze.
Opcija `-E` (odnosno, `--extended-regexp`) uključuje proširene regularne izraze
koji omogućavaju direktnu upotrebu operatora poput `+`, `?` i `{}`.

Primer: Komanda
```bash
$ grep -E '[0-9]+' ulaz.txt
Adresa je Kralja 5
Bus 23 stize rano
Termin je u 14:30
```
ispisuje sve linije fajla *ulaz.txt* koje sadrže brojeve.

*Napomena*: *grep* (bez dodatnih opcija) ne podržava skraćenicu `\d` za
karaktersku klasu za cifre, zato je neophodno pisati `[0-9]`.

Nekada nam su nam od interesa samo poklapanja, a ne i cele linije koje ih
sadrže.
Opcija `-o` (ili `--only-matching`) ispisuje samo prepoznati tekst.

Primer:
```bash
$ grep -E -o '[0-9]+' ulaz.txt
5
23
14
30
```

Alat *grep* može da prihvata više fajlova pri čemu u tom slučaju izvršava
pretragu u svakom i na izlazu ispisuje u kom fajlu je došlo do poklapanja.

Primer:
```bash
$ grep -Eo '[0-9]+' ulaz.txt test.txt
ulaz.txt:5
ulaz.txt:23
ulaz.txt:14
ulaz.txt:30
test.txt:12
test.txt:18
test.txt:27
test.txt:154
test.txt:45
test.txt:8
```
Ukoliko ne želimo ispis fajlova u kom je došlo do prepoznavanja, možemo da
dodamo opciju `-h` (ili `--no-filename`).

```bash
$ grep -Eoh '[0-9]+' ulaz.txt test.txt
5
23
14
30
12
18
27
154
45
8
```

## Komanda `sed`

Komanda `sed` (eng. ***s**tream **ed**itor*) je moćan alat za manipulaciju teksta.
Podržava supstituciju, brisanje i umetanje teksta.
Mi se fokusiramo na supstituciju.

Supstitucija teksta se vrši navođenjem konstrukcije `s/target/replacement/options`, pri čemu:
- `target` je ono što želimo da bude zamenjeno;
- `replacement` je ono čime želimo da bude zamenjeno;
- `options` su opcije koje želimo da uključimo prilikom supstitucije.

Na primer, `s/macka/pas/` služi za zamenu teksta `macka` tekstom `pas`.

Komanda `sed` podržava rad sa regularnim izrazima.
Na primer:
```bash
$ echo "cats, bats and rats!" | sed 's/.ats/dogs/'
```
```
dogs, bats and rats!
```

Primetimo da je zamenjeno samo prvo pojavljivanje šablona.
Podrazumevano, menja se samo prvo pojavljivanje u svakoj liniji ulaza.
Opcijom `g`, supstitucije se može učiniti globalnom, to jest, izvršiti nad svakom prepoznatom instancom navedenog šablona:
```bash
$ echo "cats, bats and rats!" | sed 's/.ats/dogs/g'
```
```
dogs, dogs and dogs!
```

Slično kao kod komande `grep`, i komanda `sed` podržava opciju `-E` koja dozvoljava korišćenje proširenih regularnih izraza u okviru šablona koje dajemo prilikom supstitucije.
Stoga ćemo je koristiti veoma intenzivno maltene kada god budemo radili sa regularnim izrazima.

Na primer, neka je dat fajl `employees.txt`:
```bash
$ cat employees.txt
```
```
# Employee Records
101, Alice Smith, Engineering, $90000
102, Bob Jones, Marketing, $75000
103, Charlie Brown, Engineering, $85000
104, David White, Sales, $60000
105, Eve Black, Engineering, $95000

# Notes:
# - All salaries are annual.
# - Engineering team is growing.
```

Cenzurisanje plata možemo izvršiti na sledeći način:
```bash
$ sed -E 's/\$[0-9]+/[REDACTED]/g' employees.txt
```
```
# Employee Records
101, Alice Smith, Engineering, [REDACTED]
102, Bob Jones, Marketing, [REDACTED]
103, Charlie Brown, Engineering, [REDACTED]
104, David White, Sales, [REDACTED]
105, Eve Black, Engineering, [REDACTED]

# Notes:
# - All salaries are annual.
# - Engineering team is growing.
```

Komanda `sed` ispisuje modifikovani tekst i podrazumevano ne menja sadržaj izvornog fajla.
Opcijom `-i` možemo modifikovati sadržaj fajla u mestu (eng. *in-place*).

```bash
$ cat employees.txt
```
```
# Employee Records
101, Alice Smith, Engineering, $90000
102, Bob Jones, Marketing, $75000
103, Charlie Brown, Engineering, $85000
104, David White, Sales, $60000
105, Eve Black, Engineering, $95000

# Notes:
# - All salaries are annual.
# - Engineering team is growing.
```
```bash
$ sed -E -i 's/\$[0-9]+/[REDACTED]/g' employees.txt
```
```bash
$ cat employees.txt
```
```
# Employee Records
101, Alice Smith, Engineering, [REDACTED]
102, Bob Jones, Marketing, [REDACTED]
103, Charlie Brown, Engineering, [REDACTED]
104, David White, Sales, [REDACTED]
105, Eve Black, Engineering, [REDACTED]

# Notes:
# - All salaries are annual.
# - Engineering team is growing.
```

## Komanda `sort`

Komanda `sort`, kao što joj ime kaže, sortira prosleđeni tekstualni sadržaj.
Taj sadržaj može biti zadat sa standardnog ulaza ili kao argument komande.
Stavke koje ova komanda sortira su linije, a ne i njihov sadržaj (na primer, reči u okviru njih).

Primer:
```bash
$ cat continents.txt
```
```
South America
Australia
North America
Africa
Asia
Europe
Antarctica
```
```bash
$ sort continents.txt
```
```
Africa
Antarctica
Asia
Australia
Europe
North America
South America
```

Opcijom `-r` sortiramo u obrnutom redosledu:
```bash
$ sort -r continents.txt
```
```
South America
North America
Europe
Australia
Asia
Antarctica
Africa
```

Razmotrimo fajl `numbers.txt`:
```bash
$ cat numbers.txt
```
```
3000
25
100
250
```

Njegovim sortiranjem dobijamo:
```bash
$ sort numbers.txt
```
```
100
25
250
3000
```

Ovo ponašanje je korektno (jer se sortiranje vrši leksikografski), ali, ukoliko želimo da razmatramo numeričke vrednosti stavki koje se sortiraju, koristićemo opciju `-n`:
```bash
$ sort -n numbers.txt
```
```
25
100
250
3000
```

Ako hoćemo da sortiramo tekstualni sadržaj čije se linije sastoje od više reči, to možemo uraditi pomoću opcije `-k`.
Na primer, neka je dat fajl `fish.txt` koji sadrži informacije o različitim vrstama ribe:
```
Marlin          1       350.00
Tuna            3       41.25
Sardine         500     0.05
Halibut         3       58.40
Snapper         12      18.75
MahiMahi        8       22.00
Swordfish       3       72.10
```
Informacije su podeljene u tri kolone: ime vrste, količina i cena po jedinici (tim redom).
Ukoliko želimo da sadržaj uredimo po nazivu, to možemo uraditi jednostavnim pozivom komande `sort`:
```bash
$ sort fish.txt
```
```
Halibut         3       58.40
MahiMahi        8       22.00
Marlin          1       350.00
Sardine         500     0.05
Snapper         12      18.75
Swordfish       3       72.10
Tuna            3       41.25
```
Ovo radi jer je naziv vrste ribe ujedno i prva kolona, pa predstavlja početak linije.
Međutim, ukoliko želimo da sortiramo po nekoj drugoj koloni (recimo, drugoj - količina), koristimo opciju `-k`:
```bash
$ sort -k 2 fish.txt
```
```
Snapper         12      18.75
Marlin          1       350.00
Tuna            3       41.25
Halibut         3       58.40
Swordfish       3       72.10
Sardine         500     0.05
MahiMahi        8       22.00
```

Da bismo sortirali po numeričkoj vrednosti, navodimo opciju uređivanja `n`:
```bash
$ sort -k 2n fish.txt
```
```
Marlin          1       350.00
Halibut         3       58.40
Swordfish       3       72.10
Tuna            3       41.25
MahiMahi        8       22.00
Snapper         12      18.75
Sardine         500     0.05
```
Naglasimo da se opcija uređivanja `n` ovde odnosi samo na ključ opisan opcijom `-k`.
Ukoliko hoćemo da važi globalno, onda je navodimo kao zasebnu opciju (`-n`).

Navođenjem broja 2 u opciji `-k` smo opisali da želimo da ključ za sortiranje bude deo linije koji *počinje* od drugog polja.
Podrazumevano, *kraj* ključa je kraj linije.
Stoga, opcijom `-k 2` smo sortirali po ključu koji se sastojao od drugog *i* od trećeg polja (to jest, kolone).
Dakle, uzimali smo u obzir i treću kolonu (cenu), a to formalno nismo hteli.
Ukoliko želimo da ključ suzimo na *tačno* drugo polje:
```bash
$ sort -k 2,2n fish.txt
```
```
Marlin          1       350.00
Halibut         3       58.40
Swordfish       3       72.10
Tuna            3       41.25
MahiMahi        8       22.00
Snapper         12      18.75
Sardine         500     0.05
```
Možemo videti da nam u ovom primeru to nije bilo problematično, ali za neke druge vrednosti je moglo da bude.

Primetimo: linije koje se odnose na vrste `Halibut`, `Swordfish` i `Tuna` su jednake po ključu koji smo precizirali (vrednost je 3), pa su upoređene *u celosti* (što kod nas ima za rezultat da su sortirane po nazivu, jer linije počinju nazivom).

Možemo definisati više ključeva za sortiranje.
Sortirajmo sadržaj, kao malopre, po količini, a vrste ribe koje su date u istoj količini uredimo po ceni, opadajuće:
```bash
$ sort -k 2,2n -k 3,3nr fish.txt
```
```
Marlin          1       350.00
Swordfish       3       72.10
Halibut         3       58.40
Tuna            3       41.25
MahiMahi        8       22.00
Snapper         12      18.75
Sardine         500     0.05
```

Mogli smo hteti da vrste ribe koje su date u istoj količini ne uređujemo *uopšte*, to jest, da ne navodimo ni dodatne ključeve za sortiranje, niti da dopuštamo da se izjednačeni rezultati upoređivanja razrešavaju upoređivanjem čitavih linija.
Drugim rečima, linije sa istim vrednostima druge kolone smo hteli da se navode u redosledu u kom su date originalno.
To se postiže *stabilnim sortiranjem* koje komanda `sort` podržava kroz opciju `-s`:
```bash
$ sort -s -k 2,2n fish.txt
```
```
Marlin          1       350.00
Tuna            3       41.25
Halibut         3       58.40
Swordfish       3       72.10
MahiMahi        8       22.00
Snapper         12      18.75
Sardine         500     0.05
```

Razmotrimo sada isti sadržaj u CSV formatu (fajl `fish.csv`):
```bash
$ cat fish.csv
```
```
Marlin,1,350.00
Tuna,3,41.25
Sardine,500,0.05
Halibut,3,58.40
Snapper,12,18.75
MahiMahi,8,22.00
Swordfish,3,72.10
```

Kod komande `sort`, polja se smatraju skupovima ne-belina razdvojenih belinama.
Prema tome, da bismo u ovom slučaju izvršili sortiranje po drugoj koloni, moramo naglasiti da je razdvajač kolona zapeta (`,`).
Ovo postižemo opcijom `-t`:
```bash
$ sort -t ',' -k 2,2n fish.csv
```
```
Marlin,1,350.00
Halibut,3,58.40
Swordfish,3,72.10
Tuna,3,41.25
MahiMahi,8,22.00
Snapper,12,18.75
Sardine,500,0.05
```
Za kraj ove sekcije, prikažimo da je bilo veoma važno da smo u prethodnoj komandi u opciji `-k` naveli `2,2`, a ne `2`:
```bash
$ sort -t ',' -k 2n fish.csv
```
```
Tuna,3,41.25
Halibut,3,58.40
Swordfish,3,72.10
MahiMahi,8,22.00
Snapper,12,18.75
Marlin,1,350.00
Sardine,500,0.05
```
Kako se navođenjem `2` naglašava da ključ *počinje* drugim poljem to je, efektivno, kao da sortiramo po ključevima:
```
1,350.00
3,41.25
500,0.05
3,58.40
12,18.75
8,22.00
3,72.10
```
(pogledati sadržaj fajla `fish.csv`, dat iznad).
Primetimo da su zapete i dalje deo ključa, iako je ključ opisan kao "od drugog polja".

## Komanda `uniq`

Komanda `uniq` (eng. *unique* - jedinstven) služi za eliminaciju linija duplikata iz datog tekstualnog ulaza.
Ova komanda dozvoljava ulaz direktno sa standardnog ulaza, mada ćemo je mi koristiti ili tako što ćemo joj operatorom cevi proslediti izlaz prethodne komande ili tako što ćemo je primeniti direktno nad nekim fajlom.
Na primer, ako imamo fajl `fruits.txt`:
```bash
$ cat fruits.txt
```
```
Apple
Apple
apple
Banana
Orange
Banana
Banana
Grape
```
Primenom komande `uniq` dobijamo:
```bash
$ uniq fruits.txt
```
```
Apple
apple
Banana
Orange
Banana
Grape
```
Primetimo:
1. Eliminisana su samo *susedna* pojavljivanja duplikata (u rezultatu imamo `Banana` dva puta);
2. Pri eliminaciji su razlikovana velika od malih slova (obe linije, `Apple` i `apple`, su deo rezultata primene komande).

Prvo svojstvo je regularno ponašanje komande.
U slučaju da ne želimo da eliminišemo samo susedna ponavljanja, već ponavljanja na nivou celog prosleđenog fajla (ili direktno sa ulaza) to možemo postići tako što prvo sortiramo sadržaj, a potom primenimo komandu `uniq`:
```bash
$ sort fruits.txt | uniq
```
```
apple
Apple
Banana
Grape
Orange
```
(sada ostaje samo jedna linija `Banana`).

Ukoliko ne želimo da komanda bude osetljiva na razliku između malih i velikih slova, možemo joj proslediti opciju `-i`:
```bash
$ uniq -i fruits.txt
```
```
Apple
Banana
Orange
Banana
Grape
```

Obe varijante u kombinaciji (eliminacija ponavljanja u celom fajlu, bez obzira na razliku između velikih i malih slova):
```bash
$ sort fruits.txt | uniq -i
```
```
apple
Banana
Grape
Orange
```
Primetimo da je u rezultatu sada ostala linija `apple` (sa malim prvim slovom), jer je sortiranjem dospela pre linije `Apple` (sa velikim prvim slovom).

Opcijom `-d` prikazuju se samo duplikati.
```bash
$ uniq -d fruits.txt
```
```
Apple
Banana
```
S druge strane, opcijom `-u` se izdvajaju samo ne-duplikati, to jest jedinstvene linije.
```bash
$ uniq -u fruits.txt
```
```
apple
Banana
Orange
Grape
```

Opcijom `-c` se, uz duplikate, izdvaja i njihov broj:
```bash
$ uniq -c fruits.txt
```
```
      2 Apple
      1 apple
      1 Banana
      1 Orange
      2 Banana
      1 Grape
```

Iako je na prethodnom primeru razmatran fajl sa nepraznim linijama koje se sastoje od samo po jedne reči, vredi naglasiti da komanda `uniq` razmatra i prazne linije, a kod nepraznih linija se razmatra sadržaj *čitave* linije (ne, na primer, samo prve reči).

```bash
$ cat animals.txt
```
```
Cats love dogs.

Cats!



Dogs love cats.
Dogs and cats are both awesome.
Dogs and cats are both awesome.
Dogs!


```
```bash
$ uniq animals.txt
```
```
Cats love dogs.

Cats!

Dogs love cats.
Dogs and cats are both awesome.
Dogs!

```
Spojene su samo susedne linije koje su u celosti identične, kao i prazne linije.

## Komande `head` i `tail`

Komande `head` i `tail` služe za izvlačenje početnih i krajnjih linija ulaza.
Obe komande imaju opciju `-n` koja služi za navodjenje broja linija koje treba
izvući.

Neka je sadržaj fajla *ulaz.txt* sledeći:
```
1. Prva
2. Druga
3. Treca
4. Cetvrta
5. Peta
6. Sesta
7. Sedma
8. Osma
9. Deveta
10. Deseta
```
1. Ispisivanje prve tri linije fajla.
```bash
$ head -n 3 ulaz.txt
1. Prva
2. Druga
3. Treca
```
2. Izdvajanje poslednje tri linije fajla.
```bash
$ tail -n 3 ulaz.txt
8. Osma
9. Deveta
10. Deseta
```
3. Izdvajanje od 5. do 7. linije fajla.
```bash
$ head -n 7 ulaz.txt | tail -n 3
5. Peta
6. Sesta
7. Sedma
```

Pored toga, ove komande podržavaju i komplementne operacije, odnosno izdvajanje
svih linija *osim* poslednjih ili prvih *n*. To se postiže dodavanjem znaka `-`
ili `+` ispred broja linija.
Komanda `head -n -N` izdvaja sve linije *osim* poslednjih `N`, dok komanda
`tail -n +N` izdvaja sve linije počev od linije `N` (tj. sve osim prvih `N - 1`)
linija.

Primer:
1. Izdvajanje svih linija fajla osim poslednje 3.
```bash
$ head -n -3 head-tail.txt
1. Prva
2. Druga
3. Treca
4. Cetvrta
5. Peta
6. Sesta
7. Sedma
```

2. Izdvajanje svih linija fajla osim prve 2.
```bash
$ tail -n +3 head-tail.txt
3. Treca
4. Cetvrta
5. Peta
6. Sesta
7. Sedma
8. Osma
9. Deveta
10. Deseta
```

[web-regex101]: https://regex101.com/
