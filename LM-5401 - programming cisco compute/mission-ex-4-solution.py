## Mission: Programming Cisco Compute - Python Basic and Advanced
## Mission Exercise 4 - Solution

from ucsmsdk.ucshandle import UcsHandle
handle = UcsHandle("198.18.133.91", "admin", "password")
handle.login()

filter_exp = '(name,"CommanderCode_PY_Mission_Server")'
filter_exp = '(name,"CommanderCode_PY_Mission_Server")'

filter_exp = '(name,"CommanderCode_PY_Mission_Server")'
mo_sp = handle.query_classid("LsServer",filter_str=filter_exp)

mo_sp[0].usr_lbl = "Quantum Calculations Server"

handle.set_mo(mo_sp[0])
handle.commit()

filter_exp = '(name,"Python_Heroes_Server_Pool")'
mo_compute_pool = handle.query_classid("ComputePool",filter_str=filter_exp)
handle.remove_mo(mo_compute_pool[0])
handle.commit()

filter_exp = '(name,"CommanderCode_PY_Mission_Server")'
mo_sp = handle.query_classid("LsServer",filter_str=filter_exp)
mo_ls_requirement = handle.query_children(in_mo=mo_sp[0],class_id="LsRequirement")
handle.remove_mo(mo_ls_requirement[0])
handle.commit()

handle.logout()
