#!/usr/bin/env python
################################################################################
#                                                                              #
# Copyright (c) 2015 Cisco Systems                                             #
# All Rights Reserved.                                                         #
#                                                                              #
#    Licensed under the Apache License, Version 2.0 (the "License"); you may   #
#    not use this file except in compliance with the License. You may obtain   #
#    a copy of the License at                                                  #
#                                                                              #
#         http://www.apache.org/licenses/LICENSE-2.0                           #
#                                                                              #
#    Unless required by applicable law or agreed to in writing, software       #
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT #
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the  #
#    License for the specific language governing permissions and limitations   #
#    under the License.                                                        #
#                                                                              #
################################################################################
"""
Simple application that logs on to the Switch and configure the Interfaces.
"""
import nxtoolkit.nxtoolkit as NX
import sys


def main():
    """
    Main execution routine

    :return: None
    """
    # Take login credentials from the command line if provided
    # Otherwise, take them from your environment variables file ~/.profile
    description = '''Simple application that logs on to the Switch and
                    configure the Interfaces.'''
    creds = NX.Credentials('switch', description)
    args = creds.get()

    # Login to Switch
    session = NX.Session(args.url, args.login, args.password)
    resp = session.login()
    if not resp.ok:
        print('%% Could not login to Switch')
        sys.exit(0)

    interface = NX.Interface('eth1/10')

    # Print original access VLAN
    print("Starting VLAN:")
    print(interface.get_access_vlan())

    # Setting interface attributes
    # Note: if attributes are not set, then default values will be used
    interface.set_mode('access')
    interface.set_access_vlan('vlan-100')

    # Push entire configuration to the switch
    # Note:To configure only one interface use int1.get_url() & int1.get_json()
    resp = session.push_to_switch(interface.get_url(), interface.get_json())
    if not resp.ok:
        print ('%% Could not push to Switch')
        print (resp.text)
        sys.exit(0)

    # Print original access VLAN
    print("New VLAN:")
    print(interface.get_access_vlan())



if __name__ == '__main__':
    sys.exit(main())
