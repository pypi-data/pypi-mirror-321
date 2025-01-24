from puresnmp import Client, V2C, PyWrapper
import ipaddress
import asyncio

class HuaweiSNMP:
    def __init__(self, community, ip_address):
        self.community = community
        self.ip_address = ip_address
        self.client = PyWrapper(Client(ip_address, V2C(community)))

    def get_addr_tab(self):
        mac_addr_tab = self.get_access_mac()
        ipv4_addr_tab = self.get_access_ipv4()
        ipv6_addr_tab = self.get_access_ipv6()

        common_keys = \
            set(mac_addr_tab.keys()) & \
            set(ipv4_addr_tab.keys()) & \
            set(ipv6_addr_tab.keys())

        addr_tab = []
        for key in common_keys:
            if not ipv4_addr_tab[key].startswith('10.'):
                continue
            if not ipv6_addr_tab[key].startswith('2001:'):
                continue
            addr_tab.append({
                'MAC': mac_addr_tab[key],
                'IPv4': ipv4_addr_tab[key],
                'IPv6': ipv6_addr_tab[key]
            })
        return addr_tab
       
    def get_access_mac(self):
        oid_mac = '1.3.6.1.4.1.2011.5.2.1.15.1.17'
        return asyncio.run(self.snmp_walk(oid_mac, self.conversion_to_mac))

    def get_access_ipv4(self):
        oid_ipv4 = '1.3.6.1.4.1.2011.5.2.1.15.1.15'
        return asyncio.run(self.snmp_walk(oid_ipv4, self.conversion_to_ipv4))

    def get_access_ipv6(self):
        oid_ipv6 = '1.3.6.1.4.1.2011.5.2.1.15.1.60'
        return asyncio.run(self.snmp_walk(oid_ipv6, self.conversion_to_ipv6))

    def conversion_to_mac(self, value):
        try:
            hex_string = value.hex()
            return ':'.join([hex_string[i:i+2] for i in range(2, len(hex_string), 2)])
        except ValueError as e:
            print(f"Error converting Hex-STRING to MAC: {e}")
            return None

    def conversion_to_ipv4(self, value):
        try:
            return str(value)
        except ValueError as e:
            print(f"Error converting Hex-STRING to IPv4: {e}")
            return None

    def conversion_to_ipv6(self, value):
        try:
            ipv6_address = ipaddress.IPv6Address(value)
            return str(ipv6_address)
        except ValueError as e:
            print(f"Error converting Hex-STRING to IPv6: {e}")
            return None

    async def snmp_walk(self, oid, conversion_function):
        result = {}
        try:
            async for var_bind in self.client.walk(oid):
                oid_str = str(var_bind.oid)
                oid_part = oid_str.split('.')[-1]

                conv_str = conversion_function(var_bind.value)
                
                result[oid_part] = conv_str
        except Exception as e:
            print(f"SNMP Walk failed: {e}")
        return result
