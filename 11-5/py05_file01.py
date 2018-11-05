#将本地的一个文本文件读为一个str并打印出来

fpath = r'D:\test.txt'

with open(fpath,'r')as f:
	s = f.read()
	print(s)