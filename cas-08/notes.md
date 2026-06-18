# Osma nedelja vežbi

Ove nedelje je dat uvod u programski jezik Pajton.

## Pajton interpreter

Iako ćemo pisati Pajton skripte kojima ćemo rešavati konkretne probleme, veoma je koristan i *Pajton interpreter*.
Ovaj interpreter je strukture REPL (eng. *read, execute, print, loop*). To znači da služi za čitanje datog ulaza, zatim izvršavanje, to jest interpretiranje tog ulaza, štampanje rezultata izvršavanja, i zatim iznova.

### Pokretanje interpretera
Interpeter se poziva komandom `python` ili `python3` (u zavisnosti od verzije interpretera koji se koristi):
```bash
$ python3
```
```
Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```
(Čeka se unos korisnika.)

### Izlazak iz okruženja
Iz okruženja se može izaći korišćenjem funkcije `exit`:
```python
>>> exit()
```
ili funkcije `quit`:
```python
>>> quit()
```
ili unosom CTRL+D sa tastature (kraj linije).

### Rad u okruženju
Interpreteru se može proslediti izraz:
```python
>>> 5 + 3
```
Nakon izračunavanja, dobijamo izlaz:
```
8
```

### Funkcija `help`
Funkcija `help` je dobar alat za pomoć oko dokumentacije u Pajtonu.
Preko nje možemo pristupiti dokumentaciji modula, funkcija, ključnih reči itd.
Na primer,
```python
help(print)
```
ili
```python
import sys
help(sys)
```

## Ispis na standardni izlaz, funkcija `print`
Funkcija `print` služi za štampanje sadržaja na standardni izlaz.
```python
>>> print("Hello!")
```
```
Hello!
```

```python
>>> print(2026)
```
```
2026
```

## Čitanje sa standardnog ulaza, funkcija `input`
Učitavanje sadržaja sa standardnog ulaza se može uraditi funkcijom `input`.
```python
>>> x = input()
```
```
26
```
Prethodnim pozivom se učitava vrednost sa standardnog ulaza i upisuje u promenljivu `x`.
Voditi računa da se podrazumevano vraća niska.
To možemo videti prikazom promenljive `x` i njenog tipa, funkcijom `type`:
```python
>>> x, type(x)
```
```
('26', <class 'str'>)
```
Ostali tipovi se moraju eksplicitno kastovati.
Na primer, ukoliko smo prethodnim pozivom želeli da učitamo ceo broj, morali bismo eksplicitno kastovati:
```python
>>> x = int(input())
```
```
26
```
Sada dobijamo celobrojnu vrednost:
```python
>>> x, type(x)
```
```
(26, <class 'int'>)
```

Ukoliko se funkciji `input` prosledi niska kao argument, ta niska će biti ispisana pre unosa.
Na primer:
```python
>>> x = int(input("Molimo, unesite broj: "))
```
```
Molimo, unesite broj: 2026
```

## Osnovno o tipovima

### Niske

Niske se navode između navodnika, bilo jednostrukih (`'`) ili dvostrukih (`"`).

Primer sa jednostrukim navodnicima:
```python
>>> 'this is a string'
```
```
'this is a string'
```

Primer sa dvostrukim navodnicima:
```python
>>> "this is also a string"
```
```
'this is also a string'
```

Za razliku od Beša, gde je razlika bila suptilna, ali veoma važna, u Pajtonu nema razlike između navođenja niski jednostrukim i dvostrukim navodnicima.

Niske su tipa `str`:
```python
>>> type("a string")
```
```
<class 'str'>
```

### Celi brojevi

Primer celog broja:
```python
>>> 44
```
```
44
```

Tip celog broja je `int`:
```python
>>> type(-23)
```
```
<class 'int'>
```

### Realni brojevi

Primer realnog broja:
```python
>>> 21.5
```
```
21.5
```

Tip realnog broja je `float`:
```python
>>> type(16.33)
```
```
<class 'float'>
```

### Aritmetika

Nad brojevima imamo definisane očekivane operacije sabiranja, oduzimanja, množenja, deljenja, stepenovanja, itd.
U nastavku prikazujemo odgovarajuće operatore.

#### Sabiranje - operator `+`

```python
>>> 14 + 4
```
```
18
```

#### Oduzimanje - operator `-`

```python
>>> 14 - 4
```
```
10
```

#### Množenje - operator `*`

