## Mission: Programming Cisco Compute - Python Basic and Advanced
## Mission Exercise 4 - Solution

# Get a handle and login to UCS Manager
from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("198.18.133.91", "admin", "password")
handle.login()

# Update the User Label on the Service Profile
filter_exp = '(name,"CommanderCode_PY_Mission_Server")'
mo_sp = handle.query_classid("LsServer",filter_str=filter_exp)

mo_sp[0].usr_lbl = "Quantum Calculations Server"

handle.set_mo(mo_sp[0])
handle.commit()

# Delete the Server Pool
filter_exp = '(name,"Python_Heroes_Server_Pool")'
mo_compute_pool = handle.query_classid("ComputePool",filter_str=filter_exp)
handle.remove_mo(mo_compute_pool[0])
handle.commit()

# Dis-Associate the Serivce Profile from the assigned Server
filter_exp = '(name,"CommanderCode_PY_Mission_Server")'
mo_sp = handle.query_classid("LsServer",filter_str=filter_exp)
mo_ls_requirement = handle.query_children(in_mo=mo_sp[0],class_id="LsRequirement")
handle.remove_mo(mo_ls_requirement[0])
handle.commit()

# Logout of the UCS Manager
handle.logout()
