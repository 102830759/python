import urllib.request
import urllib.parse
import re
import os

# 根据关键字下载百度图片

header = \
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        "referer": "https://image.baidu.com"
    }

# 获得数据的图片地址
def get_data(url):
    request = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(request)
    html_str = response.read().decode("utf-8")

    p = re.compile("thumbURL.*?\.jpg")
    # 获取正则匹配结果，返回的是一个list
    s = p.findall(html_str)
    file = "F:\\download\\图片"
    if os.path.isdir(file) != True:
        os.makedirs(file)

    for index, i in enumerate(s):
        get_image(i.replace("thumbURL\":\"", ""), file + "\\{num}.jpg".format(num=index + 1))

# 下载图片
def get_image(url, name):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    get_img = response.read()
    with open(name, 'wb') as fp:
        fp.write(get_img)
        print('下载完成')
    return


url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={word}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&word={word}&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&pn=30&rn=30&gsm=1e&1529645180862='
keyword = input("请输入关键字：\n")
keyword = urllib.parse.quote(keyword, "utf-8")
url1 = url.format(word=keyword)
get_data(url1)
