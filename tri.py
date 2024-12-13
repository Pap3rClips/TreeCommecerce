def tri_bulles(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

def affiche_tri(nom_fichier):
    tri = input("Veuillez choisir le type de tri (1: tri par ordre alphabétique, 2: tri par prix) : ")
    try:
        with open(nom_fichier, 'r') as f:
            if tri =="1":   
                lignes = f.readlines()
                # Supprimer les caractères de nouvelle ligne
                lignes = [ligne.strip() for ligne in lignes]
                # Trier les lignes par nom de produit
                lignes_tries = tri_bulles(lignes)
                # Afficher les produits triés
                i = 1
                for ligne in lignes_tries:
                    name, quantity, price = ligne.split(",")
                    print("----------------------------")
                    print(f"Produit {i}")
                    print("---")
                    print(f"Nom du produit : {name}")
                    print(f"Quantité du produit : {quantity}")
                    print(f"Prix du produit : {price}")
                    print("----------------------------")
                    i += 1
            if tri =="2":
                lignes = f.readlines()
                # Supprimer les caractères de nouvelle ligne
                lignes = [ligne.strip() for ligne in lignes]
                # Trier les lignes par prix
                lignes_tries = quicksort(lignes)
                # Afficher les produits triés
                i = 1
                for ligne in lignes_tries:
                    name, quantity, price = ligne.split(",")
                    print("----------------------------")
                    print(f"Produit {i}")
                    print("---")
                    print(f"Nom du produit : {name}")
                    print(f"Quantité du produit : {quantity}")
                    print(f"Prix du produit : {price}")
                    print("----------------------------")
                    i += 1
    except FileNotFoundError:
        print("Le fichier n'a pas pu être trouvé.")
    except PermissionError:
        print("Les droits ne sont pas suffisants pour lire le fichier")


def quicksort(tab):
    pivot = tab[len(tab)//2]
    left = []
    middle = []
    right = []
    for element in tab:
        if element < pivot:
            left.append(element)
        elif element > pivot:
            right.append(element)
        else:
            middle.append(element)
    return quicksort(left) + middle + quicksort(right)