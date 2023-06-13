from __future__ import print_function

import click

# from protocol.arp import send_arp_pkt, configure_arp_pkt
# from protocol.ecmp import send_ecmp_pkt, configure_ecmp_pkt
from protocol.ether import send_ether_pkt, configure_ether_pkt

# from protocol.ip import send_ip_pkt, configure_ip_pkt
# from protocol.ipv6 import send_ipv6_pkt, configure_ipv6_pkt
# from protocol.tcp import send_tcp_pkt, configure_tcp_pkt
# from protocol.udp import send_udp_pkt, configure_udp_pkt
# from protocol.vxlan import send_vxlan_pkt, configure_vxlan_pkt


@click.group()
def packet_sender_cli():
    # type () -> None
    """A tool helpful for sending different protocols of packets"""
    pass


@packet_sender_cli.group()
def arp():
    # type () -> None
    """Send arp packet"""
    pass


@packet_sender_cli.group()
def ecmp():
    # type () -> None
    """Send ecmp packet"""
    pass


@packet_sender_cli.group()
def ether():
    # type () -> None
    """Send ethernet packet"""
    pass


@packet_sender_cli.group()
def ip():
    # type () -> None
    """Send ip packet"""
    pass


@packet_sender_cli.group()
def ipv6():
    # type () -> None
    """Send ipv6 packet"""
    pass


@packet_sender_cli.group()
def tcp():
    # type () -> None
    """Send tcp packet"""
    pass


@packet_sender_cli.group()
def udp():
    # type () -> None
    """Send udp packet"""
    pass


@packet_sender_cli.group()
def vxlan():
    # type () -> None
    """Send vxlan packet"""
    pass


# Add command to arp type
# arp.add_command(configure_arp_pkt)
# arp.add_command(send_arp_pkt)


# Add command to ecmp type
# ecmp.add_command(configure_ecmp_pkt)
# ecmp.add_command(send_ecmp_pkt)


# Add command to ether type
ether.add_command(configure_ether_pkt)
ether.add_command(send_ether_pkt)


# Add command to ip type
# ip.add_command(configure_ip_pkt)
# ip.add_command(send_ip_pkt)


# # Add command to ipv6 type
# ipv6.add_command(configure_ipv6_pkt)
# ipv6.add_command(send_ipv6_pkt)


# Add command to tcp type
# tcp.add_command(configure_tcp_pkt)
# tcp.add_command(send_tcp_pkt)


# Add command to udp type
# udp.add_command(configure_udp_pkt)
# udp.add_command(send_udp_pkt)


# Add command to vxlan type
# vxlan.add_command(configure_vxlan_pkt)
# vxlan.add_command(send_vxlan_pkt)


if __name__ == "__main__":
    packet_sender_cli()
