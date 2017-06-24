## The UCS Python SDK Makes Deploying Servers a Breeze
## Exercise 1

from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("198.18.133.91", "admin", "password")
handle.login()

vars(handle)

handle.ip
handle.ucs
handle.cookie

handle.logout()

help(UcsHandle)
