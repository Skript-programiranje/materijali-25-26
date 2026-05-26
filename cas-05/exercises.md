# Regularni izrazi - zadaci

Naredni zadaci mogu poslužiti za vežbanje regularnih izraza. Zadaci su u formatu "prepoznati ..." gde je "..." nekakav skup niski. Cilj je, dakle, smisliti regularni izraz koji opisuje tražene reči. Kako je neinteresantno dati `.*` kao rešenje koje će prepoznati maltene svaki zadati skup reči, zadatak je uvek dati regularni izraz koji prepoznaje *samo* tražene reči i, idealno, *ništa više*.

## Zadaci

1. Prepoznati sve trocifrene prirodne brojeve.
2. Prepoznati sve prirodne brojeve različite od 0.
3. Prepoznati sve prirodne brojeve uključujući i 0.
4. Prepoznati sve identifikatore u programskom jeziku C++.
5. Prepoznati aritmetičke operacije *+*, *-*, *\** i */* u programskom jeziku C++.
6. Prepoznati jednolinijske komentare u programskom jeziku C++.
7. Prepoznati literale (niske) u programskom jeziku C++, gde ih definišemo
kao teskt između dvostrukih nadovnika između kojih se mogu javiti proizvoljni
karakteri osim dvostrukih navodnika.
8. Prepoznati realne brojeve u programskom jeziku C++.
9. Prepoznati validne datume gde je datum u formatu *DD-MM-GGGG* ili *DD/MM/GGGG*.

## Rešenja

1. `[1-9][0-9]{2}`
2. `[1-9][0-9]*`
3. `0|[1-9][0-9]*`
4. `[_a-zA-Z][_a-zA-Z0-9]*`
5. `\+|-|\*|\/` ili `[+\-*\/]` ili `[-+*\/]` (znak `-` ne mora da se eskejpuje u
karakterskoj klasi ukoliko je na početku ili na kraju)
6. `\/\/.*`
7. `"[^"]*"`
8. `[+-]?(0|[1-9][0-9]*)(\.[0-9]*)?`
9. `\d{2}([-\/])\d{2}\1\d{4}`

