import requests,re
from lxml import etree

url = 'https://maoyan.com/films'
header = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
param = {
    'showType':'2'
}
page_text = requests.get(url=url,headers=header,params=param).text
from fontTools.ttLib import TTFont
woff = re.search(r"url\('(.*\.woff)'\)", page_text).group(1)
woff_url = 'http:' + woff
response_woff = requests.get(woff_url, headers=header).content
with open('get_fonts.woff','wb')as f:
    f.write(response_woff)
    font = TTFont("basefonts.woff")
    font.saveXML('basefonts.xml')
baseFonts = TTFont('basefonts.woff')
base_nums = ['7', '6', '3', '8', '4', '2', '9', '5', '1', '0']
base_fonts = ['uniF45D', 'uniE59B', 'uniF4C9', 'uniE9ED', 'uniF081', 'uniE7E8', 'uniEE90', 'uniE8C9', 'uniE753','uniF675']
onlineFonts = TTFont('get_fonts.woff')
uni_list = onlineFonts.getGlyphNames()[1:-1]
temp = {}
for i in range(10):
    onlineGlyph = onlineFonts['glyf'][uni_list[i]]
    print('1-------',onlineGlyph)
    for j in range(10):
        baseGlyph = baseFonts['glyf'][base_fonts[j]]
        print('2-------', baseGlyph)
        if onlineGlyph == baseGlyph:
            temp["&#x" + uni_list[i][3:].lower() + ';'] = base_nums[j]
# pat = '(' + '|'.join(temp.keys()) + ')'
# print(pat)
# response_index = re.sub(pat, lambda x: temp[x.group()], page_text)
# print(response_index)
# tree = etree.HTML(page_text)
# dd = tree.xpath('//div[@class="movies-list"]//dd')
# for div in dd:
#     title = div.xpath('./div[2]/a/text()')[0]
#     print(title)





# base_fonts = ['uniF2DD', 'uniF747', 'uniF01C', 'uniEBD0', 'uniEA1B', 'uniE897', 'uniE477', 'uniF53B', 'uniF1DF','uniE38B']
# onlineFonts = TTFont("jiemi.woff")
# # onlineFonts.saveXML('jiemi.xml')
# uni_list = onlineFonts.getGlyphNames()[1:-1]
# base_font = baseFonts.getGlyphNames()[1:-1]
#
# temp = {}
# #因为字体是动态加载出来的，所以需要实现字体的一一对应：
# for i in range(10):
#     onlineGlyph = onlineFonts['glyf'][uni_list[i]]
#     print('1---------',onlineGlyph)
#     for j in range(10):
#         baseGlyph = baseFonts['glyf'][base_font[j]]
#         print('2--------',baseGlyph)
        # if onlineGlyph == baseGlyph:
        #     temp["&#x" + uni_list[i][3:].lower() + ';'] = base_nums[j]