#!/usr/bin/env python
"""Basic script to call from EEM."""

import cisco
import sys


def main():
    """Main method to enable interface."""
    interface = cisco.Interface('Eth1/1')
    interface.set_state(s='up')

if __name__ == '__main__':
    sys.exit(main())
