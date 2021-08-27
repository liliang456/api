import requests,os,time
from lxml import etree

url = 'https://aspx.sc.chinaz.com/query.aspx'
header = {
'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
if not os.path.exists('./rar'):
    os.mkdir('./rar')
for i in range(1,5):
    param = {
        'keyword':'免费',
        'issale':'',
        'classID':'864',
        'page':i
    }
    page_text = requests.get(url=url,headers=header,params=param).text
    tree = etree.HTML(page_text)
    div_list = tree.xpath('//div[@id="container"]/div')
    for div in div_list:
        href = 'https:'+div.xpath('./a/@href')[0]
        page = requests.get(url=href,headers=header).text
        tr = etree.HTML(page)
        li_list = tr.xpath('//div[@class="down_wrap"]/div[2]/ul/li[1]')
        t = time.time()
        for li in li_list:
            link = li.xpath('./a/@href')[0]
            yasuobao = requests.get(url=link,headers=header).content
            pat = 'rar/'+'简历模板'+str(t)+'.rar'
            with open(pat,'wb') as fp:
                fp.write(yasuobao)
                print('完成')
