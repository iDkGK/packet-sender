import psutil
import tabulate

iface_mac_mappings: dict[str, str] = dict(
    map(
        lambda fkvp: (
            fkvp[0],
            list(filter(lambda fvalue: fvalue.family.name, fkvp[1]))[0].address,
        ),
        filter(
            lambda kvp: any(map(lambda value: value.family.name == "AF_LINK", kvp[1])),
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
                    headers=["Interface Name", "Mac Address"],
                ),
            )
        )
    return iface_mac_address
