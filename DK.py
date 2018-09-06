import re
import urllib.request
def get_content(url):
    html = urllib.request.urlopen(url)
    content = html.read().decode('utf-8')
    # content = html.read().decode('gb2312')
    html.close()
    return content

def get_images(info):
    src = r'<img class="BDE_Image" src="(.+?\.jpg)"'
    comp = re.compile(src)
    get_codes = re.findall(comp,info)
    i = 1
    for get_codes in get_codes:
        urllib.request.urlretrieve(get_codes, r'C:\Users\王刚\Desktop\新建文件夹 (2)\%s.jpg' % i)
        i = i + 1

if __name__ == '__main__':
    info = get_content('http://desk.zol.com.cn/')
    print(info)
    get_images(info)