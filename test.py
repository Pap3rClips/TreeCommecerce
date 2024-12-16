import pandas

try:
    users_data = pandas.read_csv('users.csv')
except FileNotFoundError as e:
    print(f"Le fichier n'a pas put être trouvé : {e}")
except PermissionError as e:
    print(f"Vous ne possedez pas les permissions suffisante : {e}")
except Exception as e:
    print(f"Erreur : {e}")

i = 1
users_data_dict = users_data.to_dict()

search = "hadrien"
for key in users_data_dict['username'].keys():
    if search == users_data_dict['username'][key]:
        print(f"HIT : {users_data_dict['password'][key]}")