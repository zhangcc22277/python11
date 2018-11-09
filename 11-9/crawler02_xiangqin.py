
#设置条件
#解析网页
#保存图片
#保存信息
import requests
import os
#http://www.7799520.com/api/user/pc/list/search?startage=21&endage=30&gender=2&marry=1&page=1
#http://www.7799520.com/api/user/pc/list/search?startage=31&endage=40&gender=2&marry=1&page=1
#设置年龄
def query_age():
	age=int(input('请输入期望对方年龄（如20）：'))
	if 21<= age <=30:
		startage=21
		endage=30
	elif 31<= age <=40:
		startage=31
		endage=40
	else:
		startage=0
		endage=0
	#print(startage)
	return startage,endage
#设置性别
def query_sex():
	sex=input('请输入期望对方性别（如，男）：')
	if sex =='男':
		gender=1
	else:
		gender=2
	return gender
#设置身高
def query_height():
	height=int(input('请输入对方身高（如：162）:'))
	#身高区域进行判断
	if 151<=height<=160:
		startheight=151
		endheight=160
	elif 161<=height<=170:
		startheight=161
		endheight=170
	elif 171<=height<=180:
		startheight=171
		endheight=180
	elif 181<=height<=190:
		startheight=181
		endheight=190
	else:
		startheight=0
		endheight=0
	#返回对应的起始身高和终止身高
	return startheight,endheight

def query_monery():
	money = int(input('请输入期望的对方月薪(如8000):'))
	if 2000<=money<5000:
		salary=2
	elif 5000<=money<10000:
		salary =3
	elif 10000<=money<=20000:
		salary=4
	elif 20000<money:
		salary=5
	else:
		salary=0
	return salary

#查询符合条件的数据
def query_data():
	print('请输入你的筛选条件，考试本次婚缘')
	#年龄
	startage,endage=query_age()
	#性别
	gender=query_sex()
	#身高
	startheight,endheight=query_height()
	#薪资
	salary=query_monery()

	for i in range(1,11):
		#解析网站
	#http://www.7799520.com/api/user/pc/list/search?startage=21&endage=30&gender=2&startheight=161&endheight=170&marry=1&salary=3&page=1		json = get_one(i,startage,endage,gender,startheight,endheight,salary):
		json = get_one(i,startage,endage,gender,startheight,endheight,salary)
		for item in json['data']['list']:
			#print(item)
			#保存图片
			save_image(item)

def save_image(item):
	if not os.path.exists('images'):
		os.mkdir('images')

	image_url=item['avatar']
	response=requests.get(image_url)
	if response.status_code==200:
		file_path='images/{}.jpg'.format(item['username'])
		if not os.path.exists(file_path):
			print('正在获取：%s的信息'%item['username'])
			with open(file_path,'wb')as f:
				f.write(response.content)
				#获取图片内容，一音频
		else:
			print('已经下载过')

#解析网站
def get_one(page,startage,endage,gender,startheight,endheight,salary):
	#请求头
	headers={
		'Referer':'http://www.7799520.com/jiaoyou.html',
		'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
	}
	base_url='http://www.7799520.com/api/user/pc/list/search?startage={}&endage={}&gender={}&startheight={}&endheight={}&marry=1&salary={}&page={}'.format(startage,endage,gender,startheight,endheight,salary,page)
	#print(base_url)
	while True:
		try:
			response =requests.get(base_url,headers=headers)
			if response.status_code==200:
				return response.json()
		except:
			return None

query_data()