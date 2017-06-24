## Mission: Programming Cisco Compute - Python Basic and Advanced
## Mission Exercise 2 - Solution

from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("198.18.133.91", "admin", "password")
handle.login()

from ucsmsdk.mometa.compute.ComputePool import ComputePool
from ucsmsdk.mometa.compute.ComputePooledSlot import ComputePooledSlot

mo_pool = ComputePool(parent_mo_or_dn="org-root", name="Python_Heroes_Server_Pool")

handle.add_mo(mo_pool)
handle.commit()

filter_exp = '(name,"Python_Heroes_Server_Pool")'
mo_compute_pool = handle.query_classid("computePool",filter_str=filter_exp)

for slot_num in 1,2,3,4:
   mo_compute_pooled_slot = ComputePooledSlot(parent_mo_or_dn=mo_compute_pool[0].dn, chassis_id="2", slot_id=str(slot_num))
   handle.add_mo(mo_compute_pooled_slot)

handle.commit()

handle.logout()
