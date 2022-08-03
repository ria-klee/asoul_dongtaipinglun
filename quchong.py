# 文本去重
import os

Folderpath = os.getcwd()

f3 = open(Folderpath + '\\quchong.txt', "r", encoding='utf-8')
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

with open(Folderpath + '\\quchong.txt', 'w', encoding='utf-8') as f:
    for i in range(len(text_list)):
        # s = str(i).split()
        s = str(text_list[i])
        s = s + '\n'
        f.write(s)
    print('================保存文件成功================')
