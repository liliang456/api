import requests
url='https://www.sogou.com/web'
kw = input('输入要查找的内容：')
param = {
    'query':kw
}
header = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
res = requests.get(url=url,params=param,headers=header)
page_text = res.text
filename = kw+'.html'
with open(filename,'w',encoding='utf-8') as f:
    f.write(page_text)
print(kw,'打印成功')