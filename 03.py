# coding:utf-8
from utils.WebRequests import get_page

url = "https://www.tianyancha.com/search/p2?key=longyuan"

rep = get_page(url)
print(rep)


