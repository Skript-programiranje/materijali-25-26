# Deseta nedelja vežbi

Ove nedelje upoznali smo se sa mehanizmima programskog jezika Pajton za čitanje fajlova i pisanje u fajlove.
Obradili smo modul `os` za interakciju sa operativnim sistemom, a sa ciljem obilaska i obrade fajlova i direktorijuma u fajl sistemu.
Takođe, upoznali smo se sa formatom JSON, formatom za čuvanje i transfer podataka, kao i Pajton modulom `json` za rad sa podacima u ovom formatu.

## Sortiranje u Pajtonu
Pre nego što se upustimo u glavne teme za ovu nedelju vežbi, pomenućemo mehanizme za sortiranje.

### Metod `sort`, funkcija `sorted`

Ranije smo pomenuli da metod `sort` klase `list` sortira listu u mestu.
Pored toga postoji i *funkcija* `sorted`, koja sortira kolekciju i vraća sortiranu kolekciju kao povratnu vrednost, pri čemu originalna kolekcija ostaje nepromenjena.

Prikažimo to na primeru.
Neka je data naredna lista:
```python
>>> people = ["marko", "ana", "milica"]
```
Primenom funkcije `sorted` dobijamo:
```python
>>> sorted(people)
```
```python
['ana', 'marko', 'milica']
```
pri čemu originalna lista ostaje nepromenjena:
```python
>>> people
```
```python
['marko', 'ana', 'milica']
```
S druge strane, poziv metoda `sort`:
```python
>>> people.sort()
```
ne vraća povratnu vrednost, ali menja originalnu listu, u mestu:
```python
>>> people
```
```python
['ana', 'marko', 'milica']
```

### Argument `reverse`
I metod `sort` i funkcija `sorted` podržavaju argument `reverse`.

Argument `reverse` je logička vrednost koja opisuje da li se sortiranje vrši u opadajućem redosledu ili ne.
Drugim rečima, ako vrednost ovog argumenta postavimo na `True`, soritraće se opadajuće, a ako je postavimo na `False`, soritraće se rastuće.
Podrazumevana vrednost ovog argumenta je `False`.

Primer:
```python
>>> people = ["marko", "ana", "milica"]
```
```python
>>> sorted(people, reverse=True)
```
```python
['milica', 'marko', 'ana']
```
```python
>>> sorted(people, reverse=False)
```
```python
['ana', 'marko', 'milica']
```
```python
>>> sorted(people)
```
```python
['ana', 'marko', 'milica']
```

### Argument `key`
Veoma koristan argument je argument `key`.
Kao i argument `reverse`, i ovaj argument je podržan i od strane funkcije `sorted` i od strane metoda `sort`.
Argumentom `key` se prima *ključ* po kome se sortira i očekuje se da ovaj ključ bude zadat u vidu funkcije.

Na primer, neka je data kolekcija:
```python
>>> people = ["marko", "anastasija", "mile"]
```
"Obično" sortiranje daje:
```python
>>> sorted(people)
```
```python
['anastasija', 'marko', 'mile']
```
S druge strane, možemo sortirati po dužini niske, prosleđivanjem funkcije `len` kao ključ:
```python
>>> sorted(people, key=len)
```
```python
['mile', 'marko', 'anastasija']
```

Nama će uglavnom biti od koristi da prosleđujemo kompleksnije funkcije kao ključeve za sortiranje.
To postižemo *lambda funkcijama*.

Opišimo ovo kroz primer.
Neka je data lista parova:
```python
>>> ages = [
...     ("marko", 23),
...     ("ana", 21),
...     ("marko", 20),
...     ("milica", 22)
... ]
```
"Obično" sortiranje:
```python
>>> sorted(ages)
```
će sortirati leksikografski, to jest, prvo po prvoj koordinati, pa onda po drugoj:
```python
[('ana', 21), ('marko', 20), ('marko', 23), ('milica', 22)]
```
Ukoliko ne želimo da uopšte sortiramo po imenima, već samo da sortiramo po broju godina:
```python
>>> sorted(ages, key=lambda p: p[1])
```
Ovim dobijamo:
```python
[('marko', 20), ('ana', 21), ('milica', 22), ('marko', 23)]
```
Ovde smo koristili `lambda p: p[1]` - ključna reč `lambda` označava da je u pitanju lambda funkcija, a ono što za tom rečju sledi je opis same funkcije.
U ovom primeru, funkcija šalje argument `p` (što mi znamo da će biti jedan uređeni par u listi) u vrednost `p[1]` (to jest, drugu koordinatu tog uređenog para).

