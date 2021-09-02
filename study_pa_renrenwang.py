import requests,json
from lxml import etree
import base64
header = {
'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
'Content-Type':
    'application/json'
}
# url_ick = 'http://rrwapi.renren.com/icode/v1/getBase64ImgCode'
# data_ick = {"type":1,
#         "appKey":"bcceb522717c2c49f895b561fa913d10",
#         "sessionKey":"",
#         "callId":"1630394333867",
#         "sig":"90643a035e3ab40f4847f75da7371238"
#         }
# resp_ick = requests.post(url=url_ick,data=json.dumps(data_ick),headers=header).text
# ick_ = json.loads(resp_ick)
# ick = ick_['data']['ick']
# image = ick_['data']['imageBase64String']
# image_data = base64.b64decode(image)
# with open('./image.jpg','wb') as fp:
#     fp.write(image_data)
# from chaojiying_Python.chaojiying import Chaojiying_Client
# chaojiying = Chaojiying_Client('wangdagou', 'li6679964', '921860')  # 用户中心>>软件ID 生成一个替换 96001
# im = open('image.jpg', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
# verify = chaojiying.PostPic(im, 1004)
# url_login = 'http://rrwapi.renren.com/account/v1/loginByPassword'
# data_login = {"user":"15264292923",
#         "password":"7146b317e364ceda1f48cafbdd9d539a",
#         "appKey":"bcceb522717c2c49f895b561fa913d10",
#         "sessionKey":"",
#         "callId":"1630393073673",
#         "sig":"c17c809a1b2f839222ba7678493fcbb6",
#         "verifyCode":verify['pic_str'],
#         "ick": str(ick)
#         }
# res = requests.post(url=url_login,data=json.dumps(data_login),headers=header).text
# print('1---------',res)

url_detail = 'http://www.renren.com/personal/325168886'
session = requests.session()
detail_text = session.get(url=url_detail,headers=header).text
with open('./renren.html','w',encoding='utf-8') as fp:
        fp.write(detail_text)
# print(detail_text)


# url_html = 'http://www.renren.com/login'
# page_text = requests.get(url=url_html,headers=header).text
# print(page_text)
# tree = etree.HTML(page_text)
# image_url = tree.xpath('//*[@id="app"]/div[3]/div/div[1]/div[2]/div[2]/div[3]/div/img/@src')
# print(image_url)
