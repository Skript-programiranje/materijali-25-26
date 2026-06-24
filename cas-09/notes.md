# Deveta nedelja vežbi

Ova nedelja predstavlja drugu nedelju uvoda u osnove programskog jezika Pajton.
Obrađeni su neki korisni metodi za rad sa niskama, uvedeni su skupovi, rečnici i torke i prikazan je modul `sys`.
Na kraju su prikazani operatori `==` i `is`, kao i razlika između ta dva operatora.

## Korisni metodi za rad sa niskama

Prilikom rada sa niskama, biće nam korisni određeni odabrani metodi koje navodimo u narednoj tabeli.
U navedenim primerima, `s` je neka unapred zadata niska.
| funkcija | primer poziva | značenje |
|--|--|--|
| `lower` | `s.lower()` | transformacija niske `s` u nisku sa svim malim slovima |
| `upper` | `s.upper()` | transformacija niske `s` u nisku sa svim velikim slovima |
| `islower` | `s.islower()` | provera da li se niska `s` sastoji od svih malih slova |
| `isupper` | `s.isupper()` | provera da li se niska `s` sastoji od svih velikih slova |
| `split` | `s.split()`, `s.split("and")` | podela niske `s` na podniske koristeći delimiter koji se navodi kao argument; ukoliko nije dat argument, podrazumevano se razdvaja po belinama |
| `rsplit` | `s.rsplit()`, `s.rsplit(maxsplit=2)` | slično kao `split`, ali se deli zdesna nalevo; nema razlike u odnosu na `split` ukoliko se ne navede argument `maxsplit` |
| `strip` | `s.strip()` | iz niske `s` se uklanjaju vodeće i prateće beline |
| `find` | `s.find("cat")` | u niski `s` se traži data podniska (`"cat"`); vraća se indeks prvog pojavljivanja te podniske (ili -1 ukoliko nema te podniske) |
| `rfind` | `s.rfind("dog")` | slično kao `find`, ali se traži zdesna nalevo (vraća se indeks poslednjeg pojavljivanja, gledano sleva) |
| `join` | `"/".join(['14', '03', '2026'])` | vrši se spajanje niski koje se prosleđuju kroz neku kolekciju kao argument funkcije; spajaju se po niski nad kojom se ovaj metod poziva |
| `startswith` | `s.startswith("Once upon a time")` | proverava se da li niska `s` počinje datom podniskom |
| `endswith` | `s.endswith("happily ever after.")` | proverava se da li se niska `s` završava datom podniskom |
| `replace` | `s.replace("sad", "happy")` | vrši se zamena prosleđene niske (`"sad"`) nekom drugom zadatom niskom (`"happy"`) u niski `s` |

## Modul `sys`, argumenti komandne linije

Modul `sys` je sistemska biblioteka koja omogućuje pristup sistemskim parametrima, funkcijama, promenljivama i slično.
Nama će biti posebno korisna za pristup argumentima komandne linije i za obradu grešaka u programu.

Kao i sa svakom bibliotekom, da bismo ovu biblioteku kositili, potrebno je da je uključimo:
```python
import sys
```

Argumenti komandne linije su skladišteni u listi `sys.argv`.
Ime skripta je skladišteno u `sys.argv[0]`, dok su ostali argumenti komandne linije `sys.argv[1]`, `sys.argv[2]` itd.

Ukoliko tokom programa zaključimo da je došlo do nekakve greške, koristićemo funkciju `sys.exit`, kojoj ćemo kao argument proslediti odgovarajući ne-nula izlazni status.
Izlazni status 0 koristimo kada program završavamo, a nije došlo ni do kakve greške.
Takođe, preko modula `sys` imamo pristup tokovima podataka:
- standardni ulaz `sys.stdin`;
- standardni izlaz `sys.stdout`;
- standardni izlaz za greške `sys.stderr` (nama posebno koristan ukoliko želimo da preusmerimo ispis u ovaj tok).