```python
>>> 14 * 4
```
```
56
```

#### Deljenje - operator `/`

```python
>>> 14 / 4
```
```
3.5
```
Primetimo da se deljenje podrazumevano vrši u domenu realnih brojeva.

#### Celobrojno deljenje

Količnik pri celobrojnom deljenju se određuje operatorom `//`:
```python
>>> 14 // 4
```
```
3
```

Ostatak pri celobrojnom deljenju se određuje operatorom `%`:
```python
>>> 14 % 4
```
```
2
```

#### Stepenovanje

```python
>>> 14 ** 4
```
```
38416
```
ili:
```python
>>> pow(14,4)
```
```
38416
```

### Logičke vrednosti

Logičke vrednosti su u Pajtonu predstavljene tipom `bool`.

Primer logičke vrednosti:
```python
>>> False
```
```
False
```

Tip logičke vrednosti je `bool`:
```python
>>> type(True)
```
```
<class 'bool'>
```

Primeri operacija (logički opreatori `not`, `and` i `or`):
```python
>>> not False
```
```
True
```
```python
>>> False and True
```
```
False
```
```python
>>> True or False
```
```
True
```
Primetimo da se koriste engleske reči za odgovarajuće logičke veznike, a ne simboli `!`, `&&` i `||`, kao što bismo možda očekivali.

## Liste
Liste su ugrađene, mutabilne kolekcije podataka u Pajtonu.

### Pravljenje listi
```python
>>> l = [1, 3, "a string", 5.5]
```
Primetimo da tipovi elemenata mogu da se razlikuju.

### Pristup elementima liste
Liste u Pajtonu podržavaju indeksni pristup.
Indeksiranje počinje nulom.
```python
>>> l[1]
```
```
3
```
Dozvoljeno je pristupanje negativnim indeksom.
Indeksom -1 pristupamo poslednjem elementu, indeksom -2 pretposlednjem i tako dalje.
Primer:
```python
>>> l[-1]
```
```
5.5
```

Liste su mutabilan tip podatka i podržavaju modifkaciju.
Podržavaju i uklanjanje elemenata, kao i brojne druge funkcionalnosti.
Prikažimo neke od korisnih mehanizama za baratanje listama kroz primere u narednim tabelama:

### Modifikovanje liste
| primer | značenje |
|--|--|
| `l[1] = 7` | element liste `l` sa indeksom 1 postaje `7` |
| `l.append(3)` | na kraj liste `l` se dodaje element `3` |
| `l.extend(["word", 1.2])` | lista se proširuje (dodavanjem na kraj) elementima `"word"` i `1.2` |
| `l.insert(2, 13)` | na poziciju sa indeksom 2 se postavlja element `13`, a svi ostali elementi sa indeksom 2 i više se pomeraju "udesno" |

### Uklanjanje elemenata liste
| primer | značenje |
|--|--|
| `l.remove(3)` | uklanja se prvo pojavljivanje elementa `3` u listi `l` |
| `del l[2]` | uklanja se element na poziciji sa indeksom 2 u listi `l` |
| `l.pop(2)` | ekvivalentno ponašanje kao iznad (povratna vrednost je uklonjeni element) |
| `l.pop()` | isto, ali se podrazumevano uklanja poslednji element liste `l` |
| `l.clear()` | uklanjaju se svi elementi liste `l` |

### Korisne operacije i funkcije
| primer | značenje |
|--|--|
| `len(l)` | određuje se dužina liste `l` |
| `elem in l` | proverava se da li `elem` pripada listi `l` |
| `l.sort()` | lista `l` se sortira (u mestu) |
| `sorted(l)` | lista `l` se sortira, ali ne u mestu, nego se rezultujuća sortirana lista vraća kao povratna vrednost funkcije |
| `l.reverse()` | određuje se lista sa elementima u obrnutnom redosledu u odnosu na listu `l` |
| `l.count("apple")` | određuje se broj pojavljivanja elementa `"apple"` u listi `l` |

## Operator za isecanje sekvenci
Liste i niske podržavaju operator za isecanje sekvenci (eng. *slice operator*).
Sintaksa je sledeća:
```python
object[start:end:step]
```
pri čemu je:
- `object` objekat čiju podsekvencu tražimo;
- `start` indeks početka te podsekvence (uključujući i element na toj poziciji);
- `end` indeks kraja podsekvence (*ne* uključujući element na toj poziciji);
- `step` korak kojim se uzimaju elementi objekta.
Pokažimo ovo na primeru liste:
```python
>>> l = [2, 1, 7, -3, 0]
```

