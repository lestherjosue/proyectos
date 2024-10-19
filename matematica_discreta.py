import math
from itertools import permutations, combinations, combinations_with_replacement

def permutaciones_sin_repeticion(n, r):
    return math.factorial(n) // math.factorial(n - r)

def permutaciones_con_repeticion(n, r):
    return n ** r

def combinaciones_sin_repeticion(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

def combinaciones_con_repeticion(n, r):
    return math.factorial(n + r - 1) // (math.factorial(r) * math.factorial(n - 1))

# Ejemplos de uso
n = 3  # Número total de elementos
r = 2  # Número de elementos a elegir

print(f"Permutaciones sin repetición (P({n}, {r})): {permutaciones_sin_repeticion(n, r)}")
print(f"Permutaciones con repetición (P({n}, {r})): {permutaciones_con_repeticion(n, r)}")
print(f"Combinaciones sin repetición (C({n}, {r})): {combinaciones_sin_repeticion(n, r)}")
print(f"Combinaciones con repetición (C({n}, {r})): {combinaciones_con_repeticion(n, r)}")

# Ejemplos con elementos específicos
elementos = ['A', 'B', 'C']

# Permutaciones de elementos
print("\nPermutaciones de elementos (sin repetición):")
for p in permutations(elementos, r):
    print(p)

# Combinaciones de elementos
print("\nCombinaciones de elementos (sin repetición):")
for c in combinations(elementos, r):
    print(c)

# Combinaciones de elementos (con repetición)
print("\nCombinaciones de elementos (con repetición):")
for cr in combinations_with_replacement(elementos, r):
    print(cr)