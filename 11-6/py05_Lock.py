#线程锁
#由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，
# 所以，不会造成修改的冲突。
# 创建一个锁就是通过threading.Lock()来实现：

import time,threading

#假定这是你的银行存款
balance = 0
def chang_it(n):
	#现存后取，结果应该是为0：
	global balance
	balance = balance+n
	balance = balance-n

def run_thread(n):
	for i in range(100000):
		chang_it(n)

t1 = threading.Thread(target=run_thread,arg=(5,))
t2 = threading.Thread(target=run_thread,arg=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)