Prikažimo prethodno kroz primer.
Neka se očekuje da skript prima tačno dva argumenta komandne linije, pri čemu drugi predstavlja neki fajl.
```python
# Provera da je broj argumenata tacno dva.
if len(sys.argv) != 2:
    # Ispis ocekivanog poziva skripta; poruka se ispisuje na standardni izlaz za greske.
    print(f"Usage: {sys.argv[0]} <input_file>", file=sys.stderr)
    # Izlaz iz programa, uz status 1.
    sys.exit(1)
```

## Torke
Torke (eng. *tuples*) su tip podataka sličan listama.
Mogu skladištiti više podataka različitih tipova i imaju indeksni pristup elementima.

Primer pravljenja liste:
```python
t = (1, 2, "three", 4.0)
```

Od listi se razlikuju po tome što su torke imatuabilne, to jest, možemo pristupati njihovim elementima, ali ne i menjati ih.

U prethodnom primeru:
```python
print(t[0])         # moze
t[0] = 1            # ne moze!
```

## Rečnici

Rečnici (eng. *dictionaries*) predstavljaju sturkture podataka u Pajtonu u kojima su podaci organizovani u maniru "ključ -> vrednost".
Ključevi moraju biti hešabilni tipovi (to jest da mogu da se heširaju), što je često ekvivalentno sa tim da su imutabilni.
Na primer, liste ne mogu da budu ključevi rečnika, ali torke mogu.

Rečnik se pravi navođenjem parova ključ-vrednost, razdvojenih zarezom, između vitičastih zagrada `{` i `}`. Na primer:
```python
>>> grades = {
...     "Marko": 9,
...     "Milica": 10,
...     "Marija": 8
... }
```
```python
>>> grades
```
```
{'Marko': 9, 'Milica': 10, 'Marija': 8}
```

Vrednosti u rečniku se može pristupiti preko njenog ključa:
```python
>>> grades['Marija']
```
```
8
```

Rečnici su mutabilni, to jest, mogu im se menjati vrednosti:
```python
>>> grades['Marija'] += 1
>>> print(grades)
```
```
{'Marko': 9, 'Milica': 10, 'Marija': 9}
```
Ako pokušamo da postavimo neku vrednost za neki ključ koji prethodno nije postojao u rečniku, kreiraće se novi par ključ-vrednost:
```python
>>> grades['Mirko'] = 7
>>> print(grades)
```
```
{'Marko': 9, 'Milica': 10, 'Marija': 9, 'Mirko': 7}
```

Metodima `keys` i `values` možemo dobiti kolekciju ključeva i kolekciju vrednosti rečnika, redom, dok metodom `items` možemo dobiti kolekciju parova ključ-vrednost.
```python
>>> grades.keys()
```
```
dict_keys(['Marko', 'Milica', 'Marija', 'Mirko'])
```

```python
>>> grades.values()
```
```
dict_values([9, 10, 9, 7])
```

```python
>>> grades.items()
```
```
dict_items([('Marko', 9), ('Milica', 10), ('Marija', 9), ('Mirko', 7)])
```

Primetimo da kao povratne vrednosti dobijamo `dict_keys`, `dict_values` i `dict_items`; dakle, ne baš liste (kao što bismo možda očekivali).
Svakako, ovi tipovi podataka su iterabilni, što će nama biti važno i korisno.

Primer iteriranja po ključevima rečnika:
```python
>>> for key in grades.keys():
...     print(key)
...
```
```
Marko
Milica
Marija
Mirko
```

Primer iteriranja po vrednostima rečnika:
```python
>>> for value in grades.values():
...     print(value)
... 
```
```
9
10
9
7
```

Primer iteriranja po parovima ključ-vrednost rečnika:
```python
>>> for key, value in grades.items():
...     print(f"{key} ima ocenu {value}")
...
```
```
Marko ima ocenu 9
Milica ima ocenu 10
Marija ima ocenu 9
Mirko ima ocenu 7
```

