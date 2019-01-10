#! /usr/bin/env python3
# ! -*- coding:utf-8 -*-
##从接口文档自动获取数据的小程序，李正强友情支持

import requests
import base64
import json

url = "www.ywqiao.com"
port = "9910"
domain = "http://{url}:{port}".format(url=url, port=port)

tokenapi = "{domain}/smart/token/get".format(domain=domain)
deviceapi = "{domain}/smart/status/get".format(domain=domain)
print("tokenapi = %s\ndeviceapi = %s" % (tokenapi, deviceapi))

print('*' * 10 + "Get Token" + '*' * 10)
data = {
    'username': 'szyds',
    'password': 'szyds20180816',
    'client_id': 'szydsapp',
    'client_secret': 'szydssecret',
    'grant_type': 'password'
}
b64 = base64.b64encode(
    "{client_id}:{client_secret}".format(client_id=data['client_id'], client_secret=data['client_secret']).encode())
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
    'Authorization': 'Basic ' + str(b64)[1:],
    'Content-Type': 'application/x-www-form-urlencoded'
}
token = requests.post(url=tokenapi, data=data, headers=header).json()
print(token)

print('*' * 10 + "Get Device Status" + '*' * 10)
authval = token['token_type'].capitalize() + ' ' + token['access_token']
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.96 Safari/537.36',
    'Authorization': authval,
    'Content-Type': 'application/raw'
    }

d = {"devicePid": ["XSCY10180101TEST0100029", "XSCY10180101TEST0100030"],
     "collectCode": ["C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "C11", "C12", "C13", "C14", "C15",
                     "C16", "C17", "C18"]}
encodedjson = json.dumps(d)
device = requests.post(url=deviceapi, data=encodedjson, headers=header).json()
json_data = json.dumps(device, sort_keys=True, indent=4)
print(json_data)
