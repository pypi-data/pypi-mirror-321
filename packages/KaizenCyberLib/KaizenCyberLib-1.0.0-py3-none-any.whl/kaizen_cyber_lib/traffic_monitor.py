from scapy.all import sniff

def monitor_traffic(interface: str, packet_count: int):
    """
    Surveille le trafic réseau sur une interface donnée.

    :param interface: Nom de l'interface réseau (ex. "eth0", "wlan0").
    :param packet_count: Nombre de paquets à capturer.
    """
    def process_packet(packet):
        print(packet.summary())

    sniff(iface=interface, count=packet_count, prn=process_packet)

# Exemple d'utilisation :
# monitor_traffic("eth0", 10)
