#coding = utf-8
import urllib
from urllib import request
import re
import requests
from selenium import webdriver
import selenium
import time
import os



# Chrome_login = webdriver.Chrome()
chromedriver = r"C:\Users\*\AppData\Local\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
# add_path = '*'


def rreplace(self, old, new, *max):
    count = len(self)
    if max and str(max[0]).isdigit():
        count = max[0]
        return new.join(self.rsplit(old, count))


def getHTMLText(url):
    try:
        response = requests.get(url, timeout = 30)
        response.raise_for_status()
        response.encoding = 'utf-8'
        return response.text
    except:
        return ''



def main():
    url = '*'
    words = input('搜索名称：')
    deeps = int(input('查询页数：'))
    nums = deeps + 1
    words_d = urllib.parse.quote(words, safe='/', encoding='gb2312', errors=None)
    print('-' * 30)
    for i in range(nums):
        print(i)
        f = url + words_d + "/normal/" + str(i)
        print(f)
        html = getHTMLText(url + words_d + "/normal/" + str(i))
        # re_title = re.compile(r'<a  href="/dict/detail/index/(.*?)</a>', re.S)
        re_download = '<div class="dict_dl_btn"><a href="(.*?)"></a></div>'
        # raw_title = re.findall(re_title, html)
        raw_download = re.findall(re_download, html)
        #print(len(raw_download))
        for i in range(len(raw_download)):
            print(i)
            url0 = raw_download[i]
            url1 = 'https:' + str(url0)
            # n = url0.rsplit('=',1)[1]
            print(url0)
            driver.refresh()
            driver.get(url1)
            time.sleep(5)
            # with open(add_path + '/' + n + '.scel',"a") as code:
            #     code.write(f)




if __name__ == '__main__':
    main()
