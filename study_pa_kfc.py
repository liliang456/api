import requests,json

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
kw = input('请输入地名:')
header = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
for i in range(1,11):
    data = {
        'cname':'',
        'pid':'',
        'keyword':kw,
        'pageIndex':i,
        'pageSize':'10'
    }
    res = requests.post(url=url, data=data, headers=header)
    page_text =json.loads(res.text)
    table = page_text['Table1']
    if len(table) != 0:
        fp = open('./kfc.json','w',encoding='utf-8')
        json.dump(table,fp=fp,ensure_ascii=False)
    else:
        print('爬取结束')
        break
