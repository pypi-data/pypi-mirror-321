import whois

def check_domain(domain: str):
    """
    Vérifie les informations Whois d'un domaine.

    :param domain: Nom de domaine à vérifier
    :return: Informations Whois ou message d'erreur
    """
    try:
        domain_info = whois.whois(domain)
        if domain_info:
            print(f"Informations sur le domaine : {domain}")
            print(f"Créé le : {domain_info.creation_date}")
            print(f"Expire le : {domain_info.expiration_date}")
            print(f"Registrar : {domain_info.registrar}")
        else:
            print(f"Impossible de récupérer les informations pour le domaine {domain}.")
    except Exception as e:
        print(f"Erreur lors de la vérification du domaine : {e}")

# Exemple d'utilisation :
# check_domain("example.com")
