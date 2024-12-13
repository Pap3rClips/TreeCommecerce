from TreeCommecerce.function import *
from TreeCommecerce.tri import *
from users import *

def print_interface():
    print("---------")
    print("INVENTORY")
    print("---------")
    print("1 - Afficher les produits de l'inventaire (CSV)")
    print("2 - Ajouter un produit dans l'inventaire")
    print("3 - Supprimer un produit de l'inventaire")
    print("4 - Tri par ordre alphabétique(fonctionnel) ou par prix(pas encore fonctionnel)")
    print("-----")
    print("USERS")
    print("-----")
    print("5 - Afficher les utilisateurs")
    print("6 - Ajouter un utilisateur")
    print("7 - Supprimer un utilisateur")
    print("8 - Mettre à jour un utilisateur")
    print("-----------------------")
    print("9 - Quitter l'interface")
    print("-----------------------")
    
    

def call_interface():
    user = input("Veuillez entrer votre nom d'utilisateur : ")
    password = input("Veuillez entrer votre mot de passe : ")
    if not password and user in open('users.csv').read():
        return print("Identifiant incorrect") 
    elif password and user in open('users.csv').read():
        choose = 1
        while choose!=0:
            print_interface()
            choose = input("Veuillez choisir une méthode : ")
            choose = int(choose)
            if choose==1:
                afficher_inventory_csv()
            if choose==2:
                add_to_inventory()
            if choose==3:
                delete_from_inventory()
            if choose==4:
                affiche_tri('inventory.csv')
            if choose==5:
                afficher_users()
            if choose==6:
                add_users()
            if choose==7:
                delete_users()
            if choose==8:
                update_users()
            if choose==9:
                choose=0
        

call_interface()