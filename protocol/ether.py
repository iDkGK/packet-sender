import click
from database.redisclient import redisclient
from interface import interface


@click.command(name="conf")
@click.argument("pkt_id", metavar="<ether_packet_id>", required=True, type=int)
@click.option(
    "-s", "--src", required=False, help="Source mac address of Ethernet packet"
)
@click.option(
    "-d", "--dst", required=False, help="Destination mac address of Ethernet packet"
)
@click.option("-t", "--type", required=False, help="Type of Ethernet packet")
def configure_ether_pkt(
    pkt_id: int,
    src: str | None = None,
    dst: str | None = None,
    type: str | None = None,
) -> None:
    """
    Configure header of an ethernet packet

    Args:
    - ``pkt_id``: packet id
    - ``src``: source mac address
    - ``dst``: destination mac address
    - ``type``: packet type

    Returns:
    - True if configuration succeeded
    - False if configuration failed

    Raises:
    None
    """
    key = "ETHER_PKT:HEADER: {}".format(pkt_id)
    src = interface.get_iface_mac_address("eth0") if src is None else src
    dst = "ff:ff:ff:ff:ff:ff" if dst is None else dst
    type = "0x8000" if type is None else type
    fields = {
        "src_addr": src,
        "dst_addr": dst,
        "type": type,
    }
    # redisclient.set(key, fields)
    print(key, fields)


@click.command(name="send")
@click.argument("pkt_id", metavar="<ether_packet_id>", required=True, type=int)
@click.argument("interface", metavar="<EthernetX>", required=True)
def send_ether_pkt(pkt_id: int) -> None:
    """
    Send ethernet packet

    Args:
    - ``pkt_id``: packet id

    Returns:
    None

    Raises:
    None
    """
    print("text: {}".format(pkt_id))