### Sortiranje ostalih kolekcija
Najčešće ćemo sortirati liste, i njihovo sortiranje daje kao rezultat, naravno, listu, ali se mogu sortirati i torke, rečnici i skupovi, pri čemu su rezultati sortiranja u tom slučaju liste.

## Čitanje fajlova i pisanje u fajlove u Pajtonu

Fajl se može otvoriti pozivom funkcije `open`.
Kao prvi argument prosleđujemo putanju do fajla koji otvaramo (putanja može biti relativna ili apsolutna), a kao drugi argument režim u kojem ga otvaramo: `"r"` (eng. *read*) je za čitanje, dok je `"w"` (eng. *write*) za pisanje.

Primer poziva funkcije `open`:
```python
>>> file = open("/home/student/Desktop/example.txt", "r")
```
Funkcijom `read` dobijamo sadržaj čitavog fajla, u vidu jedne niske:
```python
>>> contents = file.read()
```
```python
>>> contents
```
```python
'This is an example file.\nThese contents serve as an example\nof reading files in Python.\n'
```
```python
>>> print(contents)
```
```
This is an example file.
These contents serve as an example
of reading files in Python.

```

Takođe, možemo sadržaj možemo pročitati i kao skup linija, koristeći funkciju `readlines`.
Ova funkcija čita sadržaj fajla i upisuje linije u listu.
Imati u vidu da je svaka linije terminirana oznakom `\n` za novi red.
```python
>>> file = open("/home/student/Desktop/example.txt", "r")
```
```python
>>> lines = file.readlines()
```
```python
>>> lines
```
```python
['This is an example file.\n', 'These contents serve as an example\n', 'of reading files in Python.\n']
```

Preporučeno je čitati fajlove uz naredbu `with`:
```python
>>> with open("example.txt", "r") as file:
...     content = file.read()
...     # obrada sadrzaja fajla...
...
```
Na ovaj način, pravi se poseban kontekst u kome fajl biva zatvoren bilo da se desila greška prilikom njegovog otvaranja ili nije.

Ipak, ovim pristupom ne obrađujemo eventualnu grešku ukoliko se ona ukaže.
Da bismo to uradili, možemo koristiti koncept hvatanja izuzetaka (nalik na način na koji se to radi u programskom jeziku Java):
```python
import sys

try:
    with open("fajl.txt", "r") as file:
        contents = file.read()
        # obrada sadrzaja fajla...
except IOError:
    print("Greska pri otvaranju fajla!")
    sys.exit(1)
```
Ovaj pristup bi trebalo koristiti kad god otvaramo i koristimo fajlove.

Pisanje u fajlove je vrlo slično.
Tu nam je korisna funkcija `write`.
```python
>>> try:
...     with open("some_file.txt", "w") as file:
...         file.write("Hello!\n")
...         file.write("This line doesn't erase the previous one.\n")
...         file.write("All three of these lines will be written to the file.\n")
... except IOError:
...     print("Greska prilikom otvaranja fajla.")
...     sys.exit(1)
...
```
Primetimo da, ukoliko ovo uradimo u Pajton interpreteru, dobijamo sledeći ispis:
```python
7
42
54
```
To je zato što funkcija `write` vraća broj upisanih karaktera.
Svakako, ovaj ispis ne bi bio vidljiv prilikom poziva is skripta.

U prethodnom primeru, linije koje su upisivane u fajl nisu se prepisivale jedna preko druge.
S druge strane, prethodni sadržaj fajla "some_file.txt" jeste prepisan, jer je mod za korišćenje fajla bio zadat sa `"w"`.
Ukoliko želimo da *dopisujemo*, a ne da prepisujemo postojeći sadržaj fajla, koristićemo mod `"a"` (eng. *append*).

