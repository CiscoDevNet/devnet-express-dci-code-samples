## Mission: Programming Cisco Compute - Python Basic and Advanced
## Mission Exercise 1 - Solution

from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("198.18.133.91", "admin", "password")
handle.login()

handle.logout()
