#! /usr/bin/env python3
# ! -*- coding:utf-8 -*-
##从接口文档自动获取数据，并将json格式的数据解析，写入mysql数据库，每2分钟写一次

import requests
import base64
import json
import pymysql as mdb
import time
import datetime


def get_data():
    url = "www.ywqiao.com"
    port = "9910"
    domain = "http://{url}:{port}".format(url=url, port=port)

    tokenapi = "{domain}/smart/token/get".format(domain=domain)
    deviceapi = "{domain}/smart/status/get".format(domain=domain)
    # print("tokenapi = %s\ndeviceapi = %s" % (tokenapi, deviceapi))

    # print('*' * 10 + "Get Token" + '*' * 10)
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
    # print(token)

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
    return json_data;

def op_data(json_data):
    # 处理json数据
    #result = json_data
    json_to_python = json.loads(json_data)
    result_data = json_to_python['data']
    result_key = list(result_data.keys())
    results = [[] for i in range(len(result_key))]

    for i in range(len(result_key)):
        if result_key[i]=='XSCY10180101TEST0100029' or result_key[i]=='XSCY10180101TEST0100030':
            results[i].append(result_key[i])
            a = datetime.datetime.strptime(result_data[result_key[i]]['T3'], '%Y-%m-%d %H:%M') + datetime.timedelta(
                minutes=-1)
            aa = a.strftime('%Y-%m-%d %H:%M')
            results[i].append(aa)
            results[i].append(result_data[result_key[i]]['T3'])
            results[i].append(result_data[result_key[i]]['C1'] + result_data[result_key[i]]['C2'])
            results[i].append(result_data[result_key[i]]['C3'] + result_data[result_key[i]]['C4'])
            results[i].append(result_data[result_key[i]]['C5'])
            results[i].append(result_data[result_key[i]]['C17'] + result_data[result_key[i]]['C18'])
    print(results)
    return (results)


#插入数据库
def insert_table(results):
    con = mdb.connect('localhost', 'root', '19880511', 'shuichan');
    for i in range(len(results)):
        if results[i] !=[]:
            if results[i][0] == 'XSCY10180101TEST0100029':
                 sheb_id = 1
            else :
                 sheb_id = 2
            sheb_num = results[i][0]
            data_time = results[i][1]
            get_time = results[i][2]
            dis_o = results[i][3]
            ph = results[i][4]
            w_temp = results[i][5]
            turbidity = results[i][6]

            with con:
                cur = con.cursor()
                sql = "INSERT INTO shuichandata(sheb_id, sheb_num, data_time,get_time,dis_o,ph,w_temp,turbidity)" \
                      "VALUES('%s','%s','%s','%s','%s','%s','%s','%s')" % (
                          sheb_id, sheb_num, data_time, get_time, dis_o, ph, w_temp, turbidity)
                cur.execute(sql)

    con.close()

i=0
while True:
    json_data = get_data()
    results = op_data(json_data)
    insert_table(results)
    i=i+1
    print("获取次数:",i)
    time.sleep(120)

# json_data=get_data()
# results=op_data(json_data)
# insert_table(results)

