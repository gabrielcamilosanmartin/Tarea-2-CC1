import math
import scipy
import scipy.special

def f1(x):
	print ('f1')
	return (math.sin(math.pi*(x/5)))/(math.pi*(x/5))
def f2(x):
	print ('f2')
	return x**2
def f3(x):
	print ('f3')
	return (x**3)+2
def f4(x):
	print ('f4')
	return math.floor(x/3)
def f5(x):
	print ('f5')
	return scipy.special.j0(x)
def f(n,x):
	if (n==1):
		return f1(x)
	elif(n==2):
		return f2(x)
	elif(n==3):
		return f3(x)
	elif(n==4):
		return f4(x)
	elif(n==5):
		return f5(x)



	
