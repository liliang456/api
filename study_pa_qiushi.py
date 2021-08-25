import requests

url = 'https://www.qiushibaike.com/pic/'
header = {
'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
res = requests.get(url=url)
print(res.text)