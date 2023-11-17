def factorielle_for(n):
    resultat = 1
    for i in range(1, n + 1):
        resultat *= i
        print(f"Étape {i}: {resultat}")
    return resultat

def factorielle_while(n):
    resultat = 1
    i = 1
    while i <= n:
        resultat *= i
        print(f"Étape {i}: {resultat}")
        i += 1
    return resultat

n = int(input("Entrez un entier n pour calculer sa factorielle : "))
choix_boucle = input("Choisissez la boucle (1 pour for, 2 pour while) : ")

if choix_boucle == '1':
    resultat_factorielle = factorielle_for(n)
elif choix_boucle == '2':
    resultat_factorielle = factorielle_while(n)
else:
    print("Choix non valide. Veuillez choisir 1 pour for ou 2 pour while.")

print(f"La factorielle de {n} est : {resultat_factorielle}")
