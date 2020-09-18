#!/usr/bin/env python
"""Basic script to call from EEM."""
# pylint: disable=import-error

import sys
import cisco


def main():
    """Main method to enable interface."""
    interface = cisco.Interface('Eth1/1')
    interface.set_state(s='up')

if __name__ == '__main__':
    sys.exit(main())
