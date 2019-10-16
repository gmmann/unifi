import requests
import json
from pprint import pprint
import urllib3
from getpass import getpass
import csv

site_file = './sites.csv'

with open(site_file, 'r') as site_list:
    site_list_read = csv.reader(site_list, delimiter=',')
    site_list.readline()
    for site_list_row in site_list_read:
        controller_host = site_list_row[0]
        user_name = site_list_row[1]
        site_name = site_list_row[2]


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
controller = {"ip": controller_host, "port": "8443"}

# set REST API headers
headers = {"Accept": "application/json",
           "Content-Type": "application/json"}
# set URL parameters
loginUrl = 'api/login'
url = f"https://{controller['ip']}:{controller['port']}/{loginUrl}"
# get password
pass_word = getpass('What is the password?                     : ')

body = {
    "username": user_name,
    "password": pass_word
}
# Open a session for capturing cookies
session = requests.Session()
# login
response = session.post(url, headers=headers,
                        data=json.dumps(body), verify=False)

# parse response data into a Python object
api_data = response.json()
# print("/" * 50)
# pprint(api_data)
# print('Logged in!')
# print("/" * 50)

# Set up to get site name
getSitesUrl = 'api/self/sites'
url = f"https://{controller['ip']}:{controller['port']}/{getSitesUrl}"
response = session.get(url, headers=headers,
                       verify=False)
api_data = response.json()
# print("/" * 50)
# print("/" * 50)

# Parse out the resulting list of info
responseList = api_data['data']
n = 'name'
for items in responseList:
    if items.get('desc') == site_name:
        n = items.get('name')

getDevicesUrl = f"api/s/{n}/stat/device"
url = f"https://{controller['ip']}:{controller['port']}/{getDevicesUrl}"
response = session.get(url, headers=headers,
                       verify=False)
api_data = response.json()
responseList = api_data['data']
print('DEVICE LIST AND STATUS')
for device in responseList:
    print(f"The device {device['name']} has IP {device['ip']}")
    print(f"MAC:            {device['mac']}")
    print(f"DHCP?:          {device['config_network']['type']}")
    if device['state'] == 1:
        print('State:          online')
    else:
        print('State:          offline')
    print(f"Upgradable?     {device['upgradable']}")
    print(' ')



print(api_data)
