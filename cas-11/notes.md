# Jedanaesta nedelja vežbi

Ranije tokom kursa smo se upoznali sa regularnim izrazima.
Ove nedelje smo upoznali Pajton modul `re` za rad sa regularnim izrazima.

## Modul `re`

Modul `re` (skraćeno od engleskog *regular expressions*) sadrži puno funkcija koje su nam korisne za rad sa regularnim izrazima.
Funkcije iz ovog modula služe za prepoznavanje niski koje odgovaraju šablonima zadatim regularnim izrazima.
Da bismo imali pristup ovim funkcijama, kao i do sada, moramo uključiti ovaj modul:
```python
>>> import re
```

### Pregled funkcija

Funkcije koje smo obradili na času date su u narednoj tabeli.
| funkcija | ponašanje |
|--|--|
| `re.search` | ispituje da li data niska sadrži podnisku koja se poklapa sa datim šablonom |
| `re.match` | ispituje da li data niska počinje podniskom koja se poklapa sa datim šablonom |
| `re.fullmatch` | ispituje da li se data niska *u celosti* poklapa sa datim šablonom |
| `re.findall` | pronalazi sva poklapanja šablona u datoj niski; povratna vrednost je lista pronađenih niski |
| `re.finditer` | slično kao `re.findall`, samo što je povratna vrednost iterabilni objekat koji sadrži poklapanja u vidu `Match` objekata |
| `re.split` | razdvaja datu nisku na podniske, pri čemu se za delimiter koristi svako poklapanje datog šablona |
| `re.sub` | u datoj niski menja svako pojavljivanje podniske koja odgovara datom šablonu, datom niskom |
| `re.compile` | unapred priprema regularni izraz i kompilira ga u objekat nad kojim se mogu pozivati metodi `search`, `match` itd. |

Kao i do sada, ako nam treba pomoć oko bilo koje od ovih funkcija, zovemo funkciju `help`:
```python
>>> help(re.search)
```

### Sirove niske

