import requests
from lxml import etree
header = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
url = 'https://www.baidu.com/?tn=88093251_83_hao_pg'
resp = requests.get(url=url,headers=header)
resp.encoding = 'utf-8'
page_text = resp.text
# tree = etree.HTML(page_text)
# li_list = tree.xpath('//*[@id="s_xmancard_news_new"]/div/div[1]/div/div')

# //*[@id="s_xmancard_news_new"]/div/div[1]/div/div
print(page_text)