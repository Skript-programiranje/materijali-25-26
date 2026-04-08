## Команда `ls`

Листање директоријума може се урадити командом `ls`. Команда `ls` приказује садржај текућег директоријума: фајлове, директоријуме и све остало. Изузетак су, рецимо, скривени фајлови, чија имена почињу тачком (на пример, текући директоријум `.` и родитељски директоријум `..`). Уколико желимо да видимо скривене фајлове, можемо навести опцију `-a`:

```bash
$ ls -a
...
```

Такође корисна опција је `-l` за испис у дугом формату (енг. *long format*).

```bash
$ ls -l
...
```

`ll` је често алијас за команду `ls` са опцијама `-a`, `-l`, `-F`.

```bash
$ ll
...
```

Алијас је, као што име каже, друго име за неку команду (обично са неким специфичним опцијама). Ако желимо да видимо постављене алијасе, можемо то урадити командом `alias`:

```bash
$ alias
...
```

Специфично можемо да видимо шта представља неки конкретан алијас путем `alias [naziv_alijasa]`, на пример:

```bash
$ alias ll
alias ll='ls -l'
```

Такође, инфомацију о типу команде или алијаса можемо добити командом `type`:

```bash
$ type ll
ll is aliased to `ls -l'
$ type cat
cat is /usr/bin/cat
```

---

## Прављење и брисање фајлова и директоријума

Фајл се може направити командом `touch`:

```bash
$ touch file.txt
$ ls
file.txt
```

Фајлове можемо обрисати командом `rm`:

```bash
$ ls
file.txt another.txt
$ rm file.txt
$ ls
another.txt
```

Команду `rm` треба користити *веома* пажљиво, јер је брисање које она врши неоповратно!

Уколико желимо да направимо директоријум, то можемо урадити командом `mkdir`:

```bash
$ ls
01_prvi.txt 02_drugi.txt
$ mkdir zadaci
$ ls
01_prvi.txt 02_drugi.txt zadaci
```

Командом `rmdir` можемо обрисати празне директоријуме.

```bash
$ ls
01_prvi.txt 02_drugi.txt zadaci
$ rmdir zadaci
$ ls
01_prvi.txt 02_drugi.txt
```

Фајл можемо копирати командом `cp`.

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

Командом `mv` можемо померити или преименовати фајл. Основни облик коришћења ове команде је `mv <source> <destination>`. Уколико `source` и `destination` имају исти родитељски директоријум, онда се врши преименовање `source` у `destination`. У супротном се `source` помера у родитељски директоријум фајла `destination`.

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

## Кретање кроз фајл систем

Тренутни радни директоријум може се видети командом `pwd`.

```bash
$ pwd
/home/sp/
```

Тренутни радни директоријум се може променити командом `cd`.

```bash
$ ls
predavanja vezbe
$ cd vezbe
$ pwd
/home/sp/vezbe
```

Уколико имамо потребу да се често пребацујемо између више директоријума, корисне су команде `pushd` и `popd`.

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

## Измене дозвола над фајловима

```bash
$ ls -l
-rw-r-x-w- 1 sp sp   146 Mar 18 09:50 1.sh
```

Прва колона се састоји од 10 карактера и носи информације о дозволама.

| Тип | Власник | Група | Остали |
|-----|--------|-------|--------|
| `-` | `rw-`  | `r-x` | `-w-`  |

Карактер `r` означава читање, `w` писање, `x` извршавање, а `-` недостатак дозволе.

### Текстуални начин

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

### Нумерички начин

`rwxr--rw-` → `111100110` → `745`

```bash
$ chmod 745 1.sh
$ ls -l
-rwxr--rw- 1 sp sp   146 Mar 18 09:50 1.sh
```

---

## Променљиве окружења

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

## Покретање скрипти

Једна од главних предности интеракције са рачунаром помоћу командне линије јесте
аутоматизација помоћу шел (shell) скрипти.
Команде се могу написати у текстуалном фајлу, а тај фајл се затим може дати шелу
да га изврши.

На пример, ако направимо фајл `zdravo.sh` са следећим садржајем:
```bash
echo "Zdravo, svete!"
```

Можемо да је покренемо на следећи начин:
```bash
$ bash zdravo.sh
Zdravo, svete!
```

Други, чешћи, начин је да скрипте покрећемо тако што:
1. скрипти доделимо право извршавања:
```bash
$ chmod +x zdravo.sh
```
2. покренемо скрипту као извршиви фајл:
```bash
$ ./zdravo.sh
Zdravo, svete!
```

Међутим, да бисмо то радили, потребно је да у скрипти задамо који програм треба
да је извршава.
У овом случају, то ће бити `bash`, па је потребно да то додамо.
То се ради тако што се на почетку скрипте постави линија која почиње `#!` (енгл.
*shebang*) коју прати путања до програма.

На пример, ако команда `which bash` враћа `/usr/bin/bash`, онда се скрипта може
изменити на следећи начин:
```bash
#!/usr/bin/bash

echo "Zdravo, svete!"
```
