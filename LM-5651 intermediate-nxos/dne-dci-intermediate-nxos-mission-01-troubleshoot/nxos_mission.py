# Import necessary modules
import requests
import json
import os
from ciscosparkapi import CiscoSparkAPI

ROOM_NAME = "" # MISSION: Paste room name here
ACCESS_TOKEN = "" # MISSION: Paste your access token here

if not ROOM_NAME or not ACCESS_TOKEN:
    exit("Looks like ROOM_NAME and/or ACCESS_TOKEN variables are empty.\n"\
         "If you are attending a DevNetExpress Event obtain the room name from your instructor "\
         " and populate the ROOM_NAME variable.\n"\
         "To obtain your access token visit https://developer.ciscospark.com and assign it to ACCESS_TOKEN variable.")

api = CiscoSparkAPI(access_token=ACCESS_TOKEN)
all_rooms = api.rooms.list()
ROOM_ID =[rm.id for rm in all_rooms if ROOM_NAME in rm.title]

if len(ROOM_ID) < 1:
    exit("Provided room name either does not exists or has a typo in it.\n"\
         "Please check room name and then re-run the script.\n")


# Defining global parameters
NX_IP = "" # MISSION: Set the value to the Nexus's IP address
URL = "http://%s/ins" % NX_IP

USERNAME = "" # MISSION: Provide the username information
PASS = "" # MISSION: Provide password associated with username above


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
    payload = None

    if "jsonrpc" in payload[0] and payload[0]["params"]["cmd"] == cmd:
        return payload
    else:
        exit("MISSION: Obtain payload structure from NX-API Developer Sandbox"\
             "and assign it to the payload variable")

CMD = "" # MISSION: Provide CLI command to retrieve the MAC addresses table
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
    mission_msg = ""
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
                mission_msg += "\n##**-=INTEFACE %s STATISTICS=-**" % iface.upper()
                mission_msg += "\n    Administrative State: " + str(iface_stats["admin_state"])
                mission_msg += "\n    Interface State: "+ str(iface_stats["state"])
                mission_msg += "\n    Burned-in MAC Address: "+ str(iface_stats["eth_bia_addr"])
                mission_msg += "\n    MTU: " + str(iface_stats["eth_mtu"])
                mission_msg += "\n    Interface Mode: " + str(iface_stats["eth_mode"])
                mission_msg += "\n    Last Flap: " + str(iface_stats["eth_link_flapped"])
                mission_msg += "\n    Last Clearing: " + str(iface_stats["eth_clear_counters"])
                mission_msg += "\n    RX Information"
                mission_msg += "\n        Unicast Packets: " + str(iface_stats["eth_inucast"])
                mission_msg += "\n        Multicast Packets: " + str(iface_stats["eth_inmcast"])
                mission_msg += "\n        CRC: " + str(iface_stats["eth_crc"])
                mission_msg += "\n        Input Error: " + str(iface_stats["eth_inerr"])
                mission_msg += "\n        Ignored: " + str(iface_stats["eth_ignored"])
                mission_msg += "\n        Drop due to Interface Down: " + str(iface_stats["eth_in_ifdown_drops"])
                mission_msg += "\n    TX Information"
                mission_msg += "\n        Unicast Packets: " + str(iface_stats["eth_outucast"])
                mission_msg += "\n        Multicast Packets: " + str(iface_stats["eth_outmcast"])
                mission_msg += "\n        Jumbo Packets: " + str(iface_stats["eth_jumbo_outpkts"])
                mission_msg += "\n        Output Error: " + str(iface_stats["eth_outerr"])
                mission_msg += "\n        Collision: " + str(iface_stats["eth_coll"])
                mission_msg += "\n        Output Discard: " + str(iface_stats["eth_outdiscard"])
        break
    else:
        input("Sorry the number you have entered is not valid. Press Enter to try again!")
try:
    api.messages.create(ROOM_ID[0], markdown=mission_msg)
    print("You successfully completed the mission. Check the Spark Room\n\n\n")
    print(mission_msg)
except:
    print("Something went wrong while posting the message in the Spark Room!")