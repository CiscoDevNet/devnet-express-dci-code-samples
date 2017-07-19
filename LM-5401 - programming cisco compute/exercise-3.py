## The UCS Python SDK Makes Deploying Servers a Breeze
## Exercise 3

# Get a handle and login to UCS Manager
from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("198.18.133.91", "admin", "password")
handle.login()

# Query the computeBlade Class
blades = handle.query_classid("computeBlade")

# Print computeBlade object attributes
for blade in blades:
    print(blade.dn, blade.total_memory, blade.num_of_cpus, blade.serial)

# Print out the computeBlade child object equipmentLocatorLed Class attribute oper_state
for blade in blades:
    leds = handle.query_children(in_dn=blade.dn, class_id="equipmentLocatorLed")
    for led in leds:
        print(blade.dn, led.oper_state)

# Logout of the UCS Manager  
handle.logout()
