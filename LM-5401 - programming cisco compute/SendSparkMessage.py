import json
import sys
import requests

webex_teams_api_token = 'YOUR TOKEN'
webex_teams_room_name = 'YOUR EVENT ROOM NAME'
webex_teams_message = 'YOUR MESSAGE'
#webex_teams_message = 'I have completed the Programming Cisco Compute - Python Mission'

if webex_teams_api_token == 'YOUR TOKEN' or webex_teams_room_name == 'YOUR EVENT ROOM NAME' or webex_teams_message == 'YOUR MESSAGE':
    print('Make the updates to the Webex Teams variables')
    quit()

webex_teams_messages_resource = '/messages'
webex_teams_rooms_resource = '/rooms'
webex_teams_uri_v1 = 'https://api.ciscospark.com/v1'

webex_teams_headers = {'Authorization':'Bearer ' + webex_teams_api_token, 'Content-Type':'application/json', 'Accept':'application/json'}

resp = requests.get(webex_teams_uri_v1 + webex_teams_rooms_resource, headers=webex_teams_headers)
resp = resp.json()

for room in resp["items"]:
     if room["title"] == webex_teams_room_name:
             room_id = room["id"]

webex_teams_msg_json = {"roomId": room_id, "text": webex_teams_message}
resp = requests.post(webex_teams_uri_v1 + webex_teams_messages_resource, json=webex_teams_msg_json, headers=webex_teams_headers)

resp = resp.json()
print(resp)
