import requests


def check_email_on_services(email: str):
    """
    Vérifie si une adresse email est associée à des services connus.

    :param email: Adresse email à vérifier.
    :return: Un dictionnaire avec les résultats.
    """
    services = {
        "GitHub": f"https://api.github.com/search/users?q={email}",
        "Twitter": f"https://twitter.com/i/api/1.1/users/lookup.json?email={email}",
        "LinkedIn": f"https://api.linkedin.com/v2/emailAddress?q={email}",
        "Facebook": f"https://graph.facebook.com/v9.0/search?q={email}&type=user",
        "Instagram": f"https://api.instagram.com/v1/users/search?q={email}",
        "Pinterest": f"https://api.pinterest.com/v3/search/pins/?query={email}",
        "Snapchat": f"https://kit.snapchat.com/v1/users/search?q={email}",
        "TikTok": f"https://api.tiktok.com/v1/users/search?q={email}",
        "Reddit": f"https://www.reddit.com/api/v1/user/{email}",
        "Spotify": f"https://api.spotify.com/v1/search?q={email}&type=user",
        "SoundCloud": f"https://api.soundcloud.com/users?q={email}",
        "YouTube": f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={email}&type=user",
        "Vimeo": f"https://api.vimeo.com/users?query={email}",
        "Tumblr": f"https://api.tumblr.com/v2/blog/{email}.tumblr.com/info",
        "Flickr": f"https://api.flickr.com/services/rest/?method=flickr.people.findByEmail&find_email={email}",
        "Medium": f"https://api.medium.com/v1/users/{email}",
        "Quora": f"https://www.quora.com/profile/{email}",
        "DeviantArt": f"https://www.deviantart.com/api/v1/oauth2/user/search?q={email}",
        "Dribbble": f"https://api.dribbble.com/v2/user/{email}",
        "Behance": f"https://api.behance.net/v2/users?q={email}",
        # Ajouter d'autres services avec des endpoints disponibles
    }

    results = {}
    headers = {"User-Agent": "KaizenCyberLib/1.0"}

    for service, url in services.items():
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                results[service] = "Compte trouvé"
            else:
                results[service] = "Pas de compte trouvé"
        except Exception as e:
            results[service] = f"Erreur : {e}"

    return results

# Exemple d'utilisation
# results = check_email_on_services("example@example.com")
# print(results)
