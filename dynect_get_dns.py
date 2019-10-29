import requests
import json
from pprint import pprint
import urllib3
from getpass import getpass
from getpass import getuser

import csv

# domain_file = './domains.csv'

# with open(domain_file, 'r') as domain_list:
#     domain_list_read = csv.reader(domain_list, delimiter=',')
#     domain_list.readline()
#     for domain_list_row in domain_list_read:
#         controller_host = domain_list_row[0]
#         user_name = domain_list_row[1]
#         site_name = domain_list_row[2]
# # # https://api.dynect.net/REST/Session/?customer_name=axedacorp&user_name=hostingadmin&password=4ug0S!r3et
# # # {
# # #     "status": "success",
# # #     "data": {
# # #         "token": "AdOm9beMVoxfxV6P5RDNEBCFX8MNyOKcwXvHqeZkTx/UDlkXwRHCFpYZl4t5aLShwqC0szI49/nP4t1ChFqPWctCilzWrmTISZBznZ1QP0ptGr1bSYtL5z3w5PnKPn5PCVXYs4WbgcDuqBK7yzubGZ9RgCWE18fxg54oB+OnZH0=",
# # #         "version": "3.7.15"
# # #     },
# # #     "job_id": 2486289394,
# # #     "msgs": [
# # #         {
# # #             "INFO": "login: Login successful",
# # #             "SOURCE": "BLL",
# # #             "ERR_CD": null,
# # #             "LVL": "INFO"
# # #         }
# # #     ]
# # # }





urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
# dynect_api = {"ip": dynect_api_host, "port": "443"}

# set REST API headers
headers = {"Accept": "application/json",
           "Content-Type": "application/json"}
# set URL parameters
# loginUrl = 'api/login'
url_domain = 'api.dynect.net'
url_uri    = 'REST/Session/'
url = f"https://{url_domain}:/{url_uri}"
# get password
# customer_name = input('What is the customer name                 : ')
# user_name     = input('What is the user     name                 : ')
customer_name = 'axedacorp'
try:
    user_name     = 'hostingadmin'
    # user_name     = 'gmann@ptc.com'
except:
    print('ERROR', error)

try: 
    pass_word     = '4ug0S!r3et'
    # pass_word     = getpass('What is the password?                     : ')
except:
    print('ERROR', error)

body = {
    "customer_name" : customer_name,
    "user_name": user_name,
    "password": pass_word
}
# print(customer_name)
# print(user_name)
# print(pass_word)
# print(url)

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
# pprint(api_data)
try:

data_data = api_data['data']
token_id = data_data['token']
print(token_id)









# # # # # Set up to get site name
# # # # getSitesUrl = 'api/self/sites'
# # # # url = f"https://{controller['ip']}:{controller['port']}/{getSitesUrl}"
# # # # response = session.get(url, headers=headers,
# # # #                        verify=False)
# # # # api_data = response.json()
# # # # # print("/" * 50)
# # # # # print("/" * 50)

# # # # # Parse out the resulting list of info
# # # # responseList = api_data['data']
# # # # # site_parse = responseList['data'][]
# # # # # print(responseList{'desc'})
# # # # n = 'name'
# # # # for items in responseList:
# # # #     if items.get('desc') == site_name:
# # # #         n = items.get('name')

# # # # getDevicesUrl = f"api/s/{n}/stat/device"
# # # # url = f"https://{controller['ip']}:{controller['port']}/{getDevicesUrl}"
# # # # response = session.get(url, headers=headers,
# # # #                        verify=False)
# # # # api_data = response.json()
# # # # responseList = api_data['data']
# # # # device_output_file = './device_status_report.txt'

# # # # write_config_file = open(device_output_file,'a+')
# # # # print('DEVICE LIST AND STATUS')
# # # # write_config_file.writelines('DEVICE LIST AND STATUS \n')
# # # # print(site_name)
# # # # write_config_file.writelines(f"{site_name} \n")


# # # # #grouping



# # # # for device in responseList:
# # # #     # write_config_file = open(device_output_file,'a+')
# # # #     print(f"The device {device['name']} has IP {device['ip']}")
# # # #     print(f"MAC:            {device['mac']}")
# # # #     print(f"DHCP?:          {device['config_network']['type']}")
# # # #     write_config_file.writelines(f"The device {device['name']} has IP {device['ip']} \n")
# # # #     write_config_file.writelines(f"MAC:            {device['mac']} \n")
# # # #     write_config_file.writelines(f"DHCP?:          {device['config_network']['type']} \n")
# # # #     if device['state'] == 1:
# # # #         print('State:          online')
# # # #         write_config_file.writelines('State:          online \n')
# # # #     else:
# # # #         print('State:          offline \n')
# # # #         write_config_file.writelines('State:          offline \n')
# # # #     print(f"Upgradable?     {device['upgradable']}")
# # # #     print(' ')
# # # #     write_config_file.writelines(f"Upgradable?     {device['upgradable']} \n")
# # # #     write_config_file.writelines(' ')


# # # # print()
# # # # print()
# # # # print()
# # # # print()
# # # # print('========================================================================================')
# # # # print('========================================================================================')
# # # # print('========================================================================================')
# # # # print('========================================================================================')
# # # # print('========================================================================================')
# # # # print()
# # # # print()
# # # # print()
# # # # print()


# # # # # print(api_data)


# # # # getClientsUrl = f"api/s/{n}/stat/sta"
# # # # url = f"https://{controller['ip']}:{controller['port']}/{getClientsUrl}"
# # # # response = session.get(url, headers=headers,
# # # #                        verify=False)
# # # # api_data = response.json()
# # # # responseList = api_data['data']
# # # # print('CLIENT LIST AND STATUS')
# # # # # print(api_data)

# # # # client_output_file = './client_status_report.txt'
# # # # for client in responseList:
# # # #     write_config_file = open(client_output_file,'a+')
# # # #     wired_wireless = {client['is_wired']}
# # # #     # print(wired_wireless)
# # # #     if True in wired_wireless:
# # # #         conn_type = 'Wired'
# # # #         # print(f"{client['name']} client MAC Address of {client['mac']} is {conn_type} ")
# # # #     else:
# # # #         conn_type = 'Wireless'
# # # #     print(f"{client['name']} client MAC Address of {client['mac']} is {conn_type} ")
# # # #     write_config_file.writelines(f"{client['name']} client MAC Address of {client['mac']} is {conn_type} \n")

# # # #     # print(f"The client {client['name']} has IP {client['ip']} and MAC Address of {client['mac']} ")
# # # #     # print(f"MAC:            " )
# # # #     # print(f"DHCP?:          {client['config_network']['type']}")
# # # #     # if client['state'] == 1:
# # # #     #     print('State:          online')
# # # #     # else:
# # # #     #     print('State:          offline')
# # # #     # print(f"Upgradable?     {device['upgradable']}")
# # # #     # print(' ')
# # # # print('========================================================================================')
# # # # print('========================================================================================')
# # # # print('========================================================================================')
# # # # print('========================================================================================')
# # # # print('========================================================================================')



