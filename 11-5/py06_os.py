#利用os模块编写一个能实现dir -1输出的程序

import os,time,sys
from pprint import pprint

class ls:
	#输出格式的设定
	def __init__(self,path='.'):
		self.path=path

	def output(self):
		localtime = time.localtime()
		Time = '/'.join([str(x) for x in localtime[0:3]])
		
		if os.name =='nt':
			print ('-'*30)
			print("{: ^30}.format('OS:Windows')")
			print('-'*30)
		print('{:<{}}{:>}'.format('time',30-len(Time),Time))

		#实现ls-l
		#获取文件夹下的文件个数，只取一层
		def numOfFile(self,path,num=1):
			try:
				if os.path.isdir(path):
					for x in os.listdir(path:
						num +=1
			except BaseException:
				pass
			finally:
				return num

#二进制码转换为权限码
	def num2chmod(self,numstr):
		chmod =['r','w','x']
		words = ''
		for i,x in enumerate(numstr):
			if x =='1':
				words +=(lambda i, chmod : chmod[i % 3])(i, chmod)
			else:
				words +="-"
		return words

	def listdir(self):
		self.output()
		print('权限\t    文件数\t     用户ID\t     群组\t     文件修改\t     日期\t     大小\t     文件名\t')
		for x in os.listdir(self.path):
			dir = os.path.join(self.path,x)

			#显示dir路径文件的信息
			stat = os.stat(dir)
			#输出INode保护模式的信息
			print(self.num2chmod(str((bin(stat.st_mode)[-9:]))),end='\t')
			#输出该路径下的文件数量
			print(self.numOfFile(dir),end='\t\t')
			#输出该用户Id和群组ID
			print (stat.st_uid,end='\t'*2)
			print(stat.st_gid,end='\t'*2)
			#输出每个文件的修改时间：

			print('/'.join(str(x) for x in time.localtime(stat.st_mtime)[0:3]),end='\t   ')
			print(stat.st_size,end='\t'*2)
			print (x)
	def __call__(self,*args,**kwargs):
		self.listdir()

if __name__ == '__main__':
	ls(sys.argv[1])()


