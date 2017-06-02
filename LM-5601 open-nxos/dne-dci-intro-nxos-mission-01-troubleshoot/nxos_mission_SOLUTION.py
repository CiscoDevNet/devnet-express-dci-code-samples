# Import necessary modules
import requests
import json
import os

# Defining global parameters
NX_IP = "198.18.134.140" # MISSION: Set the value to the Nexus's IP address
URL = "http://%s/ins" % NX_IP

USERNAME = "admin" # MISSION: Provide the username information
PASS = "C1sco12345" # MISSION: Provide password associated with username above


HEADERS = {"content-type" : "application/json-rpc"}

def cls():

    try:
        os.system("cls")
    except:
        os.system("clear")

def json_rpc_payload(cmd):
    """
    MISSION: Obtain payload structure from NX-API Developer Sandbox
    and assign to the payload variable
    The "cmd" key should be set to cmd parameter.
    """
    payload = [
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": cmd,
      "version": 1
    },
    "id": 1
  }
]

    if "jsonrpc" in payload[0] and payload[0]["params"]["cmd"] == cmd:
        return payload
    else:
        exit("MISSION: Obtain payload structure from NX-API Developer Sandbox"\
             "and assign it to the payload variable")

CMD = "show mac address-table" # MISSION: Provide CLI command to retrieve the MAC addresses table
PAYLOAD = json_rpc_payload(CMD)

# Checking if all variables were populated
if NX_IP and USERNAME and PASS and CMD:
    response = requests.post(URL, json=PAYLOAD, headers=HEADERS, auth=(USERNAME, PASS))
else:
    exit("Looks like one of the values required to complete this mission is empty.\n"\
    "Please populate NX_IP, USERNAME, PASS and CMD variables with necessary information and re-run the script.")

# If request was successful obtain interesting data and assign it a variable
if response.ok:
    mac_table = response.json()["result"]["body"]["TABLE_mac_address"]["ROW_mac_address"]
else:
    exit("Something went wrong while retrieving the requested information. The returned error is:\n", response.text)

# Create an array of mac address found on the target device
mac_list = {num: mac["disp_mac_addr"] for num, mac in enumerate(mac_table) if "Eth" in mac["disp_port"]}

# In the while loop the user has to choose a valid MAC address number
# Then relevant information will be displayed.
while True:
    cls()
    for num, mac in enumerate(mac_list):
        print(str(num+1)+". "+ mac_list[num])
    user_choice = int(input("\n\nEnter the number of the MAC address to get more information\n>>> "))-1
    if user_choice in mac_list:
        iface = None
        for mac in mac_table:
            if mac["disp_mac_addr"] == mac_list[user_choice]:
                print("MAC Address: ", mac["disp_mac_addr"])
                print("VLAN: ", mac["disp_vlan"])
                print("INTERFACE: ", mac["disp_port"])
                iface = mac["disp_port"]
        if iface:
            CMD = "show interface %s" % iface
            PAYLOAD = json_rpc_payload(CMD)
            response = requests.post(URL, json=PAYLOAD, headers= HEADERS, auth=(USERNAME, PASS))
            if response.ok:
                iface_stats = response.json()["result"]["body"]["TABLE_interface"]["ROW_interface"]
                print("\n-=INTEFACE %s STATISTICS=-" % iface.upper())
                print("\tAdministrative State:", iface_stats["admin_state"])
                print("\tInterface State:", iface_stats["state"])
                print("\tBurned-in MAC Address:", iface_stats["eth_bia_addr"])
                print("\tMTU:", iface_stats["eth_mtu"])
                print("\tInterface Mode:", iface_stats["eth_mode"])
                print("\tLast Flap:", iface_stats["eth_link_flapped"])
                print("\tLast Clearing:", iface_stats["eth_clear_counters"])
                print("\tRX Information")
                print("\t\tUnicast Packets:", iface_stats["eth_inucast"])
                print("\t\tMulticast Packets:", iface_stats["eth_inmcast"])
                print("\t\tCRC:", iface_stats["eth_crc"])
                print("\t\tInput Error:", iface_stats["eth_inerr"])
                print("\t\tIgnored:", iface_stats["eth_ignored"])
                print("\t\tDrop due to Interface Down:", iface_stats["eth_in_ifdown_drops"])
                print("\tTX Information")
                print("\t\tUnicast Packets:", iface_stats["eth_outucast"])
                print("\t\tMulticast Packets:", iface_stats["eth_outmcast"])
                print("\t\tJumbo Packets:", iface_stats["eth_jumbo_outpkts"])
                print("\t\tOutput Error:", iface_stats["eth_outerr"])
                print("\t\tCollision:", iface_stats["eth_coll"])
                print("\t\tOutput Discard:", iface_stats["eth_outdiscard"])
        break
    else:
        input("Sorry the number you have entered is not valid. Press Enter to try again!")
