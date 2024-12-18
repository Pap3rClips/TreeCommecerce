import pandas as pd
import hashlib
import os

def add_users():
    print("Formulaire d'ajout d'un nouvel utilisateur")
    username = input("Veuillez entrer le nom d'utilisateur :")
    password = hash(input("Veuillez entrer le mot de passe :"))
    
    if username == "admin":
        print("---------------------------------------")
        print("Vous ne pouvez pas créer un utilisateur avec le nom admin")
        print("---------------------------------------")
        return
    if username in open('users.csv').read():
        print("---------------------------------------")
        print("L'utilisateur existe déjà")
        print("---------------------------------------")
        return
    try: 
        with open("users.csv", "a") as files:
            print("Ajout de l'utilisateur dans la base de données ...")
            # hash_password = hash(password)
            files.write(f"{username},{password['hash']},{password['salt']}\n") 
    except PermissionError:
        print("Permissions insuffisantes pour ouvrir le fichier")
    except Exception as e:
        print(f"Erreur inconnue : {e}")

def delete_users():
    name = str(input("Veuillez entrer le nom de l'utilisateur à supprimer : "))
    print("Ouverture de la base de données ...")
    if name not in open('users.csv').read():
        print("---------------------------------------")
        print("L'utilisateur n'existe pas")
        print("---------------------------------------")
        print("Fermeture de la base de données ...")
        return
    try:
        with open('users.csv', 'r') as file:
            content = file.readlines()
        with open('users.csv', 'w') as file:
            for line in content:
                if not line.startswith(name + ','):
                    file.write(line)
    except FileExistsError:
        print("Le fichier n'a pas été trouvé")
    except PermissionError:
        print("Les droits ne sont pas suffisant pour ouvrir le fichier")
    print("---------------------------------------")
    print("Utilisateur supprimé !!")
    print("---------------------------------------")
    print("Fermeture de la base de données ...")


def update_users():
    print("Préparation de la mise à jour des utilisateurs...")
    name = input("Veuillez entrer le nom de l'utilisateur à mettre à jour : ")
    new_name = input("Veuillez entrer le nouveau nom d'utilisateur : ")
    password = input("Veuillez entrer le nouveau mot de passe : ")
    print("Ouverture de la base de données ...")
    if name not in open('users.csv').read():
        print("---------------------------------------")
        print("L'utilisateur n'existe pas")
        print("---------------------------------------")
        print("Fermeture de la base de données ...")
        return
    try:
        with open('users.csv', 'r') as file:
            content = file.readlines()
        with open('users.csv', 'w') as file:
            for line in content:
                if not line.startswith(name + ','):
                    file.write(line)
                else:
                    file.write(f"{new_name},{password['hash']},{password['salt']}\n")
    except FileExistsError:
        print("Le fichier n'a pas été trouvé")
    except PermissionError:
        print("Les droits ne sont pas suffisant pour ouvrir le fichier")
    print("---------------------------------------")
    print("Utilisateur mis à jour !!")
    print("---------------------------------------")
    print("Fermeture de la base de données ...")


def afficher_users():
    try:
        print("____________________________")
        print("Affichage des identifiants :")
        print("----------------------------")
        users = pd.read_csv("users.csv")
        print(users)
    except PermissionError:
        print("Permissions insuffisantes pour ouvrir le fichier")
    except Exception as e:
        print(f"Erreur inconnue : {e}")

def hash(password)->dict:
    salt = os.urandom(16)
    hash_object = hashlib.sha256()
    hash_object.update(salt+password.encode())
    hashed_password = hash_object.hexdigest()
    return {"salt" : salt.hex(), "hash" : hashed_password}

def verify_users(password, hashed_password, salt) -> bool:
    hash_object = hashlib.sha256()
    hash_object.update(password.encode() + salt.encode())
    print(f"Comparaison {hash_object.hexdigest()} avec {hashed_password}")
    if hash_object.hexdigest() == hashed_password:
        return True
    else:
        return False
