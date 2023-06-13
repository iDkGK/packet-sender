from __future__ import print_function

import click
from typing import Callable, Union
from utilities.interface import get_iface_mac_address

# from utilities.redisclient import redisclient


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
    pkt_id,  # type: int
    src=None,  # type: Union[str, None]
    dst=None,  # type: Union[str, None]
    type=None,  # type: Union[str, None]
):
    # type: (int, Union[str, None], Union[str, None], Union[str, None]) -> None
    """
    Configure header of an ethernet packet
    """
    key = "ETHER_PKT:HEADER: {}".format(pkt_id)
    src = get_iface_mac_address("eth0") if src is None else src
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
def send_ether_pkt(
    pkt_id,  # type: int
):
    # type: (int) -> None
    """
    Send ethernet packet
    """
    print("text: {}".format(pkt_id))
