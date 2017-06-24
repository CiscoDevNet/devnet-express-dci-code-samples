## The UCS Python SDK Makes Deploying Servers a Breeze
## Exercise 4

# Get a handle and login to UCS Manager
from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("198.18.133.91", "admin", "password")
handle.login()

# Query for compute blades that are not associated
blades = handle.query_classid("computeBlade")
for blade in blades:
    if blade.association == "none":
        print(blade.dn, blade.association)

# Create the Python_Heroes Organization
from ucsmsdk.mometa.org.OrgOrg import OrgOrg
root_org = handle.query_dn("org-root")
mo_org = OrgOrg(parent_mo_or_dn=root_org,name="Python_Heroes")
handle.add_mo(mo_org, modify_present=True)
handle.commit()

# Create the CommanderCode_Python_Server Service Profile
from ucsmsdk.mometa.ls.LsServer import LsServer
sp_org = handle.query_dn("org-root/org-Python_Heroes")
mo_sp = LsServer(parent_mo_or_dn=sp_org,name="CommanderCode_Python_Server")
handle.add_mo(mo_sp, modify_present=True)
handle.commit()

# Add a MAC block to the default MAC Pool
from ucsmsdk.mometa.macpool.MacpoolBlock import MacpoolBlock
mac_pool_default = handle.query_dn("org-root/mac-pool-default")
mo_mac_pool_block = MacpoolBlock(parent_mo_or_dn=mac_pool_default,r_from="00:25:B5:00:00:AA",to="00:25:B5:00:00:D9")
handle.add_mo(mo_mac_pool_block, modify_present=True)
handle.commit()

# Associate the CommanderCode_Python_Server Service Profile to a blade
service_profiles = handle.query_classid("lsServer")
for service_profile in service_profiles:
   if service_profile.name == "CommanderCode_Python_Server":
       print(service_profile.dn, service_profile.name)
       mo_sp = service_profile
       break

from ucsmsdk.mometa.ls.LsBinding import LsBinding
mo_ls_binding = LsBinding(parent_mo_or_dn=mo_sp,pn_dn="sys/chassis-1/blade-2")
handle.add_mo(mo_ls_binding, modify_present=True)
handle.commit()

# Query the Service Profile and the blade
service_profile = handle.query_dn("org-root/org-Python_Heroes/ls-CommanderCode_Python_Server")
print(service_profile.name, service_profile.assign_state, service_profile.assoc_state)

blade = handle.query_dn("sys/chassis-1/blade-2")
print(blade.dn, blade.assigned_to_dn)

# Logout of the UCS Manager
handle.logout()
