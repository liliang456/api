import requests,json

url = 'https://movie.douban.com/j/chart/top_list'
param = {
    'type':'5',
    'interval_id':'100:90',
    'start':'0',
    'limit': '20',
    'action':''
}
header = {
'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
res = requests.get(url=url,headers=header,params=param)
page_text = res.json()
print(page_text)
for title in page_text:
     ra = title['rating']
     ti = title['title']
     ac = title['actors']
     print(ra,ti,ac)
# filename = './douban.json'
# fp = open(filename,'w',encoding='utf-8')
# json.dump(page_text,fp=fp,ensure_ascii=False)
