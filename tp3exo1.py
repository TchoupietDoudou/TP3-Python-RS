# Exercice a) 
sum_result = 0

for i in range(N + 1):
    sum_result += i

print("La somme des N entiers naturels de 0 à", N, "est :", sum_result)

# Exercice b) 
value = 0

while value != 100:
    value = int(input("Entrez une valeur pour l'exercice b) (entrez 100 pour terminer) : "))

print("La boucle d'attente se termine.")

# Exercice c) 
count_less_than_10 = 0
count_10_to_15 = 0
count_greater_than_15 = 0

for _ in range(10):
    valeur = float(input("Entrez une valeur réelle entre 0 et 20 pour l'exercice c) : "))
    
    while valeur < 0 or valeur > 20:
        valeur = float(input("La valeur doit être entre 0 et 20. Réessayez : "))
    
    if valeur < 10:
        count_less_than_10 += 1
    elif 10 <= valeur < 15:
        count_10_to_15 += 1
    else:
        count_greater_than_15 += 1

print("Nombre de valeurs inférieures à 10 :", count_less_than_10)
print("Nombre de valeurs entre 10 et 15 :", count_10_to_15)
print("Nombre de valeurs supérieures ou égales à 15 :", count_greater_than_15)

# Exercice d) 
X = float(input("Entrez une valeur X (supérieure à 1) pour l'exercice d) : "))
N = 0
sum_result = 0

while sum_result <= X:
    N += 1
    sum_result += N

print("Le plus grand nombre N tel que la somme des entiers de 0 à N est inférieure ou égale à", X, "est :", N - 1)

