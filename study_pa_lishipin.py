import requests,random,json,re,os
from lxml import etree
from multiprocessing.dummy import Pool
header = {
'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
url = 'https://www.pearvideo.com/category_5'
page_text = requests.get(url=url,headers=header).text
tree = etree.HTML(page_text)
li_list = tree.xpath('//div[@id="listvideoList"]/ul/li')
url_lis = []
if not os.path.exists('./lishipin'):
    os.mkdir('./lishipin')
for li in li_list:
    detail_li = li.xpath('./div[@class="vervideo-bd"]/a/@href')[0]
    detail_name = li.xpath('./div[@class="vervideo-bd"]/a/div[2]/text()')[0]+'.mp4'
    video_url = 'https://www.pearvideo.com/'+detail_li
    video_name = detai_name+'.mp4'
    count = detail_li.split('_')[1]
    url_video_detail = 'https://www.pearvideo.com/videoStatus.jsp'
    param = {
        'contId':count,
        'mrd': str(random.random())
    }
    header_url = {
        'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        'Referer':'https://www.pearvideo.com/video_'+str(count),
        'Cookie': '__secdyid=70b476d4b22c0b3514ba63d27cddd5aa01ca04f714e4dd68021630476900; JSESSIONID=592593ED567287DC24E351B6374F44E6; PEAR_UUID=7e7789ae-9730-4eae-ad9f-496e755179ab; _uab_collina=163047682407048397647561; UM_distinctid=17b9fff2bc76b-075924a073ce19-3d644509-e1000-17b9fff2bc87d8; CNZZDATA1260553744=30359212-1630416087-https%253A%252F%252Fwww.baidu.com%252F%7C1630416087; Hm_lvt_9707bc8d5f6bba210e7218b8496f076a=1630476824,1630476905; p_h5_u=52E65F34-7951-4FE9-8871-C50A1BE3F037; acw_tc=781bad2516304852549891086e633d131d8f00bbee0032cba11cd636875d49; Hm_lpvt_9707bc8d5f6bba210e7218b8496f076a=1630485562; SERVERID=ed8d5ad7d9b044d0dd5993c7c771ef48|1630486800|1630476900'
    }
    detail_video_url = requests.get(url=url_video_detail,params=param,headers=header_url).text
    de = json.loads(detail_video_url)
    srcUrl = de['videoInfo']['videos']['srcUrl']
    new_url = re.sub(r'\/\d{13}-',f'/cont-{count}-',srcUrl)
    dic = {
        'name':detail_name,
        'url':new_url
    }
    url_lis.append(dic)
def get_content(dic):
    end_url = dic['url']
    print(dic['name'],'正在下载。。。')
    res = requests.get(url=end_url,headers=header).content
    intab = "?/|\><:*"
    title = dic['name']
    for s in intab:
        if s in title:
            title = title.replace(s, '')
    path = 'lishipin/' + title
    with open(path,'wb') as fp:
        fp.write(res)
    print(detail_name,'下载成功。。。')

pool = Pool(4)
pool.map(get_content,url_lis)
pool.close()
pool.join()


