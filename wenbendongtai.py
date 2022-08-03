# 纯文本动态评论爬取
import os
import re
import time
import urllib.request

Folderpath = os.getcwd()
time.sleep(2)
comment_list = []  # 创建空列表
rpid_list = []  # 创建空列表
zong = 0
for i in range(50):  # 动态下面的评论总共有30页，一页30-100评论左右，往大了填就行
    url = 'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn=' + str(
        i) + '&type=17&oid=687193083747500039&sort=0'  # oid是动态链接后面一串数字，sort=2是热门排序，sort=0是时间排序
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}  # 代理用户进行浏览器伪装
    html = urllib.request.Request(url=url, headers=headers)
    data = urllib.request.urlopen(html).read().decode('utf-8')
    # print(data)
    comment = re.findall(r'"content":{"message":"(.*?)"', data, re.S)  # 用正则表达式扒所需要的评论内容获取，只爬了评论内容
    rpid = re.findall(r'"rpid":\d*', data, re.S)
    # print(comment)
    # print(rpid)
    print(len(comment))  # 输出每页有多少个回复
    zong += len(comment)
    comment_list.extend(comment)  # 将评论内容一个个添加进空列表
    rpid_list.extend(rpid)
print(zong)
print('评论已经爬取完成')
comment_txt = open(Folderpath + '\\pinglun.txt', 'w', encoding='utf-8')  # 创建txt文本
huifu_txt = open(Folderpath + '\\pid.txt', 'a', encoding='utf-8')  # 创建txt文本

for r in comment_list:
    comment_txt.write(r)  # 写入txt文本
    comment_txt.write('\n')
comment_txt.write("评论总数为：%d" % zong)
comment_txt.close()

for p in rpid_list:
    huifu_txt.write(p)  # 写入txt文本
    huifu_txt.write('\n')
huifu_txt.close()

f3 = open(Folderpath + '\\pinglun.txt', "r", encoding='utf-8')
text_list = []
s = set()
document = f3.readlines()
document_num = int(len(document))
print('原条数：' + str(document_num))
print('================去重中================')
content = [x.strip() for x in document]
# print(content)

for x in range(0, len(content)):
    url = content[x]
    if url not in s:
        s.add(url)
        text_list.append(url)

filename = int(len(text_list))
print('现条数：' + str(filename))
print('减少了：' + str(document_num - filename))

with open(Folderpath + '\\quchong.txt', 'a+', encoding='utf-8') as f:
    for i in range(len(text_list)):
        # s = str(i).split()
        s = str(text_list[i])
        s = s + '\n'
        f.write(s)
    print('================保存文件成功================')
