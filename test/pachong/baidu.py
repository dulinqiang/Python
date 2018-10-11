import requests
import re
import json
# try:
class baidu:
    def __init__(self):
        pass
    def gettitle(self):
        try:
            res=requests.get(url='http://tieba.baidu.com/p/3138733512?see_lz=1&pn=1')
            rule='<a.*?>(.*?)</a>'
            # print(res.text)
            for i in re.findall(rule,res.text):
                 print(i)
        except Exception as e:
            print("爬取是出现错误：",e)
t=baidu()
t.gettitle()

# except Exception as e:
#     print(e)
