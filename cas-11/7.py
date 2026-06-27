#!/usr/bin/python

# Zadatak: Zameniti pojavljivanje mejlova u tekstu recju [EMAIL].

import re

text = """
User john.doe@example.com logged in.
User alice@test.org logged out.
"""

# Za zamenu koriscenjem sablona zadatog regularnim izrazom, koristimo funkciju re.sub.
anonimno = re.sub(r"[\w.]+@[\w.]+", "[EMAIL]", text)

print(anonimno)
