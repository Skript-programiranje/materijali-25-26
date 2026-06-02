# Peta nedelja vežbi

Ovaj čas je bio posvećen uvodu u regularne izraze.
Pomenute su osnove regularnih izraza i njihova podrška kroz
alat komandne linije `grep`.

## Regularni izrazi

Regularni izrazi (engl. *regular expressions*, skraćeno *regex*)
predstavljaju izraze za naprednu pretragu teksta.
Formalno, predstavljaju način opisivanja jedne vrste formalnih
jezika koji se zovu *regularni jezici* na način pogodan za računar.
Ipak, mi ćemo se fokusirati na praktične primene regularnih izraza
i posmatrati ih kao način za pretragu teksta.

*Napomena*: Iako regularni izrazi podsećaju na *globing*, to su
različiti koncepti i ne treba ih mešati, posebno što isti karakteri
mogu imati drugačije specijalno značenje u njima.

*Napomena*: Mnogi programi podržavaju regularne izraze i možete da
pokušate da isprobate ponašanje regularnih izraza na razne račine.
Jedan od njih, pogodan za početak, jeste sajt [regex101][web-regex101],
gde možete da zadate primer teksta u kome će se u realnom vremenu
označavati pokpanja za uneti regularni izraz.

### Operacije u regularnim izrazima

- Konkatenacija

    Regularne izraze ćemo posmatrati kao mehanizam napredne pretrage teksta.
    Kao takvi, mogu da izvršavaju i jednostavnu pretragu teksta doslovnim
    poklapanjem karaktera.
    Na primer, za prepoznavanje reči *program* u tekstu, može se koristiti
    regularni izraz `program`.
    Takvo formiranje regularnih izraza, tj. formiranje regularnih izraza
    nadovezivanjem karaktera, se naziva *konkatenacija*.

    Osim doslovnog poklapanja (koja predstavlja osnovu pretragu teksta),
    regularni izrazi podržavaju dodatne operatore koji povećavaju njihovu
    ekspresivnost.

- Alternacija: `|`

    Alternacija se koristi za uniranje različitih regularnih izraza i može
    tumačiti kao logičko *ili*.
    Na primer, regularni izraz `program|broj` prepoznaje pojavljivanja reči
    *program* i reči *broj*.

    *Napomena*: Alternacija ima niži prioritet u odnosu na konkatenaciju,
    zato regularni izraz `2025|6` prepoznaje reči *2025* i *6*, a ne reči
    *2025* i *2026*.
    Ukoliko bismo želeli drugo ponašanje, bilo bi neophodno izvršimo grupisanje
    i napišemo regularni izraz `202(5|6)`.

- Karakterske klase: `[]`

    Kraći zapis za alternaciju više karaktera se može ostvariti korišćenjem
    karakterskih klasa.
    Karakterske klase predstavljaju regularne izraze koji se zapisuju pomoću
    zagrada `[]`.
    Karakteri unutar zagrada će biti alternirani.
    Na primer, regularni izraz `[0123456789]` je ekvivalentan regularnom izrazu
    `0|1|2|3|4|5|6|7|8|9`, dok je regularni izraz `[ab2"]` ekvivalentat
    regularnom izrazu `a|b|2|"`.

    Ukoliko želimo da navedemo niz karaktera koji su susedni u ASCII tabeli,
    karakterske klase podržavaju navođenje raspona navodjenjem prvog i
    poslednjeg karaktera raspona i karaktera `-` između njih.
    Na primer, regularni izraz `[0-9]` prepoznaje cifre, dok regularni izraz
    `[a-zA-Z]` prepoznaje mala ili velika slova abecede.

    *Napomena*: Karakter `-` unutar karakterske klase se vezuje samo za susedne
    karaktere, odnosno, regularni izraz `[12-56]` ne prepoznaje sve brojeve od
    12 do 56, već samo cifre između 1 i 6.
    Naime, `-` će se odnositi na raspon `2-5`, pa će regularni izraz biti
    ekvivalentan regularnom izrazu `[123456]`.

    Karakterske klase dozvoljavaju listanje svih karaktera osim navedenih
    upotrebom simbola `^` unutar zagrada karakterske klase.
    Na primer, regularni izraz `[^a]` prepoznaje jedan karakter različit od *a*,
    dok regularni izraz `[^a-zA-Z]` prepoznaje jedan karakter koji nije ni malo
    ni veliko slovo engleske abecede (primetite da se negacija odnosi na sve
    simbole u zagradama).

    Specijalne karakterske klase:
    - `\d` je skraćenica za regularni izraz `[0-9]` (cifre)
    - `\w` je skraćenica za regularni izraz `[_a-zA-Z0-9]` (karakteri koji čine reči)
    - `\s` je skraćenica za regularni izraz `[ \n\t\f\v\r]` (beline)
    - `.` je skraćenica za sve karaktere koji ne razdvajaju redove, odnosno, možemo
    je posmatrati kao skraćenicu za regularni izraz `[^\n]`

    Slično, svaki od njih ima i negiranu verziju:
    - `\D` je skraćenica za regularni izraz `[^0-9]`
    - `\W` je skraćenica za regularni izraz `[^_a-zA-Z0-9]`
    - `\S` je skraćenica za regularni izraz `[^ \n\t\f\v\r]`

