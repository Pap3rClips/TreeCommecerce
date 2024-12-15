def tri_bulles(tab):#tri par prix
    n = len(tab)
    for i in range(n):
        for j in range(0, n-i-1):
            prix_j = float(tab[j].split(",")[2])
            prix_j1 = float(tab[j+1].split(",")[2])
            if prix_j > prix_j1:
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab

def affiche_tri(nom_fichier):
    sort = input("Veuillez choisir le type de tri (1: tri par ordre alphabétique, 2: tri par prix, 3: tri par quantité) : ")
    try:
        with open(nom_fichier, 'r') as f:
            if sort =="1":   
                lines = f.readlines()
                # Supprimer les caractères de nouvelle ligne
                lines = [line.strip() for line in lines]
                # Trier les lines par nom de produit
                lines_sorted = quicksort(lines)
                # Afficher les produits triés
                i = 1
                for line in lines_sorted:
                    name, quantity, price = line.split(",")
                    print("----------------------------")
                    print(f"Produit {i}")
                    print("---")
                    print(f"Nom du produit : {name}")
                    print(f"Quantité du produit : {quantity}")
                    print(f"Prix du produit : {price}")
                    print("----------------------------")
                    i += 1
            if sort =="2":
                lines = f.readlines()
                # Supprimer les caractères de nouvelle line
                lines = [ligne.strip() for ligne in lines]
                # Trier les lines par prix
                lines_sorted = tri_bulles(lines)
                # Afficher les produits triés
                i = 1
                for line in lines_sorted:
                    name, quantity, price = line.split(",")
                    print("----------------------------")
                    print(f"Produit {i}")
                    print("---")
                    print(f"Nom du produit : {name}")
                    print(f"Quantité du produit : {quantity}")
                    print(f"Prix du produit : {price}")
                    print("----------------------------")
                    i += 1
            if sort =="3":
                lines = f.readlines()
                # Supprimer les caractères de nouvelle line
                lines = [ligne.strip() for ligne in lines]
                # Trier les lines par prix
                lines_sorted = tri_selection(lines)
                # Afficher les produits triés
                i = 1
                for line in lines_sorted:
                    name, quantity, price = line.split(",")
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


def quicksort(tab):#tri par ordre alphabétique
    if len(tab) <= 1:
        return tab
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

def tri_selection(tab):#tri par quantité
    n = len(tab)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            quantite_min_index = int(tab[min_index].split(",")[1])
            quantite_j = int(tab[j].split(",")[1])
            if quantite_j < quantite_min_index:
                min_index = j
        tab[i], tab[min_index] = tab[min_index], tab[i]
    return tab  
                