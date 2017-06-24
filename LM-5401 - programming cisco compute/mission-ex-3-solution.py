## Mission: Programming Cisco Compute - Python Basic and Advanced
## Mission Exercise 3 - Solution

from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("198.18.133.91", "admin", "password")
handle.login()

from ucsmsdk.mometa.macpool.MacpoolBlock import MacpoolBlock
mac_pool_default = handle.query_dn("org-root/mac-pool-default")
mo_mac_pool_block = MacpoolBlock(parent_mo_or_dn=mac_pool_default,r_from="00:25:B5:00:00:AA",to="00:25:B5:00:00:D9")
handle.add_mo(mo_mac_pool_block, modify_present=True)
handle.commit()

from ucsmsdk.mometa.ls.LsServer import LsServer
from ucsmsdk.mometa.ls.LsRequirement import LsRequirement

mo_sp_template = LsServer(parent_mo_or_dn="org-root", type="initial-template", name="CommanderCode_PY_Mission_Templ")

handle.add_mo(mo_sp_template, modify_present=True)
handle.commit()

filter_exp = '(name,"CommanderCode_PY_Mission_Templ")'
mo_sp_templ = handle.query_classid("lsServer",filter_str=filter_exp)

mo_sp_templ_ls_requirement = LsRequirement(parent_mo_or_dn=mo_sp_templ[0].dn, name="Python_Heroes_Server_Pool")
handle.add_mo(mo_sp_templ_ls_requirement, modify_present=True)

mo_sp = LsServer(parent_mo_or_dn="org-root", src_templ_name="CommanderCode_PY_Mission_Templ", name="CommanderCode_PY_Mission_Server")
handle.add_mo(mo_sp, modify_present=True)
handle.commit()

filter_exp = '(name,"Python_Heroes_Server_Pool")'
mo_compute_pool = handle.query_classid("ComputePool",filter_str=filter_exp)
mo_compute_pooled_slots = handle.query_children(in_mo=mo_compute_pool[0], class_id="ComputePooledSlot")
for mo_compute_pooled_slot in mo_compute_pooled_slots:
    print(mo_compute_pooled_slot.poolable_dn, mo_compute_pooled_slot.assigned_to_dn)
handle.logout()