- Ponavljanje: `{}`

    Ponavaljanje regularnog izraza konačan broj puta se može opisati
    operatorom `{}`.
    Na primer, regularni izraz `[a-z]{4}` prepoznaje sve četvoroslovne reči
    napisane malim slovima engleske abecede.

    Operator `{}` može primiti i dva arugmenta, gde se oni tumače kao granice
    za broj ponavljanja.
    Na primer, regularni izraz `[A-Za-z]{2,5}` prepoznaje sve reči sastavljene
    od slova engleske abecede koje sadrže između 2 i 5 karaktera (granice su
    uključene).

    Ukoliko se ne navede leva granica, ona je podrazumevano 0.
    Na primer, regularni izraz `ba{,3}` prepoznaje reči *b*, *ba*, *baa* i
    *baaa*.

    Ukoliko se ne navede desna granica, ona je podrazumevano beskonačna,
    odnosno, nema gornjeg ograničenja po pitanju ponavljanja.
    Na primer, regularni izraz `[a-zA-Z]{1,}` prepoznaje sve reči sastavljene
    od malih ili velikih slova engleske abecede koje imaju barem jedan
    karakter.

    Specijalno:
    - ponavljanje 0 ili više puta (`{0,}`) se može zapisati operatorom `*`
    - ponavljanje 1 ili više puta (`{1,}`) se može zapisati operatorom `+`
    - ponavljanje 0 ili 1 puta (`{0,1}`) se može zapisati operatorom `?`

    Na primer:
    - regularni izraz `A[a-z]*` prepoznaje reči napisane engleskom abecedom
    koje počinju velikim slovom *A* (primetite da ovde spada i sama reč *A*)
    - regularni izraz `(ha)+` prepoznaje reči *ha*, *haha*, *hahaha*, itd.
    - regularni izraz `[+-]?3` prepoznaje reči *3*, *+3* i *-3*.

- Grupisanje: `()`

    Osim eksplicitnog zadavanja prioriteta, zagrade `()` u regularnim izrazima
    imaju i ulogu čuvanja poklapanja.
    Na primer, ukoliko želimo da prepoznamo reči formirane od ponavljanja jedne
    reči (kao što su *primerprimer*, *abcabc* ili *recrec*), potrebno je da
    u regularnom izrazu naglasimo da želimo da imamo ponavljanje iste reči, odnosno,
    potrebno je da pristupimo već poklopljenom početku reči.
    Regularni izraz `([a-z]+)\1` upravo to i radi.
    Zagradama okružuje regularni izraz za prepoznavanje reči `[a-z]+` čime se
    interno formira grupa koja se numeriše brojem 1, dok regularni izraz `\1`
    referiše na poklapanje u grupi 1.

    Grupa je bilo koji regularni izraz unutar zagrada `()` i numerišu se sleva
    nadesno prema redosledu otvaranja zagrada.
    Poklapanju unutar grupa se onda pristupa pomoću izraza `\1`, `\2`, itd. koji
    se nazivaju *backrefrence*.

- Sidra

    Sidra predstavljaju posebne karaktere koji služe za opisivanje mesta poklapanja.
    Neki od tih karaktera su:
    - `^` predstavlja početak reda
    - `$` predstavlja kraj reda
    - `\b` predstavlja granicu (početak ili kraj) reči

    Na primer:
    - regularni izraz `^program` prepoznaje samo one reči *program* kojima počinju
    redovi
    - regularni izraz `program$` prepoznaje samo one reči *program* kojima se
    završavaju redovi
    - regularni izraz `\bprogram` prepoznaje samo one reči *program* koje se nalaze
    na početku reči u tekstu (gde reči u tekstu definišemo kao celine razvdojene
    belinama, novim redovima i ostalim srodnim karakterima)
    - regularni izraz `program\b` prepoznaje samo one reči *program* kojima se
    završavaju reči u tekstu (gde reči u tekstu definišemo kao celine razvdojene
    belinama, novim redovima i ostalim srodnim karakterima)

[web-regex101]: https://regex101.com/
