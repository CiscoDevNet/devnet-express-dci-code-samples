import json
import sys
import requests

api_token = 'NDlkYWIzNTktZjE5MS00MDRlLWJkN2ItYjdmMjNiYzU1NDVmZGZhZjc2NDktNTc3'
room_name = 'NetDevOps CICD Bot'
#message = 'YOUR MESSAGE'
message = 'I have completed the Programming Cisco Compute - Python Mission'

if (api_token == 'YOUR TOKEN' or
    room_name == 'YOUR EVENT ROOM NAME' or
    message == 'YOUR MESSAGE'):
    print('Make the updates to the Webex Teams variables')
    quit()

messages_resource = '/messages'
rooms_resource = '/rooms?max=1000'
uri_v1 = 'https://api.ciscospark.com/v1'

http_headers = {'Authorization':'Bearer ' + api_token, 'Content-Type':'application/json', 'Accept':'application/json'}

resp = requests.get(uri_v1 + rooms_resource, headers=http_headers)
resp = resp.json()
if "errors" in resp:
   print(resp)
for room in resp["items"]:
     if room["title"] == room_name:
             room_id = room["id"]

msg_json = {"roomId": room_id, "text": message}
resp = requests.post(uri_v1 + messages_resource, json=msg_json, headers=http_headers)

resp = resp.json()
print(resp)
