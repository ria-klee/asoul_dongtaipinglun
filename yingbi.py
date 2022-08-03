# 查某个uid硬币数量
import re

import requests  # 导入requests库

uid = 393396916
url = 'https://account.bilibili.com/api/member/getCardByMid?mid=' + str(uid)
request = requests.get(url)
gz = re.findall(r'[\[](.*?)[]]', request.text)
gz2 = re.findall(r'\w+', str(gz))
yingbi = re.findall(r'"coins":[0-9]+.[0-9]', request.text)
fensi = re.findall(r'"fans":[0-9]+', request.text)
guanzhu = re.findall(r'"friend":[0-9]+', request.text)
print(gz)
print(gz2)
# a=[int(s) for s in str(gz).split(',')]
# print(a)
print(yingbi)
print(fensi)
print(guanzhu)
