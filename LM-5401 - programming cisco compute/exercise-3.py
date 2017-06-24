## The UCS Python SDK Makes Deploying Servers a Breeze
## Exercise 3

from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("198.18.133.91", "admin", "password")
handle.login()

blades = handle.query_classid("computeBlade")

for blade in blades:
    print(blade.dn, blade.total_memory, blade.num_of_cpus, blade.serial)

blades = handle.query_classid("computeBlade")

for blade in blades:
    leds = handle.query_children(in_dn=blade.dn, class_id="equipmentLocatorLed")
    for led in leds:
        print(blade.dn, led.oper_state)
   
handle.logout()
