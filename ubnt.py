import requests
import json
from pprint import pprint
import urllib3
from getpass import getpass
import csv


read_controller_creds = csv.reader('sites.csv')
print(read_controller_creds)

#For now just change the values here for your controller, username and site name
gate_way = '192.168.69.9'
user_name = 'george.m.mann@gmail.com'
site_name = '35 Thomas Farm circle'



urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# set up connection parameters in a dictionary
# gate_way = input('What is the ip address of the controller? : ')
# gate_way = '192.168.69.9'
gateway = {"ip": gate_way, "port": "8443"}

# set REST API headers
headers = {"Accept": "application/json",
           "Content-Type": "application/json"}
# set URL parameters
loginUrl = 'api/login'
url = f"https://{gateway['ip']}:{gateway['port']}/{loginUrl}"
# set username and password
# user_name = input('What is the username?                     : ')
# pass_word = input('What is the password?                     : ')
# site_name = input('What is the site name?                    : ')

# user_name = 'george.m.mann@gmail.com'
# pass_word = input('What is the password?                     : ')
pass_word = getpass('What is the password?                     : ')
# site_name = '35 Thomas Farm circle'

# print(user_name)
# print(pass_word)
# print(gate_way)
# print(url)
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
url = f"https://{gateway['ip']}:{gateway['port']}/{getSitesUrl}"
response = session.get(url, headers=headers,
                       verify=False)
api_data = response.json()
# print("/" * 50)
# pprint(api_data)
# print("/" * 50)

# Parse out the resulting list of
responseList = api_data['data']
# pprint(responseList)
n = 'name'
for items in responseList:
    if items.get('desc') == site_name:
        n = items.get('name')
# print(n)

getDevicesUrl = f"api/s/{n}/stat/device"
url = f"https://{gateway['ip']}:{gateway['port']}/{getDevicesUrl}"
response = session.get(url, headers=headers,
                       verify=False)
api_data = response.json()
responseList = api_data['data']
# pprint(responseList)
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
