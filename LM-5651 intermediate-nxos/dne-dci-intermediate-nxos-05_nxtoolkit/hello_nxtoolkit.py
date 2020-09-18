#!/usr/bin/env python
"""Basic script to print hostname using nxtoolkit1."""
# pylint: disable=import-error

import sys
import nxtoolkit.nxtoolkit as NX

USERNAME = 'admin'
PASSWORD = 'C1sco12345'
DEVICE = 'http://198.18.134.140/'


def main():
    """Simple main method to retrieve hostname."""
    session = NX.Session(DEVICE, USERNAME, PASSWORD)
    session.login()
    print("This NXOS device has the following hostname:")
    print(session.get('/api/mo/sys.json').json()
        ['imdata'][0]['topSystem']['attributes']['name'])


if __name__ == '__main__':
    sys.exit(main())
