# 以前这个接口可以查锁关注的关注列表
import re
from time import sleep

import bs4  # 导入BeautifulSoup
import requests  # 导入requests库

print("请输入要查询关注的uid:")
uid = input()
url = 'https://account.bilibili.com/api/member/getCardByMid?mid=' + str(uid)
request = requests.get(url)
gz = re.findall(r'[\[](.*?)[]]', request.text)
gz2 = re.findall(r'\w+', str(gz))
yingbi = re.findall(r'"coins":[0-9]+.[0-9]', request.text)
fensi = re.findall(r'"fans":[0-9]+', request.text)
# friend=re.findall(r'"friend":[0-9]+', request.text)

# uid = [388124521,235555226,37090048]

for n in gz2:
    url = "https://space.bilibili.com/" + str(n) + "/bangumi"
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate,br',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    request = requests.get(url)
    # print(request)
    # print(request.text)
    soup = bs4.BeautifulSoup(request.text, "html.parser")
    # print(soup.title.text)
    # print(soup.select('title'))
    print(re.findall(r".+(?=的)", soup.title.text))
    guanzhu = re.findall(r".+(?=的)", soup.title.text)
    with open("guanzhu.txt", "a", encoding='utf8') as f:
        f.write(str(guanzhu) + '\n')
    sleep(0.3)
with open("guanzhu.txt", "a", encoding='utf8') as f:
    f.write(yingbi[0] + '\n')
    f.write(fensi[0] + '\n')
# print(friend)
