## Mission: Programming Cisco Compute - Python Basic and Advanced
## Mission Exercise 1 - Solution

# Get a handle and login to UCS Manager
from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("198.18.133.91", "admin", "password")
handle.login()

# Logout of the UCS Manager
handle.logout()
