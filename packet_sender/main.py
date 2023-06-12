import click
from ethernet import sendp_ether, confp_ether_header


@click.group()
def sendp_cli():
    """Display information"""
    pass


@sendp_cli.group()
def ether():
    """Send ethernet packet"""
    pass


ether.add_command(sendp_ether)
ether.add_command(confp_ether_header)

# sendp_cli.add_command(ether)


@sendp_cli.group()
def arp():
    """Send arp packet"""
    pass


@sendp_cli.group()
def ip():
    """Send ip packet"""
    pass


@sendp_cli.group()
def ipv6():
    """Send ipv6 packet"""
    pass


@sendp_cli.group()
def ecmp():
    """Send ecmp packet"""
    pass


@sendp_cli.group()
def tcp():
    """Send tcp packet"""
    pass


@sendp_cli.group()
def udp():
    """Send udp packet"""
    pass


@sendp_cli.group()
def vxlan():
    """Send vxlan packet"""
    pass


# sendp_cli.add_command(ether)
# sendp_cli.add_command(arp)

if __name__ == "__main__":
    sendp_cli()
