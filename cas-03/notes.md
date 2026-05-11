# Treća nedelja vežbi

Na ovom času je rađena kontrola toka kroz konstrukte `while`, `until`,
`case` i funkcija, u programskom jeziku Beš.
Pored toga, rađeni su i primeri sa šel aritmetikom i pomenut pojam *glob*
([*globbing*][glob-wiki]).

## Naredba `case`

Naredba `case` predstavlja višestruku naredbu grananja u programskom jeziku
Beš.
Njena sintaksa je sledeća:
```bash
case NISKA in
    slucaj1|slucaj2|slucaj3)
        # naredbe
    ;;
    slucaj4|slucaj5)
        # naredbe
    ;;
    *)
        # naredbe koje se izvrsavaju u svim ostalim slucajevima
    ;;
esac
```
Na primer, sledeći program proverava da li korisnik prihvata poruku sa
standardnog ulaza:
```bash
read -p "Accept the message? " answer
case "$answer" in
    y|Y|yes|Yes|YES)
        echo "Message accepted"
    ;;
    n|N|no|No|NO)
        echo "Message rejected."
    ;;
    *)
        echo "Unsupported option."
    ;;
esac
```

## Naredba `while`

Naredba `while` se koristi za ponavljanje naredbi sve dok zadati uslov ne
postane netačan.
Njena sintaksa je:
```bash
while USLOV
do
    # naredbe
done
```
Poput naredbi `if` i `for`, često se zapisuje u skraćenom obliku:
```bash
while USLOV; do
    # naredbe
done
```
Izraz `USLOV` može biti uslov kao u naredbi grananja `if`.

Na primer, sledeći program učitava sa standardnog ulaza broj sve dok se ne
unese odgovarajući ključ.
```bash
key=10
read -p "Enter the key: " num
while [ "$num" -ne "$key" ]; do
    read -p "Wrong key! Try again: " num
done
echo "Correct!"
```
## Naredba `until`

Naredba `until` je tip petlje koji se koristi za ponavljanje naredbi sve dok
zadati uslov ne postane tačan.
Njena sintaksa je:
```bash
until USLOV
do
    # naredbe
done
```
Ili, skraćeno:
```bash
until USLOV; do
    # naredbe
done
```

Izraz `USLOV` može biti bilo koji uslov koji se može zadati u naredbama `if`
ili `while`.

Na primer, sledeći kod u petlji čeka da se kreira fajl sa imenom `signal.txt`:
```bash
until [ -f signal.txt ]; do
    echo "Waiting for the signal file..."
    sleep 2
done
echo "Signal received!"
```

*Napomena*: Naredba `until` se može zameniti naredbom `while` sa negiranim
uslovom.
Odnosno, prethodna petlja je ekvivalentna sledećoj:
```bash
while ! [ -f signal.txt ]; do
    echo "Waiting for the signal file..."
    sleep 2
done
echo "Signal received!"
```

## Funkcije u Bešu

Beš podržava rad sa funkcijama.
Funkcije se mogu shvatati kao podskripte i kao takve mogu da se pozivaju u
okviru skripte u kojoj su definisane.
Funkcije mogu da se definišu na dva istovetna načina:
```bash
function nova_funkcija {
    # naredbe
}
```
ili
```bash
nova_funkcija() {
    # naredbe
}
```
Parametri se funkcijama dodeljuju prilikom poziva (na identičan način kao kada
se poziva Beš skripta), a u samoj funkciji im se pristupa pomoću specijalnih
promenljivih `$1`, `$2`, ...

Na primer, izlaz sledećeg programa:
```bash
print_header() {
    echo -n "Student Info: "
}

print_student() {
    if [ "$#" -ne 2 ]; then
        echo "print_student requires name and surname"
        exit 1
	fi
    echo "$1" "$2"
}

print_header
print_student Petra Petrovic
```
je:
```bash
Student Info: Petra Petrovic
```

