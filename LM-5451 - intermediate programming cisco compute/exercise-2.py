## More Powerful Cisco Compute Python Scripts with UCS Python SDK
## Exercise 2

# Add Vlans in a transaction
from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

handle = UcsHandle("198.18.133.91", "admin", "C1sco12345")
handle.login()

fabric_lan_cloud = handle.query_classid("FabricLanCloud")

vlan_ids = ['300','301','302','303','304','305']

for vlan_id in vlan_ids:

    add_vlan = FabricVlan(parent_mo_or_dn=fabric_lan_cloud[0], name="vlan" + vlan_id, id=vlan_id)
    handle.add_mo(add_vlan)

handle.commit()
handle.logout()

input("Vlans Added - Press Enter to Continue to Set Vlans...")

# Set Vlans is a transaction
from ucsmsdk.ucshandle import UcsHandle

handle = UcsHandle("198.18.133.91", "admin", "C1sco12345")
handle.login()

vlan_ids = ['300','301','302','303','304','305']

for vlan_id in vlan_ids:
   set_vlan = handle.query_dn("fabric/lan/net-vlan" + vlan_id)
   set_vlan.sharing = "community"
   handle.set_mo(set_vlan)

handle.commit()
handle.logout()

input("Vlans Set - Press Enter to Continue to Set Vlans more efficiently...")

# Set Vlans more efficiently in a transaction
from ucsmsdk.ucshandle import UcsHandle

handle = UcsHandle("198.18.133.91", "admin", "C1sco12345")
handle.login()

fabric_vlans = handle.query_classid("FabricVLan")

vlan_ids = ['300','301','303','304','305']

for fabric_vlan in fabric_vlans:

    if fabric_vlan.id in vlan_ids and fabric_vlan.name == "vlan" + fabric_vlan.id:
        fabric_vlan.sharing = "none"
        handle.set_mo(fabric_vlan)

handle.commit()
handle.logout()

input("Vlans Set more efficiently - Press Enter to Continue to Remove Vlans...")

# Remove Vlans in a transaction
from ucsmsdk.ucshandle import UcsHandle

handle = UcsHandle("198.18.133.91", "admin", "C1sco12345")
handle.login()

fabric_vlans = handle.query_classid("FabricVLan")

vlan_ids = ['300','301','302','303','304','305']

for fabric_vlan in fabric_vlans:

  if fabric_vlan.id in vlan_ids and fabric_vlan.name == "vlan" + fabric_vlan.id:
      handle.remove_mo(fabric_vlan)

handle.commit()
handle.logout()
