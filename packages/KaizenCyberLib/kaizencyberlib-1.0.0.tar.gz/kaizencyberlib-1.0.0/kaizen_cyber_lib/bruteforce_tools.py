import itertools
import hashlib

def brute_force_hash(target_hash: str, charset: str, max_length: int):
    """
    Tente de bruteforcer un hash donné en utilisant une combinaison de caractères.

    :param target_hash: Le hash que l'on tente de casser.
    :param charset: Les caractères possibles (ex : "abc123").
    :param max_length: Longueur maximale des mots de passe à tester.
    :return: Le mot de passe correspondant au hash ou None si rien n'est trouvé.
    """
    for length in range(1, max_length + 1):
        for attempt in itertools.product(charset, repeat=length):
            attempt_password = ''.join(attempt)
            attempt_hash = hashlib.md5(attempt_password.encode()).hexdigest()  # Vous pouvez changer l'algo (e.g., sha256)
            if attempt_hash == target_hash:
                print(f"Mot de passe trouvé : {attempt_password}")
                return attempt_password
    print("Aucun mot de passe trouvé.")
    return None

# Exemple d'utilisation
# hash_target = hashlib.md5("test123".encode()).hexdigest()  # Crée un hash md5 pour "test123"
# brute_force_hash(hash_target, "abcdefghijklmnopqrstuvwxyz1234567890", 6)
