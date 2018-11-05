import time
import requests
from bs4 import BeautifulSoup

names = []
scores = []

headers = {'User-Agent':'Mozilla/5.0 (iPhone; U; CPU iPhone OS 5_1_1 like Mac OS X; en) AppleWebKit/534.46.0 (KHTML, like Gecko) CriOS/19.0.1084.60 Mobile/9B206 Safari/7534.48.3'}
root_url = 'http://www.dyaihao.com/type/5.html'
i = 1
print('正在获取 %s' % root_url)
resp = requests.get(root_url, headers=headers, timeout=15)

while resp.status_code == 200:
    print('获取一个页面后暂停5秒\n')
    time.sleep(5)
    resp.encoding = 'utf-8'

    soup = BeautifulSoup(resp.text, 'lxml')

    # type(h3s) is list, 获取电影名
    h3s = soup.select('li h3')
    for h in h3s:
        # type(t) is str
        th = h.text
        names.append(th[3:])

    # 获取评分
    ps = soup.select('li p')
    for p in ps:
        tp = p.text
        scores.append(tp[:-1])

    # 是否有下一页
    next_p = soup.find('a', class_="btn btn-primary btn-block")
    if next_p is None:
        print('恭喜爬取完毕，正在输出至文本...')
        name_score = dict(zip(names, scores))
        fileObject = open('movie2.txt', 'w')
        for k, v in name_score.items():
            fileObject.write(str(k))
            fileObject.write(",")
            fileObject.write(str(v))
            fileObject.write('\n')
        fileObject.close()
        print('文本写入完毕！结束')
        break
    else:
        # 如果有进行地址组装，并跳转
        build_url = "http://www.dyaihao.com" + next_p['href']
        i += 1
        if 0 == i % 20:
            print('\n防反爬，暂停30秒\n')
            time.sleep(30)
        print('正在获取 %s' % build_url)
        resp = requests.get(build_url, headers=headers, timeout=60)
else:
    print('发生页面打开错误')
