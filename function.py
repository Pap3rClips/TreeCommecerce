def print_inventory():
    print("Vous avez choisit l'afficachage de l'invenataire")
    try:
        with open('inventory.txt', 'r') as file:
            i = 1
            for line in file:
                name,quantity,price = line.split(",")
                print("----------------------------")
                print(f"Produit {i}")
                print("---")
                print(f"Nom du produit : {name}")
                print(f"Quantité du produit : {quantity}")
                print(f"Prix du produit : {price}")
                print("----------------------------")
                i += 1
    except FileNotFoundError:
        print("Le fichier n'a pas put être trouvé.")
    except PermissionError:
        print("Les droits ne sont pas suffisant pour lire le fichier")

def add_to_inventory():
    print("Préparation de l'ajout dans l'inventaire...")
    name = input("Veuillez entrer le nom du produit : ")
    quantity = input("Veuillez entrer la quantité du produit : ")
    price = input("Veuillez entrer le prix du produit : ")
    print("Ouverture de l'inventaire ...")
    try:
        with open('inventory.txt', 'a') as file:
            print("Ajout de l'objet dans l'inventaire ...")
            file.write(f'{name},{quantity},{price}\n')
    except PermissionError:
        print("Permissions insuffisantes pour ouvrir le fichier")
    except Exception as e:
        print(f"Erreur inconnue : {e}")
    print("Fermeture de l'aventaire...")

def delete_from_inventory():
    name = str(input("Veuillez entrer le nom du fichier à supprimer : "))
    print("Ouverture de l'inventaire")
    try:
        with open('inventory.txt', 'r') as file:
            content = file.readlines()
        with open('inventory.txt', 'w') as file:
            for line in content:
                if not line.startswith(name + ','):
                    print("hit")
                    file.write(line)
    except FileExistsError:
        print("Le fichier n'a pas été trouvé")
    except PermissionError:
        print("Les droits ne sont pas suffisant pour ouvrir le fichier")
    print("Fermeture de l'inventaire")