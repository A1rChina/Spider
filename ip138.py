import requests
import re
print("输入IP地址或者域名：")

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6'
}

url = str(input())
urls = requests.get('http://www.ip138.com/ips1388.asp?ip='+ url +'&action=2',headers=header)
urls.encoding = 'gb2312'
pattern = re.compile(r'<li>(.*?)</li>',re.S)
items = re.findall(pattern,urls.text)
for item in items:
    print(item)
