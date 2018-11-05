#对函数fact（n）编写doctest并执行

def fact(n):
	'''
	Calculate 1*2*...*n

	>>> fact(1)
	1
	>>> fact(10)
	3628800
	>>> fact(-1)
	Traceback (most recent call last):
	    ...
	ValueError
	'''
	if n<1:
		raise ValueError()
	if n==1:
		return 1
	return n*testmod()