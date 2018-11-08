#服务器编程
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#监听端口：
s.bind(('127.0.0.1',9999))
#调用listen（）方法开始监听端口，传入的参数指定等待连接的最大数量
s.listen(5)
print('Waiting for connection..')

#accept()会等待并返回一个客户端的连接
while Ture:
	#接受一个新连接
	socket,addr = s.accept()
	#创建新线程来处理TCP连接
	t= threading.THread(target=tcplink,args=(sock,addr))
	t.start()

#每个连接必须包创建新的线程（或进程）来处理，否则无法接受其他客户端的连接
def tcplink(sock,addr)	:
	print('Accept new connection from %s:%s...'%addr)
	sock.send(b'Welcome!')
	while Ture:
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8')=='exit':
			break
		sock.send(('Hello,%s!'%data.decode('utf-8')).encode('utf-8'))
	sock.close()
	print('connection from %s:%s close.'%addr)

#要测试这个服务器，编写客户端程序
s = sock.sock(sock.AF_INET,sock.SOCK_STREAM)
#建立连接
s.connect(('127.0.0.1',9999))
#接受欢迎消息
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael',b'Tracy',b'Sarah']:
	#发送数据
	s.send(data)
	print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()