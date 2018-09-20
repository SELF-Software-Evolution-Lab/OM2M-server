import requests
import json

# this code reads the last value of the DATA container of the Temp_casa app
# enter username
username = ""
# enter password
password = ""
header = {"X-M2M-Origin": username+":"+password, "Accept": "application/json"}
base_url = "http://13.58.183.185:80/~"
# you should change the device variable depending which data do you want to read.
device = "/in-cse/in-name/Temp_casa/DATA/la"
url_om2m = base_url + device

rec_server = requests.get(url_om2m, headers=header)
rec_server_dic = json.loads(rec_server.content)

print(rec_server_dic)