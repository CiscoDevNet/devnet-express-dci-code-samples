## More Powerful Cisco Compute Python Scripts with UCS Python SDK
## Exercise 3

# Query Timezone and NTP Server
from ucsmsdk.ucshandle import UcsHandle

handle = UcsHandle("198.18.133.91", "admin", "C1sco12345")
handle.login()

for object in handle.query_classid("commDateTime"):
    print(object)

for object in handle.query_classid("commDnsProvider"):
print(object)

handle.logout()

# Set Timezone
from ucsmsdk.ucshandle import UcsHandle

handle = UcsHandle("198.18.133.91", "admin", "C1sco12345")
handle.login()

timezone_mo = handle.query_dn("sys/svc-ext/datetime-svc")
timezone_mo.timezone = "America/Panama"

handle.set_mo(timezone_mo)
handle.commit()

handle.logout()

# Add NTP Server
from ucsmsdk.ucshandle import UcsHandle
from ucsmsdk.mometa.comm.CommNtpProvider import CommNtpProvider

handle = UcsHandle("198.18.133.91", "admin", "C1sco12345")
handle.login()

timezone_mo = handle.query_dn("sys/svc-ext/datetime-svc")

ntp_provider_mo = CommNtpProvider(parent_mo_or_dn=timezone_mo, name="198.18.128.3")

handle.add_mo(ntp_provider_mo)

handle.commit()
handle.logout()

input("NTP Server Added - Press Enter to Continue to Remove NTP Server...")

# Delete NTP Server
from ucsmsdk.ucshandle import UcsHandle

handle = UcsHandle("198.18.133.91", "admin", "C1sco12345")
handle.login()

ntp_provider_mo = handle.query_dn("sys/svc-ext/datetime-svc/ntp-198.18.128.3")
handle.remove_mo(ntp_provider_mo)

handle.commit()
handle.logout()
