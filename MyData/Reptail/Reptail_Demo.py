#encoding:utf8
import requests


r = requests.get('https://unsplash.com') #像目标url地址发送get请求，返回一个response对象
print(r.text) #r.text是http response的网页HTML