# 带图片的动态评论爬取
import re
import time
import urllib.request

time.sleep(2)
comment_list = []  # 创建空列表
zong = 0
for i in range(100):  # 动态下面的评论总共有100页，一页30-100评论左右，往大了填就行
    url = 'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn=' + str(
        i) + '&type=11&oid=199507248&sort=2'  # 动态评论的接口（请大家不要恶意攻击造成负荷）
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}  # 代理用户进行浏览器伪装
    html = urllib.request.Request(url=url, headers=headers)
    data = urllib.request.urlopen(html).read().decode('utf-8')
    # print(data)
    comment = re.findall(r'"content":{"message":"(.*?)"', data, re.S)  # 用正则表达式扒所需要的评论内容获取，只爬了评论内容
    # print(comment)
    print(len(comment))  # 输出每页有多少个回复
    zong += len(comment)
    comment_list.extend(comment)  # 将评论内容一个个添加进空列表
print(zong)
print('评论已经爬取完成')
comment_txt = open('D:/2.txt', 'w', encoding='utf-8')  # 创建txt文本

for r in comment_list:
    comment_txt.write(r)  # 写入txt文本
    comment_txt.write('\n')
comment_txt.close()
