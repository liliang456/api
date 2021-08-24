import requests,json
url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
header = {
'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
page_id = []
page_detail = []
for i in range(1,3):
    data = {
        'on': 'true',
        'page': i,
        'pageSize': '15',
        'productName':'' ,
        'conditionType': '1',
        'applyname': '',
        'applysn': '',
    }
    res = requests.post(url=url,data=data,headers=header).json()
    r = res['list']
    for ids in r:
        id = ids['ID']
        page_id.append(id)
url_detail = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
for a_id in page_id:
    data = {
        'id':a_id
    }
    resu_detail = requests.post(url=url_detail,headers=header,data=data).json()
    page_detail.append(resu_detail)
    for page_de in page_detail:
        name = page_de['epsName']
        print(name)
    # fp = open('./detail.json','w',encoding='utf-8')
    # json.dump(page_detail,fp=fp,ensure_ascii=False)
print('over!!!')