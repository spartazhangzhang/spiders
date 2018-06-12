# coding:utf-8
import requests,pprint

url = "http://www.baidu.com"

rep = requests.get(url)
pprint.pprint(rep.content.decode('utf-8'))