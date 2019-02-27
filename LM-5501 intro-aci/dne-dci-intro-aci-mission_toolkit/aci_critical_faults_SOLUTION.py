#! /usr/bin/env python 
"""
DevNet Express for Data Center Infrastructure
Intro to ACI Programmability Mission

Reporting Critical Faults to Webex Teams

This script will query the APIC for Faults and report
them to Webex Teams.
"""

from acitoolkit.acitoolkit import Session
from acitoolkit import Faults
from credentials import URL, LOGIN, PASSWORD
import requests, json

# MISSION: Provide your Webex Teams token and the Room ID into which to post
token = ""
room_id = ""

fault_count = {"total": 0, "critical": 0}

def post_message(message):
    """
	Simple API Call to Post Message
	"""
    u = "https://api.ciscospark.com/v1/messages"
    headers = {"Content-type": "application/json; charset=utf-8", 
               "Authorization": "Bearer {}".format(token)}
    body = {"roomId": room_id, 
            "markdown": message}
    return requests.post(u, headers=headers, data=json.dumps(body))
	
	
# MISSION: Provide the proper ACI Toolkit code to create a Session 
# object and use it to login to the APIC.  
# NOTE: Variables URL, LOGIN, and PASSWORD were imported from 
#       the credentials file.  
session = Session(URL, LOGIN, PASSWORD)
resp = session.login()
if not resp.ok:
    print('%% Could not login to APIC')
    sys.exit(1)

# MISSION: Create an instance of the toolkit class representing ACI Faults 
#   Hint: the class is called "Faults" and takes no parameters
faults_obj = Faults()

# Monitor the Faults on the APIC 
faults_obj.subscribe_faults(session)
while faults_obj.has_faults(session):
    if faults_obj.has_faults(session):
        faults = faults_obj.get_faults(session)

        if faults is not None:
            for fault in faults:
                message = []
                fault_count["total"] += 1
                if fault is not None and fault.severity in ["critical"]:
                    fault_count["critical"] += 1
                    # MISSION: Each fault object has several properties describing the fault.
                    #          The properties are: type, severity, descr, rule, dn, & domain
                    #          Complete each line below with the correct property.  
                    #          The first two are already complete.  
                    message.append( "****************")
                    message.append( "    Description         : " + fault.descr)
                    message.append( "    Distinguished Name  : " + fault.dn)
                    message.append( "    Rule                : " + fault.rule)
                    message.append( "    Severity            : " + fault.severity)
                    message.append( "    Type                : " + fault.type)
                    message.append( "    Domain              : " + fault.domain)
                    #print("\n".join(message))
                    
                    post_resp = post_to_spark("\n".join(message))
                    if post_resp.status_code != 200: 
                        print("Problem posting message to Webex Teams, check token and room_id")
                        exit(1)
                        
# Print completion message
print("{} Faults were found.\n  {} critical faults reported Webex Teams".format(fault_count["total"], 
                                                                             fault_count["critical"]))
