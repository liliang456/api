import requests,json
post_url = 'https://fanyi.baidu.com/sug'
kw = input('请输入单词：')
header = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
data = {
    'kw':kw
}
res = requests.post(url=post_url,data=data,headers=header)
# 直接返回一个json对象，用于返回值是字符串类型的数据,content-type判断，application/json是json
dic_obj = res.json()
print(dic_obj['data'][0]['v'])
filename = kw+'.json'
fp = open(filename,'w',encoding='utf-8')
json.dump(dic_obj,fp=fp,ensure_ascii=False)
# res.json() 返回的是一个字典类型的数据
