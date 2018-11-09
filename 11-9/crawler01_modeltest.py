
#1。倒库
import requests
from urllib.parse import urlencode
import os
from hashlib import md5

#2获取网页
def get_page(offset):
	#2.1定义参数属性的键值对，所以我们就直接定义一个字典
	parames={
		'offset':offset,
		'format':'json',
		'keyword':'车模',
		'autoload':'true',
		'count':'20',
		'cur_tab':'3',
		'from':'search_tab'
	}

	#2.2拼接url		https://www.toutiao.com/search_content/?offset=0&format=json&keyword=%E8%BD%A6%E6%A8%A1&autoload=true&count=20&cur_tab=1&from=search_tab
	url = 'https://www.toutiao.com/search_content/?'+urlencode(parames)
	#2.3请求这个链接
	response = requests.get(url)

	#2.4如果我们的状态码为200，返回这个结果
	if response.status_code==200:
		return response.json()

#3.解析数据
	#3.1定义解析的方法
def parse_page(html):
	data = html.get('data')

	#3.2遍历数据，得到图片和标题
	for item in data:
		image_list = item.get('image_list')
		title = item.get('title')

		#3.3构建一个生成器，目的：将图片链接和图片标题一并返回
		if image_list:
			for image in image_list:
				yield{
					'image':image.get('url'),
					'title':title
				}

#4.下载目标网页的数据
#定义一个函数，目的：实现一个保存图片的方法，item就是我们前面get_image()方法
#item里面的title创建了一个文件夹，用来请求图片的连接
def save_image(item):
	
	if not os.path.exists(item.get('title')):#os.path.exists就是用来判断文件是不是存在
		os.mkdir(item.get('title'))
	#4.1 获取连接
	local_image_url=item.get('image')
	#4.2请求图片并拼接连接
	response=requests.get('https:'+local_image_url)

	if response.status_code==200:
		file_path='{0}/{1}.{2}'.format(item.get('title'),md5(response.content).hexdigest(),'jpg')
		#hexdigest()返回一个十六进制的字符串值

		#4.3判断我们的这个路径是否存在，如果不存在就写入
		if not os.path.exists(file_path):
			with open(file_path,'wb')as f:
				f.write(response.content)

#5定义主函数
def main(offset):
	#5.1get_page(offset)拿到数据
	html=get_page(offset)
	for item in parse_page(html):
		print(item)
		save_image(item)

#6启动主函数
if __name__ == '__main__':
	main(1)

