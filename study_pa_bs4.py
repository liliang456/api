from bs4 import BeautifulSoup
import requests

url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
header = {
'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
page_text = requests.get(url=url,headers=header)
page_text.encoding = 'utf-8'
soup = BeautifulSoup(page_text.text,'lxml')
fp = open('./sanguo.txt','w',encoding='utf-8')
for li in soup.select('.book-mulu > ul > li'):
    title = li.a.string
    detail_url = 'https://www.shicimingju.com'+li.a['href']
    detail_text = requests.get(url=detail_url,headers=header)
    detail_text.encoding = 'utf-8'
    soup_detail = BeautifulSoup(detail_text.text,'lxml')
    content = soup_detail.find('div',class_='chapter_content').text
    fp.write(title+':'+content+'\n')
    print(title+'爬取成功！')