Izdvojimo elemente na pozicijama 2 i 3:
```python
>>> l[2:4:1]
```
```
[7, -3]
```

Ukoliko je korak 1, `step` se može izostaviti:
```python
>>> l[2:4:]
```
```
[7, -3]
```
ili, još kraće:
```python
>>> l[2:4]
```
```
[7, -3]
```

Ukoliko se `end` izostavi, uzimaju se elementi do kraja liste:
```python
>>> l[2:]
```
```
[7, -3, 0]
```

Ukoliko se `start` izostavi, uzimaju se elementi od početka liste:
```python
>>> l[:4]
```
```
[2, 1, 7, -3]
```

Izostavljanjem i `start` i `end`, dobijamo celu listu:
```python
>>> l[:]
```
```
[2, 1, 7, -3, 0]
```
Izdvojimo još i svaki drugi element liste (počevši od prvog, to jest na poziciji 0):
```python
>>> l[::2]
```
```
[2, 7, 0]
```

Isto ponašanje važi i za niske (i za razne druge tipove, ali nama će samo liste i niske biti važne).

```python
>>> message = "Warm greetings!"
```
```python
>>> message[5:-1]
```
```
'greetings'
```

## Kontrola toka
Pogledajmo kako se upravlja kontrolom toka izvršavanja u Pajtonu.

### Grananje
Grananje se postiže naredbama `if`, `else` i `elif`.

Osnovna struktura:
```python
if condition:
    # do something
elif other_condition:
    # do another thing
else:
    # do something else
```

Na primer:
```python
>>> x = 7
>>> if x < 5:
...     print("Manje je od 5.")
... elif x < 10:
...     print("Nije manje od 5, ali je manje od 10")
... else:
...     print("Vece je od (ili jednako) 10")
...
```
``` 
Nije manje od 5, ali je manje od 10
```

Možemo primetiti da nemamo višelinijske blokove (korišćenjem, na primer, `{` i `}`, kao u programskom jeziku C++).
Blokovi grana `then` i `else` se određuju *indentacijom*!
Sve linije koda koje se odnose na određeni blok, moramo ravnomerno nazubiti.
Ovo važi i za grananje, ali i za petlje i funkcije o kojima će biti reči u nastavku.

### Petlje
Pogledajmo kako se realizuju petlje u Pajtonu.

### `while` petlja
Osnovna sintaksa je:
```python
while condition:
    # do something
```
Na primer:
```python
i = 1
while i <= 5
    print(i)
```

### `for` petlja
U Pajtonu postoji "for each" konstrukcija:
```python
for element in collection:
    # do something
```
Na primer:
```python
>>> numbers = [1, 2, 3]
>>> for x in numbers:
...     print(x)
... 
```
```
1
2
3
```

Ne postoji "tradicionalna" `for` petlja (u stilu programskih jezika C ili C++, na primer):
```python
for i = 0; i < 10; i++:
    # do something with number i
```
Ovo ponašanje se postiže na sledeći način:
```python
for i in range(10):
    # do something with number i
```

## Funkcije

Sintaksa za definisanje funkcija je sledeća:
```python
def function_name(arguments):
    # do something
```

Na primer:
```python
>>> def add(x, y):
...     return x + y
... 
```

```python
>>> add(3, 7)
```
```
10
```
Razlikujemo *pozicione* argumente funkcija, koji moraju biti navedeni u onom redosledu u kom su navedeni u potpisu funkcije, i *imenovane* argumente, koji se mogu navesti u tom redosledu, ali se mogu navesti i svojim imenom.
Imenovani argumenti se moraju navesti nakon pozicionih.
Redosled imenovanih argumenata nije važan.
Na primer:
```python
>>> def calculate(x, y, z=0, t=1):
...     return (x - y + z) / t
...
```

Primer poziva funkcije gde su svi argumenti pozicioni:
```python
>>> calculate(3, 1, 7, 3)
```
```
3.0
```

Argumenti sa podrazumevanim vrednostima se mogu izostaviti:
```python
>>> calculate(3, 1, 4)
```
```
6.0
```
```python
>>> calculate(3, 1)
```
```
2.0
```

U sledećem primeru, `t` je imenovani argument:
```python
>>> calculate(3, 1, t=4)
```
```
0.5
```

