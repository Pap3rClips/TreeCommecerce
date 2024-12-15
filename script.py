from function import *
from tri import *
from users import *


def call_interface():
    print("Bienvenue dans l'interface de gestion de l'inventaire et des utilisateurs")
    register = input("Voulez-vous vous inscrire ? (Oui : 1, J'ai déjà un compte : 2) : ")
    if register == "1":
        add_users()
        return call_interface()
    
    elif register == "2":
        user = input("Veuillez entrer votre nom d'utilisateur : ")
        password = input("Veuillez entrer votre mot de passe : ")
        if not password in open('users.csv').read():
            print("Identifiant ou Mot de passe incorrect !!")
            return call_interface()
        elif not user in open('users.csv').read():
            print("Identifiant incorrect ou Mot de passe incorrect !!")
            return call_interface()
        
        elif password and user in open('users.csv').read():
            admin = user == "admin" and password == "admin"
            choose = 1
            while choose != 0:
                print("---------")
                print("INVENTORY")
                print("---------")
                print("1 - Afficher l'inventaire")
                print("2 - Ajouter à l'inventaire")
                print("3 - Supprimer de l'inventaire")
                print("4 - Trier l'inventaire")
                if admin:
                    print("-----")
                    print("ADMIN")
                    print("-----")
                    print("5 - Afficher les utilisateurs")
                    print("6 - Ajouter un utilisateur")
                    print("7 - Supprimer un utilisateur")
                print("-----------------------")
                print("8 - Mettre à jour un utilisateur")
                print("9 - Quitter l'interface")
                print("-----------------------")
                
                choose = input("Veuillez choisir une méthode : ")
                choose = int(choose)
                if choose == 1:
                    afficher_inventory_csv()
                elif choose == 2:
                    add_to_inventory()
                elif choose == 3:
                    delete_from_inventory()
                elif choose == 4:
                    affiche_tri('inventory.csv')
                elif admin:
                    if choose == 5:
                        afficher_users()
                    elif choose == 6:
                        add_users()
                    elif choose == 7:
                        delete_users()
                if choose == 8:
                    update_users()
                if choose == 9:
                    choose = 0

call_interface()
