heure_debut = int(input("Donnez l'heure de début de la location : "))
heure_fin = int(input("Donnez l'heure de fin de la location : "))

if heure_debut < 0 or heure_debut > 24 or heure_fin < 0 or heure_fin > 24:
    print("Les heures doivent être comprises entre 0 et 24 !\n")
elif heure_debut == heure_fin:
    print("Attention ! L'heure de fin est identique à l'heure de début.\n")
elif heure_debut > heure_fin:
    print("Attention ! Le début de la location est après la fin.\n")
else:
    duree_location = heure_fin - heure_debut

    if heure_debut >= 0 and heure_fin <= 7 or heure_debut >= 17 and heure_fin <= 24:
        tarif_horaire = 1.0
    else:
        tarif_horaire = 2.0

    print(f"Vous avez loué votre vélo pendant")
    print(f"{duree_location} heure(s) au tarif horaire de {tarif_horaire} euro(s)")

    montant_total = duree_location * tarif_horaire
    print(f"Le montant total à payer est de {montant_total} euro(s).")

