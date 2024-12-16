from function import *
from tri import *
from users import *
from api import *

def call_interface():
    print("Bienvenue dans l'interface de gestion de l'inventaire et des utilisateurs")
    register = input("Voulez-vous vous inscrire ? (Oui : 1, J'ai déjà un compte : 2) : ")
    if register == "1":
        add_users()
        return call_interface()
    
    elif register == "2":
        user = input("Veuillez entrer votre nom d'utilisateur : ")
        password = input("Veuillez entrer votre mot de passe : ")
        try:
            print("Ouverture de la base de donnée")
            users_data = pd.read_csv('users.csv')
            users_data_dict = users_data.to_dict()
            print(users_data_dict)
        except FileNotFoundError as e:
            print(f"Le fichier n'a pas put être trouvé : {e}")
        except PermissionError as e:
            print(f"Vous ne possedez pas les permissions suffisante : {e}")
        except Exception as e:
            print(f"Erreur : {e}")
        if users_data_dict['username']:
            for key in users_data_dict['username'].keys():
                if user == users_data_dict['username'][key]:
                    true_password = users_data_dict['password'][key]
                    true_salt = users_data_dict['salt'][key]
                    if verify_users(password, true_password, true_salt):
                        admin = user == "admin" and password == "admin"
                        choose = 1
                        while choose != 0:
                            print("---------")
                            print("INVENTAIRE")
                            print("---------")
                            print("1 - Afficher l'inventaire")
                            print("2 - Ajouter à l'inventaire")
                            print("3 - Supprimer de l'inventaire")
                            print("4 - Trier l'inventaire")
                            print("---------")
                            print("SECURITE")
                            print("---------")
                            print("5 - Vérification de mot de passe")
                            print("6 - Alerte de sécurité")
                            if admin:
                                print("-----")
                                print("ADMIN")
                                print("-----")
                                print("7 - Afficher les utilisateurs")
                                print("8 - Ajouter un utilisateur")
                                print("9 - Supprimer un utilisateur")
                            print("-----------------------")
                            print("10 - Mettre à jour un utilisateur")
                            print("11 - Quitter l'interface")
                            print("-----------------------")
                            
                            choose = input("Veuillez choisir une méthode : ")
                            choose = int(choose)
                            if choose == 1:
                                afficher_inventory_csv(user)
                            elif choose == 2:
                                add_to_inventory(user)
                            elif choose == 3:
                                delete_from_inventory(user)
                            elif choose == 4:
                                affiche_tri(get_inventory_file(user))
                            elif choose == 5:
                                ask_password()
                            elif choose == 6:
                                pass
                            elif admin:
                                if choose == 7:
                                    afficher_users()
                                elif choose == 8:
                                    add_users()
                                elif choose == 9:
                                    delete_users()
                            elif choose == 10:
                                update_users()
                            elif choose == 11:
                                choose = 0
                    else:
                        print("Utilisateur ou mot de passe incorrecte 1")
                        call_interface()
                else:
                    print("Utilisateur ou mot de passe incorrecte")
                    call_interface()
        else:
            print("La base de donnée est vide, créer de nouveau utilisateurs")
            call_interface()

        

call_interface()
