import psutil
import tabulate

iface_mac_mappings: dict[str, str] = dict(
    map(
        lambda fkvp: (
            fkvp[0],
            list(filter(lambda fvalue: fvalue.family.name == "AF_LINK", fkvp[1]))[
                0
            ].address,
        ),
        filter(
            lambda kvp: any(map(lambda value: value.family.name == "AF_LINK", kvp[1])),
            psutil.net_if_addrs().items(),
        ),
    )
)

iface_ip_mappings: dict[str, str] = dict(
    map(
        lambda fkvp: (
            fkvp[0],
            list(filter(lambda fvalue: fvalue.family.name == "AF_INET", fkvp[1]))[
                0
            ].address,
        ),
        filter(
            lambda kvp: any(map(lambda value: value.family.name == "AF_INET", kvp[1])),
            psutil.net_if_addrs().items(),
        ),
    )
)

iface_ipv6_mappings: dict[str, str] = dict(
    map(
        lambda fkvp: (
            fkvp[0],
            list(filter(lambda fvalue: fvalue.family.name == "AF_INET6", fkvp[1]))[
                0
            ].address,
        ),
        filter(
            lambda kvp: any(map(lambda value: value.family.name == "AF_INET6", kvp[1])),
            psutil.net_if_addrs().items(),
        ),
    )
)


def get_iface_mac_address(iface_name: str) -> str:
    """
    Get mac address of specific interface

    Args:
    - ``iface_name``: interface name

    Returns:
    - Mac address of ``iface_name``

    Raises:
    - ValueError
    """
    iface_mac_address = iface_mac_mappings.get(iface_name)
    if iface_mac_address is None:
        raise ValueError(
            "error getting interface {}. Available interfaces are listed below:\n{}".format(
                iface_name,
                tabulate.tabulate(
                    iface_mac_mappings.items(),
                    headers=["Interface Name", "MAC Address"],
                ),
            )
        )
    return iface_mac_address


def get_iface_ip_address(iface_name: str) -> str:
    """
    Get mac address of specific interface

    Args:
    - ``iface_name``: interface name

    Returns:
    - Mac address of ``iface_name``

    Raises:
    - ValueError
    """
    iface_ip_address = iface_ip_mappings.get(iface_name)
    if iface_ip_address is None:
        raise ValueError(
            "error getting interface {}. Available interfaces are listed below:\n{}".format(
                iface_name,
                tabulate.tabulate(
                    iface_ip_mappings.items(),
                    headers=["Interface Name", "IP Address"],
                ),
            )
        )
    return iface_ip_address


def get_iface_ipv6_address(iface_name: str) -> str:
    """
    Get mac address of specific interface

    Args:
    - ``iface_name``: interface name

    Returns:
    - Mac address of ``iface_name``

    Raises:
    - ValueError
    """
    iface_ipv6_address = iface_ipv6_mappings.get(iface_name)
    if iface_ipv6_address is None:
        raise ValueError(
            "error getting interface {}. Available interfaces are listed below:\n{}".format(
                iface_name,
                tabulate.tabulate(
                    iface_ipv6_mappings.items(),
                    headers=["Interface Name", "IPv6 Address"],
                ),
            )
        )
    return iface_ipv6_address
