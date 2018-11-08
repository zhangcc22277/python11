#使用UDP的通信双方也分为客户端和服务器，服务器首先需要绑定端口
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定端口
s.bind(('127.0.0.1',9999)
#绑定端口和TCP一样，但是不需要调用listen()方法，
#而是直接接收来自任何客户端的数据
print('Bind UDP on 9999...')
wile True:
	#接受数据
	data,addr = s.recvfrom(1024)
	print('Received from %s:%s'%addr)
	s.endto(b'Hello,%s!'%data,addr)

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
for data in [b'Michael',b'Tracy',c'Sarah']
	#发送数据
	s.sendto(data,('127.0.0.1'9999))
	#接收数据
	print(s,recv(1024).decode('utf-8'))
s.close()