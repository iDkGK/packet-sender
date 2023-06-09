import click

# @click.command(name="add")
# @click.argument('vid',required=True, type=int)
# def sendp_ether(vid):
#     """ add a pojo packet"""
#     print("text:{}".format(vid))
#     pass

@click.command(name="ether")
@click.argument('ether_pkt_id',required=True, type=int)
# @click.option('--packet_id', required=True, type=int, help='ID of Ethernet packet')
def ether(packet_id):
    """Send ethernet packet to other"""
    pass