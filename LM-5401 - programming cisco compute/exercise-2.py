## The UCS Python SDK Makes Deploying Servers a Breeze
## Exercise 2

from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("198.18.133.91", "admin", "password")
handle.login()

handle.query_classid("computeBlade")
blades = handle.query_classid("computeBlade")
print len(blades)

for blade in blades:
    print(blade)

for blade in blades:
    print(blade.dn)

single_blade = handle.query_dn("sys/chassis-2/blade-2")
print(single_blade)

from ucsmsdk.mometa.compute import ComputeBlade
help(ComputeBlade)

handle.logout()
