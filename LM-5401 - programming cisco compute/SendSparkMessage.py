import json
import sys
import requests

spark_api_token = 'YOUR TOKEN'
spark_room_name = 'YOUR EVENT ROOM NAME'
spark_message = 'YOUR MESSAGE'
#spark_message = 'I have completed the Programming Cisco Compute - Python Mission'

if spark_api_token == 'YOUR TOKEN' or spark_room_name == 'YOUR EVENT ROOM NAME' or spark_message == 'YOUR MESSAGE':
    print('Make the updates to the Spark variables')
    quit()

spark_messages_resource = '/messages'
spark_rooms_resource = '/rooms'
spark_uri_v1 = 'https://api.ciscospark.com/v1'

spark_headers = {'Authorization':'Bearer ' + spark_api_token, 'Content-Type':'application/json', 'Accept':'application/json'}

resp = requests.get(spark_uri_v1 + spark_rooms_resource, headers=spark_headers)
resp = resp.json()

for room in resp["items"]:
     if room["title"] == spark_room_name:
             spark_room_id = room["id"]

spark_msg_json = {"roomId": spark_room_id, "text": spark_message}
resp = requests.post(spark_uri_v1 + spark_messages_resource, json=spark_msg_json, headers=spark_headers)