## Modul `os`

Modul `os` je koristan modul za upravljanje operativnim sistemom.
Nama će biti koristan pri obilasku fajl sistema i baratanju putanjama.

Funkcije koje smo obradili na času:
- `os.path.isdir` - proverava da li je prosleđeni argument direktorijum;
- `os.path.isfile` - proverava da li je prosleđeni argument regularni fajl;
- `os.path.join` - spaja prosleđene niske separatorom koji se koristi na matičnom sistemu (na primer, `/` za Linux, `\` za Windows);
- `os.listdir` - izlistava sadržaj direktorijuma koji se prosleđuje kao argument (vraća listu imena fajlova u direktorijumu);
- `os.walk` - pravi rekurzivnu "šetnju" po direktorijumu koji se prosleđuje kao argument.

Funkcija `os.walk` rekurzivno prolazi kroz dati direktorijum.
Ova funkcija je generator; omogućava da se svakim prolazom petljom `for` izdvaja se trojka `(dirpath, dirnames, filenames)`, gde je:
- `dirpath` (niska): putanja do tekućeg direktorijuma.
- `dirnames` (lista): imena svih poddirektorijuma tekućeg direktorijuma.
- `filenames` (lista): imena svih "ne-direktorijum" fajlova u tekućem direktorijumu.

```python
>>> import os
```
```python
>>> for dirpath, dirnames, filenames in os.walk('.'):
...     print(f"Tekuca putanja: {dirpath}")
...     print(f"Poddirektorijumi: {dirnames}")
...     print(f"Ostali fajlovi: {filenames}")
... 
```

## Format JSON, modul `json`

Format JSON (eng. *JavaScript object notation*) je portabilni format za čuvanje podataka.
Podaci u ovom formatu se čuvaju tekstualno, u vidu lista i rečnika, sasvim nalik na način na koji se zadaju liste i rečnici u Pajtonu.

Primer podataka u formatu JSON (fajl `example.json`):
```json
{
  "name": "Marko Markovic",
  "age": 28,
  "skills": ["Python", "JSON"],
  "address": {
    "city": "Belgrade",
    "country": "Serbia"
  }
}
```

Za lako baratanje podacima u formatu JSON, koristićemo modul `json` u Pajtonu.
```python
>>> import json
```

Čitanje sadržaja u formatu JSON se postiže funkcijom `json.load`:
```python
>>> import json
>>> with open("example.json", "r") as file:
...     json_contents = json.load(file)
...     print(json_contents)
...
```
```python
{'name': 'Marko Markovic', 'age': 28, 'skills': ['Python', 'JSON', 'JavaScript'], 'address': {'city': 'Belgrade', 'country': 'Serbia'}}
```

S druge strane, korisno nam je i da sadržaje u Pajtonu skladištimo u fajlu u formatu JSON.
To postižemo funkcijom `json.dump`:
```python
>>> import json
>>> 
>>> student_info = {
...     "name": "Marko Markovic",
...     "age": 28,
...     "graduated": True,
...     "skills": ["Python", "JSON"],
...     "address": {
...         "city": "Belgrade",
...         "country": "Serbia"
...     }
... }
>>> 
>>> with open("student.json", "w") as file:
...     json.dump(student_info, file)
... 
```
```bash
$ cat student.json
```
```
{"name": "Marko Markovic", "age": 28, "graduated": true, "skills": ["Python", "JSON"], "address": {"city": "Belgrade", "country": "Serbia"}}
```
Veće količine podataka postaju nepregledne na ovaj način.
Da bismo popravili čitljivost, često dodajemo vrednost argumenta `indent`.
Na primer, upišimo sadržaj sa indentacijom 4:
```python
>>> with open("student.json", "w") as file:
...     json.dump(student_info, file, indent=4)
...
```
```bash
$ cat student.json
```
```
{
    "name": "Marko Markovic",
    "age": 28,
    "graduated": true,
    "skills": [
        "Python",
        "JSON"
    ],
    "address": {
        "city": "Belgrade",
        "country": "Serbia"
    }
}
```
