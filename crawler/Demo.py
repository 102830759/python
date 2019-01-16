import urllib
from urllib import request
import re

import urllib.request
import urllib.parse
import re
import os








headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) '

'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'}

def download_page(url):
    request = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(request)
    dada = response.read()
    return dada


def get_image(html):
    regx = r'http://[\s]*\.jpg'
    pattern = re.compile(regx)
    get_image = re.findall(pattern, repr(html))
    num = 1
    for img in get_image:
        image = download_page(img)
        with open('%s.jpg' % num, 'web') as fp:
            fp.write(image)
            num += 1
            print('正在现在第%s张照片' % num)

    return


url = 'http://pic.yesky.com/15/621635015.shtml'
html = download_page(url)
get_image(html)
