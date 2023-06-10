import psutil
import netifaces

def get_mac_for_interface(iface_name):
    # 获取网卡名称与MAC地址的映射关系
    addrs = psutil.net_if_addrs()

    # 遍历所有网卡，查找指定网卡的MAC地址
    for iface in addrs:
        if iface == iface_name:
            for snicaddr in addrs[iface]:
                if snicaddr.family == netifaces.AF_LINK:
                    mac_address = snicaddr.address
                    print(mac_address)
                    
class Mac_Interface:
    def __init__(self, interface="eth0"):
        self.mac=get_mac_for_interface(interface)
        
    def get_mac(self):
        return self.mac