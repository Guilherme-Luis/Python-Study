#!/usr/bin/env python
"""
Imprime a tabuada do 1 ao 10.

Tabuada do 1
1
2
3
...
-----------------
Tabuada do 2
2
4
...
-----------------
"""
__version__ = "0.1.0"
__author__ = "Guilherme"

numeros = list(range(1, 11))

#iterable (percorriveis)
#para cada X(número) que está em `números`:
for X in numeros:
    print(f"Tabuada do: {X}")
    for Y in numeros:
        print(f"{X} X {Y}: {X * Y}")
    print("---------------------------")
