#!/bin/bash

# Ekspanzijom viticastih zagrada dobijamo direktorijume examples_cpp i examples_python
mkdir -p examples_{cpp,python}

# Kombinacijom dva para viticastih zagrada dobijamo sve kombinacije fajlova:
# examples_cpp/test_example_01.txt,    examples_cpp/test_example_02.txt,    ..., examples_cpp/test_example_10.txt
# examples_python/test_example_01.txt, examples_python/test_example_02.txt, ..., examples_python/test_example_10.txt
touch examples_{cpp,python}/test_example_{01..10}.txt

