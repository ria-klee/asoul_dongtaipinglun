# asoul_dongtaipinglun
### 爬取asoul成员动态下面的评论，方便找到成员回复或者制作词云等
~~***入门水平，能用就行***~~
### 纯文字动态以2022/08/16嘉然动态里晚晚的回复为例
#### 运行huifu.py后在py文件所在文件夹找到huifu.txt,在里面搜索晚晚的uid即可找到* ('"rpid":125972903024', '来啦来啦！！！！', '"mid":672346917') ,之后再用https://www.bilibili.com/h5/comment/sub?oid=[oid]&pageType=17&root=[rpid] 直接跳转即可,也就是https://www.bilibili.com/h5/comment/sub?oid=694983299970367512&pageType=17&root=125972903024
--- 
### 带图动态的评论跳转以2022/08/23泠鸢yousa 的合作动态为例（https://t.bilibili.com/697547811817783319 ）
#### ①用https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/get_dynamic_detail?dynamic_id=697547811817783319 获取带图动态的oid，data--card--desc--rid就是该动态的oid
#### ②用https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn=0&type=11&oid=204927380&sort=2 获取热门动态，可以看到第一条就是嘉然的回复且data--replies--0中含有rpid：127041315696和oid：204927380，再使用这两个参数的具体数值就可以得到回复的跳转链接：https://www.bilibili.com/h5/comment/sub?oid=204927380&pageType=11&root=127041315696
