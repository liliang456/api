import requests,os
from lxml import etree

url = 'https://pic.netbian.com/4kfengjing/'
header = {
'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
page_text = requests.get(url=url,headers=header).text
tree = etree.HTML(page_text)
list_li = tree.xpath('//div[@class="slist"]/ul/li')
if not os.path.exists('./pic'):
    os.mkdir('./pic')
for li in list_li:
    pic_link = 'https://pic.netbian.com' + li.xpath('./a/@href')[0]
    pag = requests.get(url=pic_link,headers=header).text
    tre = etree.HTML(pag)
    pic_url ='https://pic.netbian.com'+tre.xpath('//div[@class="photo-pic"]/a/img/@src')[0]
    title = tre.xpath('//div[@class="photo-pic"]/a/img/@title')[0]+'.jpg'
    title_detail = title.encode('iso-8859-1').decode('gbk')
    pic_data = requests.get(url=pic_url,headers=header).content
    pic_pat = 'pic/'+title_detail
    with open(pic_pat,'wb') as fp:
        fp.write(pic_data)
        print(title_detail,'下载完成')






    # src = 'https://pic.netbian.com'+li.xpath('./a/img/@src')[0]
    # alt = li.xpath('./a/img/@alt')[0]+'.jpg'
    # alt_detail = alt.encode('iso-8859-1').decode('gbk')
    # pic = requests.get(url=src,headers=header).content
    # picpath = 'pic/'+alt_detail
    # with open(picpath,'wb',) as fp:
    #     fp.write(pic)
    #     print(alt_detail,'下载成功。。。')