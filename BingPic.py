import requests
import os
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
}

def get_img_url():
    for idx in range(8):
        response = requests.get(url="https://cn.bing.com/HPImageArchive.aspx?format=js&n=10&idx="+str(idx),headers=head)
        hjson = response.json()
        get_url = 'https://cn.bing.com' + hjson['images'][0]['url']
        get_title = hjson['images'][0]['enddate']
        img_date = requests.get(get_url,headers=head).content
        with open('%s.jpg'%get_title,'wb') as f:
            f.write(img_date)
            print('正在下载',get_title)


if __name__ == '__main__':
    get_img_url()
