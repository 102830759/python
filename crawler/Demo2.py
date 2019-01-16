import urllib
import urllib.request

def get_image(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    get_img = response.read()
    with open('001.jpg','wb') as fp:
        fp.write(get_img)
        print('下载完成')
    return

url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E8%B6%B3%E7%90%83%E5%AE%9D%E8%B4%9D&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word=%E8%B6%B3%E7%90%83%E5%AE%9D%E8%B4%9D&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=30&rn=30&gsm=1e&1529645180862='
get_image(url)