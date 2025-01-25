import requests


def find_social_profiles(username: str):
    """
    Recherche des profils sociaux pour un nom d'utilisateur donné.

    :param username: Nom d'utilisateur à rechercher.
    :return: Un dictionnaire des résultats.
    """
    platforms = {
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://twitter.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}/",
        "LinkedIn": f"https://www.linkedin.com/in/{username}/",
        "Facebook": f"https://www.facebook.com/{username}",
        "Pinterest": f"https://www.pinterest.com/{username}",
        "Snapchat": f"https://www.snapchat.com/add/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "Spotify": f"https://open.spotify.com/user/{username}",
        "SoundCloud": f"https://soundcloud.com/{username}",
        "YouTube": f"https://www.youtube.com/user/{username}",
        "Vimeo": f"https://vimeo.com/{username}",
        "Tumblr": f"https://{username}.tumblr.com",
        "Flickr": f"https://www.flickr.com/people/{username}",
        "Medium": f"https://medium.com/@{username}",
        "Quora": f"https://www.quora.com/profile/{username}",
        "DeviantArt": f"https://www.deviantart.com/{username}",
        "Dribbble": f"https://dribbble.com/{username}",
        "Behance": f"https://www.behance.net/{username}",
        # Ajouter d'autres plateformes avec des endpoints disponibles
    }

    results = {}
    headers = {"User-Agent": "KaizenCyberLib/1.0"}

    for platform, url in platforms.items():
        try:
            response = requests.head(url, headers=headers)
            if response.status_code == 200:
                results[platform] = "Profil trouvé"
            else:
                results[platform] = "Pas de profil trouvé"
        except Exception as e:
            results[platform] = f"Erreur : {e}"

    return results

# Exemple d'utilisation
# profiles = find_social_profiles("username123")
# print(profiles)
