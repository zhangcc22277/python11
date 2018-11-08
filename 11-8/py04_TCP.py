#socket

#导入socket数据库
import socket
#创建一个socket
#AF_INET指定使用IPV4协议，如果用更先进的IPV6，就指定为AF_INET6
#SOCK_STREAM指定使用面向流的TCP协议，这样，一个Socket对象就创建成功了
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#建立连接
s.connect(('www.sina.com.cn',80))

#发送数据
s.send(b"GET/HTTP/1.1\r\nHost:www.sina.com.cn\r\nConnection:Close\r\n\r\n")

#接受数据
buffer=[]
while Ture:
	#每次最多接受1k字节：
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break
data = b''.join(buffer)

#关闭连接
s.close()

#把网页的内容保存到文件：
header,html = data.split(b'/r/b/r/n')
print(header.decode('utf-8'))
#把接收的数据写入文件：
with open('sina.html','wb')as f:
	f.write(html)
