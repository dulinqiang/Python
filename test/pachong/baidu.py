import requests
import re
import json
import xlrd
import xlwt
import lxml
from bs4 import BeautifulSoup
# try:
class baidu:
    def __init__(self):
        pass
    def gettitle(self):
        fo = open("C:/Users/Administrator/Desktop/abc.txt", 'w+')
        try:
            res=requests.get(url='http://tieba.com/p/3138733512?see_lz=1&pn=1')
            rule='<div id="post_content\w*" class="d_post_content j_d_post_content ">(.*?)</div>'
                 # '[\u4e00-\u9fa5]*[0-9]*[\u4e00-\u9fa5]+'
            m=BeautifulSoup(res.text,'lxml')
            # for i in m.descendants:
            #     print(i.str)
            print(m.p)
            # for i in m.find_all('p'):
            #     print(i)
            # print(m.p)
            # fo.write(m.text)
            # for i in re.findall(rule,res.text):
            #      print(i)
        except Exception as e:
            print("爬取是出现错误：",e)
        finally:
            fo.close()
t=baidu()
t.gettitle()

# except Exception as e:
#     print(e)
