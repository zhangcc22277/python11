

#倒库
import requests
from urllib.parse import urlencode
import os
from hashlib import md5
import json
#2取网页
def get_page(offset):
	#2.1定义参数属性是键值对，所以我们直接定义一个字典
	parames ={
		'offset':offset,
		'format':'json',
		'keyword':'车模',
		'autoload':'true',
		'count':'20',
		'cur_tab':'1'
	}

	#2.2拼接url		https://www.toutiao.com/search_content/?offset=0&format=json&keyword=%E8%BD%A6%E6%A8%A1&autoload=true&count=20&cur_tab=1&from=search_tab
	url='https://www.toutiao.com/search_content/?' +urlencode(parames)

	#2.3请求这个连接
	response = requests.get(url)

	#2.4如果我们的状态码位200，那么我才返回这个结果
	#拓展：200成功 400错误请求（服务器找不到请求的语法）404（服务器找不到你请求的网页，405方法禁用
	if response.status_code==200:
		return response.json()

#3、解析数据
	#3.1定义解析的方法
def get_images(html):
	data = html.get('data')

	if data:
		#3.2遍历数据，得到图片列表和标题
		for item in data:

			image_list = item.get('image_list')
			title=item.get('title')

			if image_list:
				for image in image_list:
					#3,3构建了一个生成器，目的：将图片连接和图片标题一并返回
					yield{
						'image':image.get('url'),
						'title':title
					}

#4、下载目标网页的数据
#定义一个函数，目的：实现一个保存图片的方法，item就是我们前面get_images()方法返回的一个字典
#item里面的title创建了一个文件夹，用来请求图片的连接
def save_image(item):

	if not os.path.exists(item.get('title')):#os.path.exists用于判断文件是否存在
		os.mkdir(item.get('title'))#创建文件夹

	#4.1获取连接
	local_image_url=item.get('image')
	#4.2请求图片并拼接连接
	response = requests.get('https:'+local_image_url)

	if response.status_code==200:
		file_path='{0}/{1}.{2}'.format(item.get('title'),md5(response.content).hexdigest(),'jpg')
		#{0}文件名称/{1}图片名称.{2}图片格式
		#hexdigest()返回一个十六进制的字符串值

		#判断我们的这个路径是否存在，如果不存在我就写入
		if os.path.exists(file_path):
			with op(file_path,'wb')as f:
				f.write(response.content)

#i当以一个main()函数，目的：构造一个offset数组，遍历offset，提取图片，将其下载


def main (offset):
	#5.1 get_page(offset)拿到数据
	html=get_page(offset)

	#5.2便利数据 打印标题 保存数据
	for item in get_images(html):
		print(item)
		save_image(item)

#6启动函数
if __name__ == '__main__':
	main(5)


