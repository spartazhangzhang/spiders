# coding:utf-8
import pprint
from utils.Downloader import Downloader
url  = "http://www.douban.com"
urls = ["http://www.douban.com","http://www.baidu.com","http://www.taobao.com"]
# rep = WebRequests.get_page(url)
# print(rep)
downloader = Downloader(urls)
pprint.pprint(len(downloader.htmls))
pprint.pprint(downloader.htmls)

