from kaizen_cyber_lib.crypto_tools import generate_secure_password

def test_generate_secure_password():
    password = generate_secure_password(12)
    assert len(password) == 12
    assert any(char.isdigit() for char in password), "Le mot de passe doit contenir des chiffres."
    assert any(char.isalpha() for char in password), "Le mot de passe doit contenir des lettres."
    assert any(not char.isalnum() for char in password), "Le mot de passe doit contenir des caractères spéciaux."
