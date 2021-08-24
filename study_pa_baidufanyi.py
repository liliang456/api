import requests,json
def get_word():
    try:
        post_url = 'https://fanyi.baidu.com/sug'
        kw = input('请输入单词：')
        header = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }
        data = {
            'kw':kw
        }
        res = requests.post(url=post_url,data=data,headers=header)
        # 直接返回一个json对象，用于返回值是字符串类型的数据,content-type判断，application/json是json
        dic_obj = res.json()
        print(dic_obj['data'][0]['v'])
        filename = kw+'.json'
        fp = open(filename,'w',encoding='utf-8')
        json.dump(dic_obj,fp=fp,ensure_ascii=False)
        # res.json() 返回的是一个字典类型的数据
    except Exception:
        print('程序出错了，请重新查找')

if __name__ == '__main__':
    i = 10
    while True:
        get_word()
        i = i-1
        if i == 0:
            print('查询机会不满'+str(i) +'次,歇一会儿吧' )
            break