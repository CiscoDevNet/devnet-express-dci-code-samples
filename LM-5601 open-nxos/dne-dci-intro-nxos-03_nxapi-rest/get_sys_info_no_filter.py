import requests


# Assign requests.Session instance to session variable
session = requests.Session()

# Define URL and PAYLOAD variables
URL = "http://198.18.134.140/api/aaaLogin.json"
PAYLOAD = {
          "aaaUser": {
            "attributes": {
              "name": "admin",
              "pwd": "C1sco12345"
               }
            }
          }

# Obtain an authentication cookie
session.post(URL,json=PAYLOAD)

# Define SYS_URL variable
SYS_URL = "http://198.18.134.140/api/mo/sys.json"

# Obtain system information by making session.get call
# then convert it to JSON format then filter to system attributes
sys_info = session.get(SYS_URL).json()

# Print raw data

print(sys_info)