import requests
from requests import RequestException
import re
import json
from multiprocessing import Pool
head = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36',
        'Referer':'http://maoyan.com/board/2'}
def get_one_page(url):
    try:
        response=requests.get(url,headers=head)
        if response.status_code==200:
            return response.text
        return None
    except RequestException:
        return None

def parse_html(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                       +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                       +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'image':item[1],
            'index':item[0],
            'title':item[2],
            'actor':item[3].strip()[3:],
            'time':item[4].strip()[5:],
            'score':item[5]+item[6]
    }
def write_html(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()

def main(offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    get_one_page(url)
    html = get_one_page(url)
    for item in parse_html(html):
        print(item)
        write_html(item)

if __name__ == '__main__':
    pool = Pool()
    pool.map(main,[i*10 for i in range(10)])