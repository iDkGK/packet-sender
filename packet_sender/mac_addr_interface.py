import psutil
import netifaces


def get_mac_for_interface(iface_name: str):
    """
    Get mac address of specific interface

    Args:
    - ``iface_name``: interface name

    Returns:
    - Mac address of ``iface_name``

    Raises:
    - ValueError
    """
    addrs = psutil.net_if_addrs()
    iface = addrs.get(iface_name)
    if iface is None:
        raise ValueError("error getting mac address of {}".format(iface_name))

    for snicaddr in iface:
        if snicaddr.family == netifaces.AF_LINK:
            return snicaddr.address


class Mac_Interface:
    def __init__(self, interface: str = "eth0"):
        self.mac = get_mac_for_interface(interface)

    def get_mac(self):
        return self.mac
