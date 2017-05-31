#!/usr/bin/env python
"""Basic script to print hostname using nxtoolkit1."""

import nxtoolkit.nxtoolkit as NX
import sys

username = 'admin'
password = 'C1sco12345'
device = 'http://198.18.134.140/'


def main():
    """Simple main method to retrieve hostname."""
    session = NX.Session(device, username, password)
    session.login()
    print("This NXOS device has the following hostname:")
    print(session.get('/api/mo/sys.json').json()
          ['imdata'][0]['topSystem']['attributes']['name'])


if __name__ == '__main__':
    sys.exit(main())
