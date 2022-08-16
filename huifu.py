# 纯文本动态评论和pid爬取，可以用https://www.bilibili.com/h5/comment/sub?oid=[oid]&pageType=17&root=[rpid]直接跳转到指定评论

import os
import re
import time
import urllib.request

Folderpath = os.getcwd()
time.sleep(2)
comment_list = []  # 创建空列表
rpid_list = []  # 创建空列表
zong = 0
for i in range(100):  # 动态下面的评论总共有30页，一页30-100评论左右，往大了填就行
    url = 'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn=' + str(
        i) + '&type=17&oid=694983299970367512&sort=0'  # oid是动态链接后面一串数字，sort=2是热门排序，sort=0是时间排序
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}  # 代理用户进行浏览器伪装
    html = urllib.request.Request(url=url, headers=headers)
    data = urllib.request.urlopen(html).read().decode('utf-8')
    # print(data)
    comment = re.findall(r'"content":{"message":"(.*?)"', data, re.S)  # 用正则表达式扒所需要的评论内容获取，只爬了评论内容
    rpid = re.findall(r'"rpid":\d*', data, re.S)
    mid=re.findall(r'"mid":\d+', data, re.S)
    huifu = zip(rpid, comment,mid)
    # print(huifu)
    # print(rpid)
    print(len(comment))  # 输出每页有多少个回复
    zong += len(comment)
    comment_list.extend(huifu)  # 将评论内容一个个添加进空列表
print(zong)
print('评论已经爬取完成')
comment_txt = open(Folderpath + '\\huifu.txt', 'w', encoding='utf-8')  # 创建txt文本

for r in comment_list:
    comment_txt.write(str(r))  # 写入txt文本
    comment_txt.write('\n')
comment_txt.write("评论总数为：%d" % zong)
comment_txt.close()
