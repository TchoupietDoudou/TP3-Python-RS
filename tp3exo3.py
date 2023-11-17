import random

nombre_mystere = random.randint(0, 100)
compteur_tours = 0

while True:
    guess = int(input("Devinez le nombre entre 0 et 100 : "))
    compteur_tours += 1
    
    if guess < nombre_mystere:
        print("Le nombre mystère est plus grand.")
    elif guess > nombre_mystere:
        print("Le nombre mystère est plus petit.")
    else:
        print(f"Vous avez trouvé le nombre mystère en {compteur_tours} tentatives.")
        break

