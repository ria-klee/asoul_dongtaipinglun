# 视频评论和pid爬取，可以用https://www.bilibili.com/h5/comment/sub?oid=[oid]&pageType=1&root=[rpid]直接跳转到指定评论

import os
import re
import time
import urllib.request
from urllib import request

BV = input("请输入BV号:")
BVH = str(BV)
url = 'https://api.bilibili.com/x/web-interface/view?bvid=' + BVH
req = request.Request(url)
page = request.urlopen(req).read()
page = page.decode('utf-8')
string = page
aidnum = re.findall('"aid":([0-9]*)', string, flags=0)
av = int(aidnum[0])

Folderpath = os.getcwd()  # 获取当前路径
time.sleep(2)  # 等待两秒
comment_list = []  # 创建空列表
zong = 0

for i in range(1):  # 动态下面的评论总共有30页，一页30-100评论左右，往大了填就行
    url = 'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn=' + str(
        i
    ) + '&type=1&oid=' + str(
        av
    ) + '&sort=2'  # oid是动态链接后面一串数字，sort=2是热门排序，sort=0是时间排序，这里是爬热门评论，所以一页就够了
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }  # 代理用户进行浏览器伪装
    html = urllib.request.Request(url=url, headers=headers)
    data = urllib.request.urlopen(html).read().decode('utf-8')
    # print(data)
    comment = re.findall(r'"content":{"message":"(.*?)"', data,
                         re.S)  # 用正则表达式扒所需要的评论内容获取
    rpid = re.findall(r'"rpid":\d*', data, re.S)  # 回复的pid获取
    mid = re.findall(r'"mid":\d+', data, re.S)  # 回复的uid获取
    huifu = zip(rpid, comment, mid)  # 整合
    # print(huifu)
    # print(rpid)
    print(len(comment))  # 输出每页有多少个回复
    zong += len(comment)  # 爬取的总回复数量
    comment_list.extend(huifu)  # 将评论内容一个个添加进空列表
print(zong)
print('评论已经爬取完成')
comment_txt = open(Folderpath + '\\huifu.txt', 'w',
                   encoding='utf-8')  # 创建txt文本

for r in comment_list:
    comment_txt.write(str(r))  # 写入txt文本
    comment_txt.write('\n')
comment_txt.write("评论总数为：%d" % zong)
comment_txt.close()