Redosled imenovanih argumenata nije važan:
```python
>>> calculate(3, 1, z=8, t=4)
```
```
2.5
```
```python
>>> calculate(3, 1, t=4, z=8)
```
```
2.5
```

Možemo čak sve argumente navesti kao imenovane:
```python
>>> calculate(y=1, t=4, z=8, x=3)
```
```
2.5
```

### Mutabilnost i argumenti funkcija

Neki objekti u Pajtonu mogu da se izmene *u mestu*, to jest bez pravljenja novog objekta.
Takve objekte nazivamo mutabilnim objektima.
Ako objekat ne može da se izmeni u mestu, nego se za izmenjenu vrednost mora napraviti novi objekat, kažemo da je taj objekat imutabilan.

Liste (`list`) su mutabilne.
To znači da možemo promeniti element postojeće liste ili joj dodati novi element:
```python
>>> l = [1, 2, 3]
>>> l[0] = 10
>>> l.append(4)
>>> l
[10, 2, 3, 4]
```
U ovom primeru nismo pravili novu listu, već smo izmenili postojeću listu `l`.

Niske (`str`) nisu mutabilne.
To znači da ne možemo promeniti pojedinačni karakter postojeće niske:
```python
>>> s = "hello"
>>> s[0] = "H"
Traceback (most recent call last):
  ...
TypeError: 'str' object does not support item assignment
```
Ukoliko želimo promenjenu nisku, potrebno je napraviti novu nisku:
```python
>>> s = "H" + s[1:]
>>> s
'Hello'
```
U ovom primeru ime `s` nakon dodele pokazuje na novu nisku.

Od tipova koje smo do sada pomenuli, mutabilne su liste (`list`).
Imutabilni su celi brojevi (`int`), realni brojevi (`float`), logičke vrednosti (`bool`) i niske (`str`).

Ovo je posebno važno kada objekte prosleđujemo funkcijama.
Ako funkcija dobije mutabilan objekat, ona može da izmeni taj isti objekat, pa će izmena biti vidljiva i nakon izlaska iz funkcije:
```python
>>> def dodaj_element(l):
...     l.append("novi element")
...
>>> l = [1, 2, 3]
>>> dodaj_element(l)
>>> l
[1, 2, 3, 'novi element']
```
Sa druge strane, ako funkcija dobije imutabilan objekat, ona ne može da izmeni taj objekat.
Ako u funkciji promenimo vrednost parametra, to ne menja promenljivu iz koje je argument prosleđen:
```python
>>> def uvecaj(x):
...     x += 1
...
>>> x = 10
>>> uvecaj(x)
>>> x
10
```
Ukoliko nam je potrebna promenjena vrednost imutabilnog objekta, funkcija treba da je vrati kao povratnu vrednost:
```python
>>> def uvecana_vrednost(x):
...     return x + 1
...
>>> x = uvecana_vrednost(x)
>>> x
11
```

## Pisanje skriptova
Osim korišćenja Pajton interpretera, nama će, naravno, osnovni cilj biti pisati skriptove.
Skript pišemo u posebnom fajlu koji obično imenujemo sa ekstenzijom `.py`.

Dajmo primer najjednostavnijeg skripta, `hello_world.py`:
```python
print("Hello, world!")
```
Skript pozivamo pozivom interpretera, kome kao argument prosleđujemo naziv skripta:
```bash
$ python3 hello_world.py
```
Izlaz:
```
Hello, world!
```

Kao i kod Beša, na početku skripta pišemo `#!` (eng. *shebang*), uz putanju do interpretera koji koristimo, što je kod nas `python` (ili `python3`).
```python
#!/usr/bin/python3

print("Hello, world!")
```
Na taj način, skript možemo pozvati sa:
```bash
$ ./hello_world.py
```

### Komentari
Komentari počinju simbolom `#` i traju do kraja linije.
```python
#!/usr/bin/python3

# This line prints a hello message.
print("Hello, world!")
```
Višelinijski komentari ne postoje, ali se mogu napraviti navođenjem višelinijskih niski.
Na primer:
```python
"""
This block contains multiple lines.
All of these lines are considered comments.
They will all be ignored by the interpreter.
"""
```
Ova višelinijska niska će biti ignorisati od strane interpretera (to jest, neće imati nikakav smisleni uticaj prilikom interpretacije skripta), pa efektivno služi kao višelinijski komentar.
