import pandas as pd
import os

def get_inventory_file(user):
    inventory_file = f"{user}.csv"
    if not os.path.exists(inventory_file):
            pd.DataFrame(columns=["Nom", "Quantité", "Prix"]).to_csv(inventory_file, index=False)
    return inventory_file

def afficher_inventory_csv(user):
    inventory_file = get_inventory_file(user)
    try:
        print("_______________________")
        print("Affichage des produits:")
        print("-----------------------")
        products = pd.read_csv(inventory_file)
        print(products)
    except PermissionError:
        print("Permissions insuffisantes pour ouvrir le fichier")
    except Exception as e:
        print(f"Erreur inconnue : {e}")




def add_to_inventory(user):
    inventory_file = get_inventory_file(user)
    print("Préparation de l'ajout dans l'inventaire...")
    while True:
        name = input("Veuillez entrer le nom du produit : ").strip()  # Supprime les espaces avant et après
        if name and not any(char.isdigit() for char in name):  # Si le nom n'est pas vide et ne contient pas de chiffres
            break
        elif name == "":
            print("Erreur : Le nom du produit ne peut pas être vide. Veuillez retaper le nom.")
        else:
            print("Erreur : Le nom du produit ne peut pas contenir de chiffres. Veuillez retaper le nom.")
    while True:
        try:
            quantity = int(input("Veuillez entrer la quantité du produit : "))
            break  
        except ValueError:
            print("Erreur : La quantité doit être un nombre entier. Veuillez retaper la quantité.")

    
    while True:
        try:
            price = float(input("Veuillez entrer le prix du produit : "))
            break  
        except ValueError:
            print("Erreur : Le prix doit être un nombre décimal. Veuillez retaper le prix.")
    print("Ouverture de l'inventaire ...")
    try:
        with open(inventory_file, 'a') as file:
            print("Ajout de l'objet dans l'inventaire ...")
            file.write(f'{name},{quantity},{price}\n')
    except PermissionError:
        print("Permissions insuffisantes pour ouvrir le fichier")
    except Exception as e:
        print(f"Erreur inconnue : {e}")
    print("Fermeture de l'aventaire...")

def delete_from_inventory(user):
    inventory_file = get_inventory_file(user)
    name = str(input("Veuillez entrer le nom du fichier à supprimer : "))
    print("Ouverture de l'inventaire")
    if name not in open('users.csv').read():
        print("---------------------------------------")
        print("Le produit n'existe pas")
        print("---------------------------------------")
        print("Fermeture de l'inventaire ...")
        return
    try:
        with open(inventory_file, 'r') as file:
            content = file.readlines()
        with open(inventory_file, 'w') as file:
            for line in content:
                if not line.startswith(name + ','):
                    print("hit")
                    file.write(line)
    except FileExistsError:
        print("Le fichier n'a pas été trouvé")
    except PermissionError:
        print("Les droits ne sont pas suffisant pour ouvrir le fichier")
    print("---------------------------------------")
    print("Produit supprimé !!")
    print("---------------------------------------")
    print("Fermeture de l'inventaire")

