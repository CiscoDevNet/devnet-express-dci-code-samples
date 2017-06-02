#!/usr/bin/env python
"""Basic script to operate VLANs."""

import argparse
import cli
import sys


def configure_vlans(vlans, oper, interfaces):
    """Configure VLANs on required interfaces."""
    if vlans:
        if interfaces:
            if oper == 'add':
                conf = 'conf t ; interface '
                for interface in interfaces:
                    print('Adding VLANs: {vlans} to interface: '
                          '{interface}'.format(interface=interface,
                                               vlans=",".join(map(str, vlans))))
                    cli.cli('{conf} {interface} ; '
                            'switchport trunk allowed vlan add {vlans}'.format(conf=conf,
                                                                               interface=interface,
                                                                               vlans=",".join(map(str, vlans))))
            elif oper == 'delete':
                remove = 'conf t ; interface '
                for interface in interfaces:
                    print('Removing VLANs: {vlans} from interface: '
                          '{interface}'.format(interface=interface,
                                               vlans=",".join(map(str, vlans))))
                    cli.cli('{remove} {interface} ; '
                            'switchport trunk allowed vlan remove {vlans}'.format(remove=remove,
                                                                                  interface=interface,
                                                                                  vlans=",".join(map(str, vlans))))

        else:
            if oper == 'add':
                print('Adding VLANs: {vlans}'.format(vlans=",".join(map(str, vlans))))
                conf = 'conf t ; vlan '
                cli.cli("{conf} {vlans}".format(conf=conf,
                                                vlans=",".join(map(str, vlans))))
            elif oper == 'delete':
                print('Removing VLANs: {vlans}'.format(vlans=",".join(map(str, vlans))))
                remove = 'conf t ; no vlan '
                cli.cli("{remove} {vlans}".format(remove=remove,
                                                  vlans=",".join(map(str, vlans))))


def main():
    """Main method to configure VLANs on interfaces."""
    parent = argparse.ArgumentParser()
    parent.add_argument('--oper', choices=['add', 'delete'], default='add',
                        help="When configuring, choose either `add` or `delete`")
    parent.add_argument('--vlans', '-v', nargs='+',
                        help="VLAN number (1-4094)", type=int)
    parent.add_argument('--interfaces', '-i', nargs='+',
                        help="Interface name to use")
    args = parent.parse_args()
    configure_vlans(args.vlans, args.oper, args.interfaces)


if __name__ == '__main__':
    sys.exit(main())
