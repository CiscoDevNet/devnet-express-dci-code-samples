#! /usr/bin/env python
"""
DevNet Express for Data Center Infrastructure
Intermediate ACI Programmability Mission

Building a tenant application with WebArya

This script will query the APIC to verify that the
new tenant application was created.
"""

from acitoolkit.acitoolkit import Session
from acitoolkit import Tenant, AppProfile
from credentials import URL, LOGIN, PASSWORD
import requests, json, sys

# MISSION: Provide your Token and the Room ID into which to post
#          You can get it from https://developer.webex.com
#          The RoomId should have been provided by the instructors
access_token = ""
webex_teams_room_id = ""

if access_token == "" or webex_teams_room_id == "":
    print("\nPlease edit the file and provide your token and room id\n")
    sys.exit(1)

# What to look for?
mission_tenant = "SnV"
mission_anp = "Evolution_X"
success_message = "I completed the WebArya Mission and added Application {} to Tenant {}!".format(mission_anp, mission_tenant)

def post_to_webex_teams(message):
    """
	Simple API Call to Post Message to Webex Teams
	"""
    u = "https://api.ciscospark.com/v1/messages"
    headers = {"Content-type": "application/json; charset=utf-8",
               "Authorization": "Bearer {}".format(access_token)}
    body = {"roomId": webex_teams_room_id,
            "markdown": message}
    return requests.post(u, headers=headers, data=json.dumps(body))

session = Session(URL, LOGIN, PASSWORD)
resp = session.login()
if not resp.ok:
    print('%% Could not login to APIC')
    sys.exit(1)

# Query for ACI Tenants
tenants = Tenant.get(session)
for tenant in tenants:
    # Search for Mission Tenant
    if tenant.name == mission_tenant:
        # Get Apps in Tenant
        apps = AppProfile.get(session, tenant)
        for app in apps:
            # Search for mission app
            if app.name == mission_anp:
                print("Success!  Well done, we have let everyone know in Webex Teams!")
                post_to_webex_teams(success_message)
                sys.exit()

# Tenant and/or App not found, exit
sys.exit("\nMission Failed: Application {} not found in Tenant {}\n".format(mission_anp, mission_tenant))
