import requests
from lxml import etree
url = 'https://www.aqistudy.cn/historydata/'
header = {
'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
city_lis = []
page_text = requests.get(url=url,headers=header).text
tree = etree.HTML(page_text)
li_list = tree.xpath('//div[@class="bottom"]/ul/li | //div[@class="bottom"]/ul/div[2]/li')
for li in li_list:
    city = li.xpath('./a/text()')[0]
    city_lis.append(city)
print(city_lis,len(city_lis))