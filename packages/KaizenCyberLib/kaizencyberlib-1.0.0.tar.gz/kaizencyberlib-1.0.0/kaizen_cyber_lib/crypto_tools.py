import secrets
import string


def generate_secure_password(length: int = 16) -> str:
    """
    Génère un mot de passe robuste aléatoire.

    :param length: Longueur du mot de passe.
    :return: Mot de passe généré.
    """
    if length < 8:
        raise ValueError("La longueur du mot de passe doit être au moins de 8 caractères.")

    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))
