import click
from redis_db import RedisClient
from mac_addr_interface import Mac_Interface

redis_db = RedisClient(db=0)


@click.command(name="send")
@click.argument("ether_pkt_id", metavar="<ether_packet_id>", required=True, type=int)
@click.argument("interface", metavar="<EthernetX>", required=True)
def sendp_ether(ether_pkt_id: int):
    """
    Send ethernet packet

    Args:
    - ``ether_pkt_id``: packet id

    Returns:
    None

    Raises:
    None
    """
    print("text: {}".format(ether_pkt_id))


@click.command(name="conf")
@click.argument("ether_pkt_id", metavar="<ether_packet_id>", required=True, type=int)
@click.option(
    "-s", "--src", required=False, help="Source mac address of Ethernet packet"
)
@click.option(
    "-d", "--dst", required=False, help="Destination mac address of Ethernet packet"
)
@click.option("-t", "--type", required=False, help="Type of Ethernet packet")
def confp_ether_header(
    ether_pkt_id: int,
    src: str | None = None,
    dst: str | None = None,
    type: str | None = None,
):
    """
    Configure header of an ethernet packet

    Args:
    - ``ether_pkt_id``: packet id
    - ``src``: source mac address
    - ``dst``: destination mac address
    - ``type``: packet type

    Returns:
    - True if configuration succeeded
    - False if configuration failed

    Raises:
    None
    """
    key = "ETHER_PKT:HEADER: {}".format(ether_pkt_id)
    srcmac = Mac_Interface("eth0").get_mac() if src is None else src
    dstmac = "ff:ff:ff:ff:ff:ff" if dst is None else dst
    etype = "0x8000" if type is None else type
    fields = {
        "src_addr": "{}".format(srcmac),
        "dst_addr": "{}".format(dstmac),
        "type": "{}".format(etype),
    }
    # redis_db.set(key, fields)
    print(key, fields)
