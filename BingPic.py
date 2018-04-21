import requests

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'
}

response = requests.get(url="https://cn.bing.com/HPImageArchive.aspx?format=js&idx=5&n=10&nc=1524303558367&pid=hp",headers=head)
hjson = response.json()
get_url = 'https://cn.bing.com' + hjson['images'][7]['url']
print(get_url)