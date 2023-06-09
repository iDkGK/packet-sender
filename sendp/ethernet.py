import click
from redis_db import RedisClient
from mac_addr_interface import Mac_Interface

redis_db = RedisClient(db=0)#对数据库进行操作，你想要操作的数据库


@click.command(name="send")
@click.argument('ether_pkt_id',metavar='<ether_packet_id>',required=True, type=int)
@click.argument('interface',metavar='<EthernetX>',required=True)
def sendp_ether(vid):
    """ send ethernet packet by EthernetX"""
    print("text:{}".format(vid))
    pass

@click.command(name="conf")
@click.argument('ether_pkt_id',metavar='<ether_packet_id>',required=True, type=int)
@click.option('-s','--src',required=False,help='Source mac address of Ethernet packet')
@click.option('-d','--dst',required=False, help='Destination mac address of Ethernet packet')
@click.option('-t','--type',required=False,help='Type of Ethernet packet')
def confp_ether_header(ether_pkt_id,src,dst,type):
    """ config header of ethernet packet that id is ether_packet_id"""
    key="ETHER_PKT:HEADER:{}".format(ether_pkt_id)
    srcmac="00:11:22:33:44:55"
    if src == None:
        srcmac = Mac_Interface("eth0").get_mac()
    else :
        srcmac= src
    
    if dst == None:
        dstmac="ff:ff:ff:ff:ff:ff"
    else :
        dstmac=dst
    
    if type == None:
        etype="0x8000"
    else :
        etype=type
    fields = {"src_addr":"{}".formac(srcmac),"dst_addr":"{}".formac(dstmac),"type":"{}".format(etype)}
    # redis_db.set(key,fields)
    print(key,fields)

