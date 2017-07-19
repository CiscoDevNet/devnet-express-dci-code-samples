## The UCS Python SDK Makes Deploying Servers a Breeze
## Exercise 1

# Get a handle and login to UCS Manager
from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("198.18.133.91", "admin", "password")
handle.login()

# Look at the handle variables
vars(handle)

# Look at individule handle variables
handle.ip
handle.ucs
handle.cookie

# Logout of the UCS Manager
handle.logout()

# Display UcsHandle Class help
help(UcsHandle)
