def calcul_reduction( prix , etudiant, fidelite,code):
    reduction=0.0
    if statut == 1:
      reduction += prix_initial * 0.10  # 10 %

    if fidelite >= 5:
      reduction += prix_initial * 0.15  # 15 %

    if prix_initial > 100:
      reduction += 5.0  # réduction fixe supplémentaire
    if code =="oui" :
     code_promo=input("saisir le code promo :").strip().upper()
     if code_promo == "PROMO10" :
          reduction +=prix_initial * 0.10

    return reduction




while True :
    print("1. Calculer une réduction")
    print("2. Afficher les règles")
    print("3. Quitter")

    choix = int (input("Votre choix : ").strip())
    if choix == 1:
       try:
         prix_initial = float(input("Prix du produit (€) : "))
       except ValueError:
        print("Saisie invalide pour le prix.")
        exit(1)
       statut= int(input("Êtes-vous étudiant ?(1-pour oui / 0-pour no) : ").strip().lower())
       fidelite = int(input("Fidélité (en années) : ").strip())
       code=input("avez-vous un code pomo (oui/no) : "). strip().lower()
       reduction=calcul_reduction(prix_initial,statut , fidelite,code)
       prix_final = prix_initial - reduction
       print (f" prix initial : {prix_initial:.2f}")

       print(f"Réduction totale : {reduction:.2f} €")
       print(f"Prix final : {prix_final:.2f} €")
       if prix_final < 0:
         
         prix_final = 0.0  # garde-fou
         print(f" prix initial : {prix_initial :.2f}")
         print(f" reduction totale : {reduction : .2f} ")
         print(f" prix final : {prix_final : .2f}")
    elif choix == 2:
       print ("regle de reduction :")
       print ("1. 10% de reduction pour les etudiants")
       print ("2. 15% de reduction pour la fidelite superieur ou egale a 5 ans ")
       print ("3. 5 pour les prix superieur a 100")
       print ("4. 10% de reduction pour le code promo ")
    elif choix == 3 :
       print ("au revoir !")
       break
    elif choix < 1 or choix > 3 :
     print ("choix invalide, veuillez reessayer .")
       




       