Prilikom rada sa regularnim izrazima, biće nam korisne *sirove niske* (eng. *raw strings*) u Pajtonu.
Ove niske se zadaju navođenjem slova `r` ili `R` ispred niske.
Na primer, `r"ovo je sirova niska"`.
Kod ovih niski, karakter `\` se ne tretira kao poseban karakter za escape-ovanje, već kao bukvalan karakter "obrnuta kosa crta".
Na primer, u (običnoj) niski `"hello\neveryone"`, sekvenca `\n` se tretira kao karakter za novi red (eng. *newline*).
S druge strane, u sirovoj niski `r"hello\neveryone"`, sekvenca `\n` se tretira bukvalno; kao karakter `\` i karakter `n`.
```python
>>> print("hello\neveryone")
```
```
hello
everyone
```
```python
>>> print(r"hello\neveryone")
```
```
hello\neveryone
```
Ove niske ćemo koristiti maltene uvek kada budemo radili sa regularnim izrazima.

## `Match` i `None` na primeru funkcije `re.search`

Funkcija `re.search` traži poklapanje prosleđenog šablona u datoj niski.
Ukoliko je šablon poklopljen, `re.search` kao povratnu vrednost daje objekte tipa `Match`.
Ukoliko šablon nije poklopljen, dobijamo `None` objekat.

```python
>>> x = re.search(r"\d+", "This string contains some numbers: 15, 32, and 11.")
```
```python
>>> type(x)
```
```python
<class 're.Match'>
```
```python
>>> x
<re.Match object; span=(35, 37), match='15'>
```
U ovom primeru, vidimo da je dobijeni objekat `x` objekat klase `Match`.
Dodatno, imamo i informaciju o tome da je poklapanje od 35. karaktera (uključujući ga) do 37. karaktera (ne uključujući ga), kao i da je poklapanje niska `'15'`.

Biće nam vrlo korisno da budemo u stanju da iz objekta tipa `Match` izdvojimo samu nisku koja je poklopljena.
To radimo metodom `group`:
```python
>>> x.group()
```
```
'15'
```

Kao što je pomenuto iznad, ukoliko pri pozivu funkcije `re.search` ne dobijemo poklapanje, dobijamo `None` objekat.
```python
>>> x = re.search(r"\d+", "This string does NOT contains any numbers. :(")
```
```python
>>> type(x)
```
```python
<class 'NoneType'>
```

Zato, ispitivanje da li je do poklapanja došlo ili ne, možemo proveriti ispitivanjem da li je povratna vrednost bila `None`.
```python
>>> x = re.search(r"cats", "dogs, dogs, happy dogs!")
>>> if x is None: 
...     print("Nema poklapanja.")
... else:
...     print(f"Poklapanje: {x.group()}")
...
```
```
Nema poklapanja.
```

## Metodi `re.match` i `re.fullmatch`

Veoma slični metodu `re.search` su metodi `re.match` i `re.fullmatch`.
Razlika je u tome što metod `re.match` ispituje da li se dati šablon poklapa *na početku* niske (a ne bilo gde u njoj), dok metod `re.fullmatch` ispituje da li se *čitava* niska poklapa sa datim šablonom.
Možemo primetiti jednu kul stvar, a to je da se funkcije `re.match` i `re.fullmatch` mogu implementirati preko `re.search`, koristeći sidra.
Naime,
```python
re.match(pattern, string)
```
je ekvivalentno sa
```python
re.search(r"^" + pattern, string)
```
dok je
```python
re.fullmatch(pattern, string)
```
ekvivalentno sa
```python
re.search(r"^" + pattern + r"$", string)
```

## Još o metodu `group`

Kad god imamo `Match` objekat dobijen poklapanjem regularnog izraza koji ima više grupa, metodu `group` možemo proslediti broj da bismo dobili poklopljenu vrednost neke konkretne grupe.
Na primer:
```python
>>> match = re.search(r"(\d{2})\.(\d{2})\.(\d{4})", "This is a date: 26.06.2026 :)")
```
```python
>>> match.group()
```
```python
'26.06.2026'
```
Podrazumevano, poziv funkcije `group` bez argumenata je ekvivalentan pozivu funkcije `group` sa argumentom `0` (odnosno, izdvajanju čitave poklopljene niske).
```python
>>> match.group(0)
```
```python
'26.06.2026'
```
Izdvajanje prve grupe (u ovom primeru, to je dan u mesecu) radimo pozivom funkcije `group` sa argumentom 1:
```python
>>> match.group(1)
```
```python
'26'
```
Izdvajanje druge grupe (u ovom primeru, to je mesec):
```python
>>> match.group(2)
```
```python
'06'
```
Izdvajanje treće grupe (u ovom primeru, to je godina):
```python
>>> match.group(3)
```
```python
'2026'
```

Kada imamo više grupa, postaje nezgodno pratiti koja grupa je identifikovana kojim brojem, posebno kada regularni izraz modifikujemo tokom rada.
Srećom, podržane su *imenovane grupe* (eng. *named groups*), koje dopuštaju da grupama damo ime, a potom da ih tim imenom oslovljavamo (umesto brojevima).
Pokažimo to na prethodnom primeru:
```python
>>> match = re.search(r"(?P<day>\d{2})\.(?P<month>\d{2})\.(?P<year>\d{4})", "This is a date: 26.06.2026 :)")
```
```python
>>> match.group("day")
```
```python
'26'
```
```python
>>> match.group("month")
```
```python
'06'
```
```python
>>> match.group("year")
```
```python
'2026'
```
```python
>>> match.group("time")
```
```python
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: no such group
```

Na ovaj način postaje lakše raditi sa bek referencama:
```python
match = re.search(r"(?P<day>\d{2})(?P<sep>\.)(?P<month>\d{2})(?P=sep)(?P<year>\d{4})", "This is a date: 26.06.2026 :)")
```

## Funkcije `re.findall` i `re.finditer`

Za razliku od funkcija `re.search`, `re.match` i `re.fullmatch`, koje proveravaju poklapanje šablona "jednom", ukoliko želimo da pronađemo sva poklapanja datog šablona u datoj niski, koristićemo funkcije `re.findall` i `re.finditer`.
Funkcija `re.findall` vraća listu svih poklopljenih *niski* (dakle, ne `Match` objekata).
Funkcija `re.finditer` vraća iterabilni objekat.
Po ovom objektu se može iterirati `for` petlja, a stavke su `Match` objekti.

Primer rada funkcije `re.findall`:
```python
>>> re.findall(r"[A-Z][a-z]+", "here are some names: Marija, Ana, and Marko")
```
```python
['Marija', 'Ana', 'Marko']
```

Primer rada funkcije `re.finditer`:
```python
>>> for match in re.finditer(r"[A-Z][a-z]+", "here are some names: Marija, Ana, and Marko"):
...     print(match.group())
...
```
```
Marija
Ana
Marko
```

## Zastavice modula `re`

Većina funkcija modula `re` podržava argument `flags`.
Ovom argumentu se može proslediti kombinacija *zastavica* (eng. *flags*) modula `re`.
Ove zastavice predstavljaju posebne konstante koje funkciji daju dodatnu informaciju o tome kako treba da primenjuje regularni izraz pri traženju poklapanja šablona.
Na primer, na času smo obradili:
- `re.IGNORECASE` - zastavica kaže da ne treba praviti razliku između velikih i malih slova;
- `re.DOTALL` - podrazumevano, tačka (`.`) se koristi bilo kog karaktera *osim* novog reda (`\n`); ovom zastavicom se i novi red uključuje u skup karaktera koje tačka označava.

S druge strane, postoje i razne druge zastavice, čiji spisak se može pronaći u opisu modula `re`:
```python
>>> help(re)
```
Na primer, ukoliko želimo da prepoznamo šablon `pattern` u tekstu `text`, korišćenjem zastavica `re.IGNORECASE` i `re.DOTALL`:
```python
>>> re.search(pattern, text, re.IGNORECASE | re.DOTALL)
```
Primetiti bitovsku disjunkciju `|` koja je korišćena za kombinovanje zastavica.

## Funkcija `re.sub`

Funkciji `re.sub` se prosleđuje šablon u vidu regularnog izraza i tekst kojim treba zameniti taj šablon u datoj niski.
Rezultat poziva funkcije je niska u kojoj su sva poklapanja šablona zamenjena datom niskom.

Na primer,
```python
>>> re.sub(r"[A-Z][a-z]+", "[REDACTED]", "our employees are: Marija, Ana, and Marko")
```
```python
'our employees are: [REDACTED], [REDACTED], and [REDACTED]'
```

## Funkcija `re.split`

Funkcija `re.split` radi na sličan način kao funkcija `split` koju smo pominjali ranijih časova.
Razlika je u tome što se kod funkcije `re.split` niska koja predstavlja razdvajač (eng. *delimiter*) može zadati kao regularni izraz.
Na primer:
```python
>>> re.split(r'\s+and\s+', "alpha AND  beta  and gamma AND  delta", flags=re.IGNORECASE)
```
```python
['alpha', 'beta', 'gamma', 'delta']
```

## Dodatno: funkcija `re.compile`

Kada se funkcija za rad sa regularnim izrazima poziva, ona mora da procesuira prosleđeni regularni izraz i napravi unutrašnju reprezentaciju tog izraza.
Kada se provera poklapanja jednog istog šablona vrši mnogo puta, postaje neefikasno svaki put praviti tu unutrašnju reprezentaciju.

Funkcija `re.compile` omogućuje da se regularni izraz procesuira samo jednom, a da se kasnije provere poklapanja niski sa tim šablonom vrše brže.

```python
>>> book_lines = [
...     "In the little office at the back of Mr McKechnie's bookshop,",
...     "Gordon--Gordon Comstock, last member of the Comstock family,",
...     "aged twenty-nine and rather moth-eaten already--lounged across the table,",
...     "pushing a four-penny packet of Player's Weights open and shut with his thumb."
... ]
```

```python
>>> capitalized_word = re.compile(r"\b[A-Z][a-z]*\b")
```
```python
>>> i = 1
>>> for line in book_lines:
...     matches = capitalized_word.findall(line)
...     print(f"Reci sa velikim pocetnim slovom u redu {i}: {matches}")
...     i += 1
... 
```
``` 
Reci sa velikim pocetnim slovom u redu 1: ['In', 'Mr']
Reci sa velikim pocetnim slovom u redu 2: ['Gordon', 'Gordon', 'Comstock', 'Comstock']
Reci sa velikim pocetnim slovom u redu 3: []
Reci sa velikim pocetnim slovom u redu 4: ['Player', 'Weights']
```

Više o mehanizmima na kojima počivaju pomenute unutrašnje reprezentacije ovih funkcija, to jest o tzv. *konačnim automatima*, imaćete priliku da vidite na kursu Prevođenje programskih jezika.
