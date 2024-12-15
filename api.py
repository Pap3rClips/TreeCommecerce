import requests
import hashlib

def check_password(password):
    hash_object = hashlib.sha1()
    hash_object.update(password.encode())
    hash = hash_object.hexdigest().upper()
    prefix = hash[:5]
    suffix = hash[5:]
    
    url = f"https://api.pwnedpasswords.com/range/{prefix}"

    try:
        response = requests.get(url)
    except requests.exceptions.HTTPError as e:
        print(f"Erreur HTTP : {e}")
    except requests.exceptions.ConnectionError as e:
        print(f"Erreur de connexion : {e}")
    except requests.exceptions.Timeout as e:
        print(f"Requête expirée : {e}")
    except requests.exceptions.RequestException as e:
        print(f"Une erreur est survenue : {e}")
    if suffix in response.text:
        return True
    else:
        return False    

def ask_password():
    password = str(input("Veuillez entrer un mot de passe à tester : "))
    print("Lancement de la vérification du mot de passe...")
    if check_password(password):
        print("Ton mot de passe n'est pas sécurisé !")
    else:
        print("Ton mot de passe est sécurisé pour le moment...")