*Napomena*: Poziv funkcije **ne** kreira podproces već se izvršava u okviru
istog šel procesa.
Zato, na primer, promena direktorijuma u funkciji menja trenutni radni
direktorijum skripte koja se izvršava.
```bash
change_dir() {
    cd /home/sp/documents
}

pwd             # /home/sp/downloads
change_dir
pwd             # /home/sp/documents
```

## Šel aritmetika

Već je pomenuto tokom druge nedelje vežbi da se aritmetički izrazi mogu
izračunati pomoću ekspanzije `$((...))`.
Na primer, prvih `n` prirodnih brojeva možemo da ispišemo pomoću narednog
programa:
```bash
n="$1"
i=0
while [ "$i" -lt "$n" ]; do
    echo "$i"
    i=$((i + 1))
done
```
Aritmetičke operacije se mogu sprovesti i korišćenjem konstrukta `((...))`.
Za razliku od aritmetičkih ekspanzija koje predstavljaju vrednost izraza,
izrazi koji koriste `((...))`, predstavljaju aritmetičke komande.
To znači da njih ne posmatramo kao vrednosti, već kao komande.

Ispisivanje prvih `n` prirodnih brojeva se pomoću aritmetičkih komandi može
uraditi na sledeći način:
```bash
n="$1"
((i = 0))
while (( i < n )); do
    echo "$i"
    (( i++ ))
done
```
Vidimo da se u konstruktima `((...))` nalaze operatori dodele i poređenja,
odnosno, `(( i++ ))` predstavlja postinkrement promenljive `i`, dok
`$((i + 1))` predstavlja vrednost promenljive `i` uvećanu za `1`.

Aritmetičke komande proširuju i `for` petlje tako što omogućavaju sledeću
sintaksu:
```bash
# ispisivanje prvih n prirodnih brojeva
for ((i = 0; i < n; i++)); do
    echo "$i"
done
```

## Globing u šelu

Šel podržava prepoznavanje skupa fajlova na osnovu njihovih imena pomoću
paterna.
Paterni za prepoznavanje sadrže specijalne karaktere koji služe za opisivanje
složenijih pravila u imenima, a mehanizam koji ih podržava se naziva
globing (eng. *globbing*).

Specijalni karakteri:
- `*` - prepoznaje nisku proizvoljne dužine (može biti i prazna)
- `?` - prepoznaje jedan proizvoljan karakter
- `[...]` - prepoznaje neki od karaktera između zagrada `[` i `]`;
dozvoljeno je koristiti karakter `-` za navođenje opsega karaktera
- `[!...]` - prepoznaje bilo koji karakter osim onih između zagrada `[` i `]`;
dozvoljeno je koristiti karakter `-` za navođenje opsega karaktera

### Primeri

Ako je sadržaj trenutnog direktorijuma sledeći:
```bash
$ ls
1.txt  3.txt  abc.sh  a.c     a.txt  b.txt  c.txt
2.txt  4.txt  ab.txt  ac.txt  b.c    c.c    xyz.sh
```
Onda se narednim komandama ispisuju:
- Svi fajlovi koji se završavaju sa `.txt`
```bash
$ echo *.txt
1.txt 2.txt 3.txt 4.txt ab.txt ac.txt a.txt b.txt c.txt
```
- Svi fajlovi koji sadrže tačno jedan karakter nakon koga sledi `.txt`
```bash
$ echo ?.txt
1.txt 2.txt 3.txt 4.txt a.txt b.txt c.txt
```
- Svi fajlovi koji imaju ekstenziju koja sadrži tačno dva karaktera
```bash
$ echo *.??
abc.sh xyz.sh
```
- Svi fajlovi koji u imenu sadrže slovo abecede nakon kog sledi `.txt`
```bash
$ echo [a-z].txt
a.txt b.txt c.txt
```
- Svi fajlovi koji u imenu sadrže karakter koji nije slovo abecede, a nakon kog
sledi `.txt`
```bash
$ echo [!a-z].txt
1.txt 2.txt 3.txt 4.txt
```

[glob-wiki]: https://en.wikipedia.org/wiki/Glob_(programming)
