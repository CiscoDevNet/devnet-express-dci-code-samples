#!/usr/bin/env python
"""Basic script to operate NXOS."""


import cli
import json
import pprint
import sys


def main():
    """Main method to configure VLANs on interfaces."""
    interface_data = {}
    interfaces = [(interface['interface'], interface['state'], interface['portmode'])
                  for interface in json.loads(cli.clid("show interface brief"))['TABLE_interface']['ROW_interface']
                  if 'Eth' in interface['interface']]
    vlans = [(vlan['vlanshowbr-vlanid-utf'], vlan['vlanshowplist-ifidx'])
             for vlan in json.loads(cli.clid("show vlan"))['TABLE_vlanbrief']['ROW_vlanbrief']
             if 'vlanshowplist-ifidx' in vlan.keys()]
    macs = [(mac['disp_mac_addr'], mac['disp_port'])
            for mac in json.loads(cli.clid("show mac address-table"))['TABLE_mac_address']['ROW_mac_address']
            if 'Eth' in mac['disp_port']]

    for interface in interfaces:
        int_info = [interface[1], interface[2]]
        interface_data[interface[0]] = {'int_info': int_info}

        vlan_ids = [vlan[0] for vlan in vlans if interface[0] in vlan[1]]
        interface_data[interface[0]].update({'vlan_ids': vlan_ids})

        mac_addrs = [mac[0] for mac in macs if interface[0] in mac[1]]
        interface_data[interface[0]].update({'mac_addresses': mac_addrs})

    pprint.pprint(interface_data)


if __name__ == '__main__':
    sys.exit(main())
