from function import *
from tri import *

def print_interface():
    print("1 - Afficher les produits de l'inventaire")
    print("2 - Ajouter un produit dans l'inventaire")
    print("3 - Supprimer un produit de l'inventaire")
    print("4 - Tri par ordre alphabétique")
    print("5 - Quitter l'intérface")

def call_interface():
    choose = 1
    while choose!=0:
        print_interface()
        choose = input("Veuillez choisir une méthode : ")
        choose = int(choose)
        if choose==1:
            print_inventory()
        if choose==2:
            add_to_inventory()
        if choose==3:
            delete_from_inventory()
        if choose==4:
            affiche_tri('inventory.txt')
        if choose==5:
            choose = 0

call_interface()