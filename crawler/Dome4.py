import urllib.request
import urllib.parse
import json
import os


# 获得数据的图片地址
def get_data(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    html_str = response.read().decode("utf-8")

    html_json = json.loads(html_str)
    subjects = html_json['subjects']
    file = "F:\\download\\图片"
    if os.path.isdir(file) != True:
        os.makedirs(file)
    for i in range(len(subjects)):
        get_image(subjects[i]['cover'], file + "\\" + subjects[i]['rate'] + "  " + subjects[i]['title'] + ".jpg")
    # for index, i in enumerate(s):
    #     get_image(i.replace("thumbURL\":\"", ""), file + "\\{num}.jpg".format(num=index + 1))


# 下载图片
def get_image(url, name):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    get_img = response.read()
    name = name.replace("/", "")
    with open(name, 'wb') as fp:
        try:
            fp.write(get_img)
            print('下载完成')
        except:
            print(name + "==》下载出错")
    return


url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%A7%91%E5%B9%BB&sort=rank&page_limit=20&page_start=0'

get_data(url)
