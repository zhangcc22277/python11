import urllib.request
import os
from bs4 import BeautifulSoup
 
try:
    siteURL = 'https://my.hupu.com/search?fid=34&type=topic&q=%E3%80%8A%E4%B8%8D%E5%86%B7%E7%AC%91%E8%AF%9D%E3%80%8B%E7%AC%AC'
    start_html = urllib.request.urlopen(siteURL).read().decode('utf8')
    Soup = BeautifulSoup(start_html, 'html.parser')
    td_list = Soup.find_all('td', class_='p_title')
    for x in td_list:
        link = x.a['href']
        text = x.get_text()
        html = urllib.request.urlopen(link).read().decode('utf8')
        html_soup = BeautifulSoup(html, 'html.parser')
        name = html_soup.find('div', class_="subhead").span.get_text()
        path = os.path.join("D:\\buleng", name)
        if os.path.exists(path):
            continue
        else:
            os.mkdir(path)
            os.chdir(path)
 
        a_list = html_soup.find('div', class_="floor_box").find_all('img')
        i = 1
        for list in a_list:
            urllib.request.urlretrieve(list['src'], '{0}.gif'.format(i))
            i += 1
        print(name + '---- 下载完成')
    print('--------全部下载完成--------')
except urllib.error.URLError as e:
    print(e.reason)