Naglasimo još da je iteriranje po samom rečniku zapravo iteriranje po njegovim ključevima:
```python
>>> for x in grades:
...     print(x)
...
```
```
Marko
Milica
Marija
Mirko
```

## Skupovi

Skupovi se prave na sličan način kao rečnici, korišćenjem vitičastih zagrada, ali, za razliku od rečnika, navode se direktno vrednosti razdvojene zarezom, a ne parovi ključ-vrednost.

Primer:
```python
>>> A = {1, 2, 3, 4, 5}
>>> print(A)
```
```
{1, 2, 3, 4, 5}
```

Skupovi podržavaju naredne operacije:
| operator | primer | alternativno | značenje |
|---|---|---|---|
| `\|` | `A \| B` | `A.union(B)` | unija `A` i `B` |
| `&` | `A & B` | `A.intersection(B)` | presek `A` i `B` |
| `-` | `A - B` | `A.difference(B)` | razlika `A` i `B` |
| `^` | `A ^ B` | `A.symmetric_difference(B)` | simetrična razika `A` i `B` |

Mogu se porediti i narednim operatorima:
| operator | primer | značenje |
|---|---|---|
| `==` | `A == B` | `A` i `B` su jednaki |
| `<=` | `A <= B` | `A` je podskup od `B` |
| `<` | `A < B` | `A` je strogi podskup od `B` |
| `>=` | `A >= B` | `A` je nadskup od `B` |
| `>` | `A > B` | `A` je strogi nadskup od `B` |

## Komprehenzija kolekcija

Komprehenzije (eng. *comprehensions*) u Pajtonu predstavljaju sažet način konstrukcije struktura podataka na osnovu postojećih iterabilnih objekata.
Na ovaj način smo u stanju da elegantno primenimo operacije transformacije i filtriranja nad postojećim kolekcijama.

Prikažimo ovo kroz primere.

### Primer komprehenzije listi

Neka je data lista brojeva, u obliku niski:
```python
>>> number_strings = ["1", "1", "20", "-3", "4", "-1", "4", "4", "20"]
```
Da bismo dobili celobrojne vrednosti, umesto `for` petlje i "ručnog" punjenja liste:
```python
>>> numbers = []
>>> for s in number_strings:
...     numbers.append(int(s))
...
```
imamo mogućnost da uradimo sledeće:
```python
>>> numbers = [int(s) for s in number_strings]
>>> numbers
```
```python
[1, 1, 20, -3, 4, -1, 4, 4, 20]
```
Takođe, ukoliko želimo pozitivne vrednosti:
```python
>>> positive_numbers = [n for n in numbers if n > 0]
>>> positive_numbers
```
```python
[1, 1, 20, 4, 4, 4, 20]
```
(primetimo `if` u prethodnoj konstrukciji).

### Primer komprehenzije skupova

```python
>>> unique_numbers = {int(s) for s in number_strings}
>>> unique_numbers
```
```python
{1, 4, 20, -3, -1}
```

### Primer komprehenzije rečnika

```python
>>> grades_list = [("Marko", 9), ("Milica", 10), ("Marija", 8)]
>>> grades_list
```
```python
[('Marko', 9), ('Milica', 10), ('Marija', 8)]
```
```python
>>> grades_dict = {name: grade for name, grade in grades_list}
>>> grades_dict
```
```python
{'Marko': 9, 'Milica': 10, 'Marija': 8}
```

## Operatori `==` i `is`

Za kraj, navešćemo operatore `==` i `is`.
Ovi operatori porede na jednakost, ali postoji važna razlika.
Razlika između `==` i `is` je to što `==` poredi objekte po vrednosti, dok `is` poredi ispituje da li dve promenljive predstavljaju iste objekte u memoriji.

Primer:
```python
>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> l3 = l1
```
```python
>>> l2 is l1
```
```python
False
```
```python
>>> l2 == l1
```
```python
True
```
```python
>>> l3 is l1
```
```python
True
```
```python
>>> l3 == l1
```
```python
True
```
