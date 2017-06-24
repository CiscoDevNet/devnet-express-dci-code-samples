## The UCS Python SDK Makes Deploying Servers a Breeze
## Exercise 2

# Get a handle and login to UCS Manager
from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("198.18.133.91", "admin", "password")
handle.login()

# Query the computeBlade Class
handle.query_classid("computeBlade")
blades = handle.query_classid("computeBlade")
print(len(blades))

# Print out all the blade objects
for blade in blades:
    print(blade)

# Print out all the blade object distinguished names
for blade in blades:
    print(blade.dn)

# Query a single computeBlade
single_blade = handle.query_dn("sys/chassis-2/blade-2")
print(single_blade)

# Display computeBlade Class help
from ucsmsdk.mometa.compute import ComputeBlade
help(ComputeBlade)

# Logout of the UCS Manager
handle.logout()
