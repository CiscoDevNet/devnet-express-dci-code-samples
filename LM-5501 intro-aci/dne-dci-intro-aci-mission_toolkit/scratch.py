"""
Simple application that logs on to the APIC and displays all
of the faults on all the Tenants.
If a particular tenant is given, shows all the faults of that tenant
and cotinuously keeps logging the faults.
"""

import acitoolkit as ACI
from acitoolkit import Faults
from credentials import *
import requests, json

spark_token = ""
spark_room_id = ""

def post_to_spark(message): 
    """
	Simple API Call to Post Message to Spark
	"""
    u = "https://api.ciscospark.com/v1/messages"
    headers = {"Content-type": "application/json; charset=utf-8", 
               "Authorization": "Bearer {}".format(spark_token)}
    body = {"roomId": spark_room_id, 
            "markdown": message}
    return requests.post(u, headers=headers, data=json.dumps(body))
	
	

def main():
    """
    Main execution routine
    """

    # Login to APIC
    session = ACI.Session(URL, LOGIN, PASSWORD)
    resp = session.login()
    if not resp.ok:
        print('%% Could not login to APIC')
        return
    
    tenant_name = None

    faults_obj = Faults()
    faults_obj.subscribe_faults(session)
    while faults_obj.has_faults(session):
        if faults_obj.has_faults(session):
            faults = faults_obj.get_faults(session, tenant_name=tenant_name)
            if faults is not None:
                for fault in faults:
                    message = []
                    if fault is not None and fault.severity in ["critical", "major"]:
                        message.append( "****************")
                        if fault.descr is not None:
                            message.append( "     descr     : " + fault.descr)
                        else:
                            message.append( "     descr     : " + "  ")
                        message.append( "     dn        : " + fault.dn)
                        message.append( "     rule      : " + fault.rule)
                        message.append( "     severity  : " + fault.severity)
                        message.append( "     type      : " + fault.type)
                        message.append( "     domain    : " + fault.domain)
                        #print("\n".join(message))
                        post_to_spark("\n".join(message))


if __name__ == '__main__':
    main()
